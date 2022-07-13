import sys
import pandas as pd
import numpy as np

filename = argv[1]
df = pd.read_excel(filename)
# df = pd.DataFrame({
#     "col1" : [1,2],
#     "col2" : [3,4]
# })

col3 = []
for index, row in df.iterrows():
    sum = 0
    sum += (row["col1"] + row["col2"])
    col3.append()
    sum = 0
# df = df.assign("col3",col3)
df["col3"] = col3

with pd.ExcelWriter("newSample.xlsx") as writer:
    df.to_excel(writer,sheet_name="TBD")