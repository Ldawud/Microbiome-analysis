import pandas as pd 
from qiime2 import Artifact
import matplotlib.pyplot as plt 
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i","--input", help="The filepath to the vector you want turned into a histogram")
parser.add_argument("-o","--output", help="The name of your output histogram")

args = parser.parse_args()

data = Artifact.load(args.input).view(pd.Series)

data.hist()

plt.savefig(args.output)