#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

_, input_file, output_file = sys.argv

df = pd.read_csv(input_file, sep=';')
df["time"] = df["time"].astype("datetime64[ns]")
df["time"] = df["time"] - df["time"][0]
df["time"] = df["time"] / np.timedelta64(1, "s")
df["frequency"] = df["frequency"] / 1000
plt.plot("time", "frequency", data=df, marker='+')
plt.xlabel("Time (s)")
plt.ylabel("Frequency (MHz)")
plt.savefig(output_file, bbox_inches="tight")
