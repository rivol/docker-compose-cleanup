""" Console script for docker-compose-cleanup.

ATM the script doesn't support any parameters, so using Click is somewhat superfluous. For now.
"""

import click


@click.command()
def main():
    from .docker_compose_cleanup import clean
    clean()

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
