from aider.coders import Coder
from aider.models import Model
from execution_plan import create_execution_plan, load_requirements
import os

# This is a list of files to add to the chat

import re
from pathlib import Path
    
def clean_csv(input_file, output_file, expected_columns=5):
    error_lines = []
    cleaned_lines = []

    with open(input_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            # Check for irregularities
            columns = line.split(',')
            if len(columns) != expected_columns:
                error_lines.append((line_number, len(columns), line.strip(), "Incorrect number of columns"))
            else:
                # Check for inconsistent quoting or special characters
                if any('"' in col and not col.startswith('"') and not col.endswith('"') for col in columns):
                    error_lines.append((line_number, len(columns), line.strip(), "Inconsistent quoting or special characters"))
                else:
                    cleaned_lines.append(line)

    # Write cleaned content to the new file
    with open(output_file, 'w') as clean_file:
        for line in cleaned_lines:
            clean_file.write(line)

    return error_lines, output_file


def swap_cleaned_csvs(coder):
    # Get all CSV files in the ./seeds/ directory
    csv_files = list(Path('./seeds/').rglob('*.csv'))

    for csv_file in csv_files:
        input_file_path = str(csv_file)
        output_file_path = str(csv_file.parent / f"cleaned_{csv_file.name}")

        # Clean the CSV file and get error lines
        errors, cleaned_file = clean_csv(input_file_path, output_file_path)

        if errors:
            print(f"Irregularities found in the following lines of {input_file_path}:")
            for error in errors:
                print(f"Line {error[0]}: {error[2]}")
        else:
            print(f"No irregularities found in {input_file_path}. Cleaned file saved to {cleaned_file}.")
            # Remove the old file
            os.remove(input_file_path)
        
    staging_models_filenames = find_files_by_regex(os.path.join(os.getcwd(), 'models/staging'), r'.*\.sql$')
    coder.run(f"Replace the ref('raw_') with ref('cleaned_raw_') in the following files as the name of the seed csvs as changed: {staging_models_filenames}")


def check_success_dbt_build(coder):
    success = False
    counter = 0
    while not success:
        dbt_build_response = coder.run("/run dbt build")
        # Define the regex pattern to find the number of errors
        error_pattern = re.compile(r'\bERROR=(\d+)')

        # Search for the pattern in the log message
        match = error_pattern.search(dbt_build_response)
        if match:
            error_count = int(match.group(1))
            if error_count > 0:
                print("Error found in dbt build log message.")
            else:
                print("No error found in dbtlog message.")
            if 'raw_' in dbt_build_response:
                swap_cleaned_csvs(coder)
            else:
                coder.run(f"Fix the error in code. When I run dbt build I get the following error: \n {dbt_build_response}")
        else:
            print("No error information found in log message.")
            success = True
        counter += 1
        if counter > 5:
            break
    
    return success


def extract_filenames(response):
    # Define the regex pattern to match filenames with paths ending with sql, yml, md, yaml, csv
    pattern = re.compile(r'(\S+\.(sql|yml|md|yaml|csv))')
    # Find all matches in the response
    matches = pattern.findall(response)
    # Extract the filenames from the matches and remove unwanted characters
    filenames = list(set([re.sub(r"[`'*]", "", match[0]) for match in matches]))
    return filenames

def find_files_by_regex(directory, pattern):
    regex = re.compile(pattern)
    return [str(file.relative_to(directory)) for file in Path(directory).rglob('*') if regex.match(file.name) and 'venv' not in file.parts and 'target' not in file.parts and not any(part.startswith('.') for part in file.parts)]

def generate_code(branch_name, project_name, requirements_file):
    requirements = load_requirements(requirements_file)
    execution_plan = create_execution_plan(branch_name, project_name, requirements)
    config_filenames = find_files_by_regex(os.getcwd(), r'.*\.(yml|yaml)$')
    docs_filenames = find_files_by_regex(os.getcwd(), r'.*\.md$')
    staging_filenames = find_files_by_regex(os.path.join(os.getcwd(), 'models/staging'), r'.*\.(sql|md|yml)$')
    staging_models_filenames = find_files_by_regex(os.path.join(os.getcwd(), 'models/staging'), r'.*\.sql$')
    models_filenames = find_files_by_regex(os.path.join(os.getcwd(), 'models'), r'.*\.sql$')
    all_filenames = find_files_by_regex(os.getcwd(), r'.*\.(sql|md|yml|yaml|csv)$')
    file_categories = {
        "Config Files": config_filenames,
        "Docs Files": docs_filenames,
        "Staging Files": staging_filenames,
        "Staging Models Files": staging_models_filenames,
        "Models Files": models_filenames,
        "All Files": all_filenames
    }

    for category, filenames in file_categories.items():
        print(f"{category}:")
        for filename in filenames:
            print(f"  - {filename}")


    model = Model(
        "gpt-4o-2024-08-06",
        weak_model="gpt-4o-mini"
    )
    model.edit_format = "diff"
    model.use_repo_map = True
    model.accepts_images = True
    model.lazy = True
    model.reminder = "sys"

    # # Create a coder object
    coder = Coder.create(auto_lint=False, main_model=model, fnames=all_filenames)

    # Run git checkout to switch to the new branch
    checkout_command = f"git checkout -b {branch_name}-brewery-shop-example"
    print(f"Running shell command: {checkout_command}")
    os.system(checkout_command)

    for i, step in enumerate(execution_plan):
        response = coder.run(step)
        any_new_files = False
        if response:
            edit_filenames = extract_filenames(response)
            for filename in edit_filenames:
                if not any(filename in filepath for filepath in all_filenames):
                    # Check if the file is a CSV or SQL file and if it is inside the seeds or models folder
                    if (filename.endswith('.csv') or filename.endswith('.sql')) and ('seeds' in filename or 'models' in filename):
                        abs_path = os.path.abspath(filename)
                        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
                        with open(abs_path, 'w') as f:
                            pass
                        any_new_files = True
                        # Add the new file to git tracking
                        git_add_command = f"git add {abs_path}"
                        print(f"Running shell command: {git_add_command}")
                        os.system(git_add_command)
                        # Add the new file to the filenames in Coder
                        coder.add_rel_fname(filename)

            if any_new_files:
                new_msg = f"Recreate the response ONLY for skipped files in previous response: \n {response}. The task to solve is {step}."
                coder.run(new_msg)
        if i%4 == 0:
            check_success_dbt_build(coder)
    check_success_dbt_build(coder)

if __name__ == "__main__":
    generate_code()
       
