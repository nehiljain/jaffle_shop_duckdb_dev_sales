import click
from generate_brewery_shop_ai import generate_code, swap_cleaned_csvs, check_success_dbt_build  # Import the new function

@click.group()
def cli():
    """/demodrive CLI Tool"""  # Updated project name
    pass

@cli.command()
@click.option('--branch_name', type=str, required=True, help="Branch name for the project.")
@click.option('--project_name', type=str, required=True, help="Project name.")
@click.option('--requirements_file', type=str, required=True, help="Path to the requirements markdown file.")
@click.option('--io_flag', is_flag=True, default=True, help="Flag to enable interactive mode.")
def generate(branch_name, project_name, requirements_file, io_flag):
    """Generate code based on the provided options."""
    generate_code(branch_name=branch_name, project_name=project_name, requirements_file=requirements_file, io_flag=io_flag)

@cli.command()
@click.option('--branch_name', type=str, required=True, help="Branch name for the project.")
@click.option('--project_name', type=str, required=True, help="Project name.")
@click.option('--requirements_file', type=str, required=True, help="Path to the requirements markdown file.")
@click.option('--io_flag', is_flag=True, default=False, help="Flag to enable interactive mode.")
def swap_csv(branch_name, project_name, requirements_file, io_flag):
    """Swap cleaned CSV files based on the provided options."""
    swap_cleaned_csvs(branch_name=branch_name, project_name=project_name, requirements_file=requirements_file, io_flag=io_flag)

@cli.command()
@click.option('--branch_name', type=str, required=True, help="Branch name for the project.")
@click.option('--project_name', type=str, required=True, help="Project name.")
@click.option('--requirements_file', type=str, required=True, help="Path to the requirements markdown file.")
@click.option('--io_flag', is_flag=True, default=True, help="Flag to enable interactive mode.")
def fix_dbt_build(branch_name, project_name, requirements_file, io_flag):
    """Check and run dbt build based on the provided options."""
    check_success_dbt_build(branch_name=branch_name, project_name=project_name, requirements_file=requirements_file, io_flag=io_flag)

if __name__ == "__main__":
    cli()
