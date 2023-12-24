import pandas as pd
import re
df = pd.read_csv("workData.tsv", sep = "\t")
def trumpChecker(s):
    p = r'(?<![a-zA-Z0-9])' + re.escape("Trump") + r'(?![a-zA-Z0-9])'
    return bool(re.search(p,s))

df["trump_mention"] = df["content"].apply(trumpChecker)
final = df[["tweet_id","publish_date","content", "trump_mention"]]
final.to_csv("dataset.tsv", sep ="\t", index = False)

