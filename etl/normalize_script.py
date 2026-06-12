import json
import models.compile as c
import pandas as pd

practice_merged = c.merge_json_return("files/practice")["cards"]

practice_merged_normalized = pd.json_normalize(practice_merged, sep = "_")

file_path = "files/practice_normalized.csv"

practice_merged_normalized.to_csv(file_path, index = False)

print(practice_merged_normalized.head(5))