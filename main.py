import click
from generate_brewery_shop_ai import generate_code

@click.group()
def cli():
    """/dev/sales CLI Tool"""
    pass

@cli.command()
@click.option('--code', type=str, help="Path to the code location.")
@click.option('--usecase_prompt', type=str, help="Description of the use case.")
def generate(code, usecase_prompt):
    """Generate code based on the provided options."""
    if not code or not usecase_prompt:
        click.echo("Error: Both --code and --usecase_prompt are required when --generate is specified.")
        return

    click.echo(f"Generating code at path: {code}")
    click.echo(f"Use case prompt: {usecase_prompt}")
    # Add your code generation logic here
    generate_code()

if __name__ == "__main__":
    cli()

