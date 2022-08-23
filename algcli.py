import os
import click
import subprocess

@click.group()
def cli():
    pass

@cli.command()
def run():
    os.environ["FLASK_APP"] = "app"
    os.environ["FLASK_ENV"] = "development"
    subprocess.run("./CLI/algrun.sh")
    