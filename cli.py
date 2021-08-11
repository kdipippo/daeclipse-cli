"""Main file for DeviantArt Eclipse CLI."""

import typer

import daeclipse_cli

app = typer.Typer(help='DeviantArt Eclipse CLI')

app.command()(daeclipse_cli.add_art_to_groups)
app.command()(daeclipse_cli.hot_tags)
app.command()(daeclipse_cli.post_status)
app.command()(daeclipse_cli.show_tags)
app.command()(daeclipse_cli.spammer)
app.command()(daeclipse_cli.user_comments)


if __name__ == '__main__':
    app()
