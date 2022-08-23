from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
      name = "algo-bot",
      version= "0.0.1",
      packages= find_packages(),
      url="https://github.com/Cratoinyan/algo-trade-bot",
      entry_points = '''
            [console_scripts]
            algo-bot=algcli:cli
      '''
      )