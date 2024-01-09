import pandas as pd
fileName = "raw.csv"
df = pd.read_csv(fileName)
filtered = df.head(10000)
ff = filtered[(filtered["language"] ==  "English") & (~filtered["content"].str.contains("\?", regex=True))]
ff.to_csv("workData.tsv", sep = "\t", index = False)
