# sample code to get total of each row 
import sys
import pandas as pd
import numpy as np

filename = sys.argv[1]
df = pd.read_excel(filename)

col3 = []
for index, row in df.iterrows():
    sum = 0
    sum += (row["col1"] + row["col2"])
    col3.append(sum)
    sum = 0
# df = df.assign("col3",col3)
df["total"] = col3

with pd.ExcelWriter("newSheet.xlsx") as writer:
    df.to_excel(writer,sheet_name="TBD")