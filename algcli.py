from email.policy import default
import os
import click
import subprocess

@click.group()
def cli():
    pass

@cli.command()
@click.option("-d/-p", default= False)
def run(d):
    os.environ["FLASK_APP"] = "app"
    if d:
        os.environ["FLASK_ENV"] = "development"
    else:
        os.environ["FLASK_ENV"] = "production"
    subprocess.run(os.path.dirname(__file__) + "/CLI/algrun.sh")
    
@cli.command()
def backtest():
    import backtraderTest
    backtraderTest.run()
    