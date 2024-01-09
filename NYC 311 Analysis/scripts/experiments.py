# %%
import pandas as pd

# %%
df = pd.DataFrame(
    [
        ["bird", "falcon", 123],
        ["bird", "sparrow", 20],
        ["feline", "cat", 15],
        ["bird", "sparrow", 25],
    ],
    columns=["animal", "name", "speed"],
)

# %%
df.groupby(["animal", "name"]).size().reset_index(name="counts")

# %%

