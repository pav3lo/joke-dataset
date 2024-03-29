# INPUT: .csv with "Question", "Answer", and "meta" fields.
# OUTPUT: .csv with only the rows with the specified "meta" tags.

import pandas as pd
import sys
from jokeutils import *

infile = parse_args()
DELETE_AFTER_MOVING = False
df = pd.read_csv(infile)

cols = (["Question", "Answer", "meta"])
newdf = pd.DataFrame(columns=cols)

tag = "type:tradlightbulb"

outfile = outfile_name(tag)


insertion_row = 1
for idx, tags in enumerate(df["meta"]):
    if tag in tags:
        newdf.loc[insertion_row] = df.loc[idx]
        if DELETE_AFTER_MOVING:
            df = df.drop(idx)
        insertion_row += 1

    if (idx % 5000 == 0):
        print(idx)

df.to_csv(infile, encoding='utf-8', index=False)
newdf.to_csv(outfile, encoding='utf-8', index=False)
