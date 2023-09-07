import json

import click

from template_sync.gh_utils import get_respositories_to_sync
from template_sync.log import setup_logging


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "-t",
    "--github-token",
    help="GitHub personal token. If not provided, will look for GITHUB_TOKEN env var.",
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="Enable verbose logging",
)
@click.option(
    "-oj",
    "--output-json",
    help="Output file for JSON",
    required=False,
)
def get(github_token: str, verbose: bool, output_json: str):
    """Get all of the repositories to sync for user"""
    setup_logging(verbose)

    repos = list(get_respositories_to_sync())
    # dump templates to json file
    if output_json:
        with open(output_json, "w") as f:
            json.dump(repos, f, indent=4)


def main():
    cli()


if __name__ == "__main__":
    main()
