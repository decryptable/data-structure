import click
from app.menu import run_menu


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
def main() -> None:
    run_menu()


if __name__ == "__main__":
    main()
