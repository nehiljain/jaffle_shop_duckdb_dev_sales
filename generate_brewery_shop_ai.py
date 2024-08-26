from aider.coders import Coder
from aider.models import Model
from execution_plan import execution_plan, branch_name
import os
# This is a list of files to add to the chat

import re
from pathlib import Path


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
    print(step)
    response = coder.run(step)
    print("~~"*100)
    print(response)
    print("~~"*100)
    if response:
    #     # Check if the response contains a shell command
    #     shell_command_match = re.search(r'```bash\n(.*?)\n```', response, re.DOTALL)
    #     if shell_command_match:
    #         shell_command = shell_command_match.group(1).strip()
    #         print(f"Running shell command: {shell_command}")
    #         coder.handle_shell_commands(shell_command)
        edit_filenames = extract_filenames(response)
        print("~~"*100)
        print(f"Filenames being edited {edit_filenames}")
        print("~~"*100)

        # Check if edit_filenames match any of the items in all_filenames, if not create an empty file
        for filename in edit_filenames:
            if not any(filename in filepath for filepath in all_filenames):
                print(f"{filename} doesn't exist and WILL BE CREATED")
                abs_path = os.path.abspath(filename)
                os.makedirs(os.path.dirname(abs_path), exist_ok=True)
                with open(abs_path, 'w') as f:
                    pass
                # Add the new file to git tracking
                git_add_command = f"git add {abs_path}"
                print(f"Running shell command: {git_add_command}")
                os.system(git_add_command)
                # Add the new file to the filenames in Coder
                coder.add_rel_fname(filename)
                # Update the repo map with the new file
                new_msg = f"Recreate the response for skipped files now that they are created and available for edits. Here is your previous response: \n {response}"
                coder.run(new_msg)
    if i > 5:
        break

# # This will execute one instruction on those files and then return
# coder.run("make a script that prints hello world")

# # Send another instruction
# coder.run("make it say goodbye")

# # You can run in-chat "/" commands too
# coder.run("/tokens")