# Module imports
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Creation Info
from lib.bess import bess

author_init = "ECM"

# Path generation, it is done this way to avoid
path = os.getcwd()
path_lib = os.path.join(path, 'lib')
path_in = os.path.join(path, 'input')
path_out = os.path.join(path, 'output')
filenames = os.listdir(path_in)


bess_unit = bess(0.950814, 4, 5000, [450, 400, 430, 350, 0.95, 0.4])
