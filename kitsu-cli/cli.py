import click
import gazu
import questionary

gazu.set_host("http://localhost/api")
user = gazu.log_in("admin@example.com", "mysecretpassword")


@click.group()
def cli():
    """My Studio Kitsu Tool"""
    pass


@cli.group()
def production():
    """Commands for managing productions"""
    pass


@production.command()
@click.option("--name", help="Filter by production name")
def list(name):
    """List available productions"""
    productions = gazu.project.all_projects()

    for production in productions:
        click.echo(f"{production['name']}")


@production.command()
def select():
    """List available productions"""
    productions = gazu.project.all_projects()

    selected_project = questionary.select(
        "Which project are you working on?", choices=productions
    ).ask()

    click.echo(f"You selected {selected_project}. Loading assets...")


if __name__ == "__main__":
    cli()
