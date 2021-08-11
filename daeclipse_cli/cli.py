"""Main file for DeviantArt Eclipse CLI."""

import typer

import daeclipse_cli.commands as commands


app = typer.Typer(help='DeviantArt Eclipse CLI')

app.command()(commands.add_art_to_groups)
app.command()(commands.hot_tags)
app.command()(commands.post_status)
app.command()(commands.show_tags)
app.command()(commands.spammer)
app.command()(commands.user_comments)
