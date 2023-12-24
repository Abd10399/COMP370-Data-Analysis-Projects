import pandas as pd
df = pd.read_csv("dataset.tsv", sep="\t")
value_ctr = df["trump_mention"].value_counts()
tr = value_ctr[True]
fl = value_ctr[False]

t1 = {"result" : ["frac-trump-mentions"],"value" : [round((tr/(tr+fl)),3)]}

final = pd.DataFrame(t1)
final.to_csv("results.tsv", sep="\t", index=False)
