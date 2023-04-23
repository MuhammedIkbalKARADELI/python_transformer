import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

df = pd.read_csv("Artifact.csv",header=None)


plt.plot(df)
plt.show()