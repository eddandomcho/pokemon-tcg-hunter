import json
from models import compile as c
import pandas as pd
from models import save_card_json as scj

def normalize_card_info():

    practice_merged = c.merge_json_return("files/practice")["cards"]

    practice_merged_normalized = pd.json_normalize(practice_merged, sep = "_")

    file_path = "files/practice_normalized.csv"

    practice_merged_normalized.to_csv(file_path, index = False)

    print(practice_merged_normalized.head(5))

def normalize_price_info():
    practice_merged = c.merge_json_return_price("files/practice")["cards"]

    practice_merged_normalized = pd.json_normalize(practice_merged, sep = "_")

    file_path = "files/practice_normalized_price.csv"

    practice_merged_normalized.to_csv(file_path, index = False)

    print(practice_merged_normalized.head(5))

scj.print_card_json("23821 39")