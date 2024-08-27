import click
from generate_brewery_shop_ai import generate_code

@click.group()
def cli():
    """/dev/sell CLI Tool"""
    pass

@cli.command()
@click.option('--branch_name', type=str, required=True, help="Branch name for the project.")
@click.option('--project_name', type=str, required=True, help="Project name.")
@click.option('--requirements_file', type=str, required=True, help="Path to the requirements markdown file.")
def generate(branch_name, project_name, requirements_file):
    """Generate code based on the provided options."""
    # Add your code generation logic here
    generate_code(branch_name=branch_name, project_name=project_name, requirements_file=requirements_file)

if __name__ == "__main__":
    cli()
