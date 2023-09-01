import click
from template.example_lib import hello_world


@click.command()
@click.option("-n", "--name", prompt="Your name", help="The person to greet.")
def hello(name: str):
    """Simple program that greets given NAME."""
    click.echo(hello_world(name))


if __name__ == "__main__":
    hello()
