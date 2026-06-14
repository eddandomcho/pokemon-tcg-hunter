from models import compile as c
import pandas as pd

def normalize_card_info():

    practice_merged = c.merge_json_return("files/practice")["cards"]

    practice_merged_normalized = pd.json_normalize(practice_merged, sep = "_")

    file_path = "files/normalized_files/practice_normalized.csv"

    practice_merged_normalized.to_csv(file_path, index = False)

    print(practice_merged_normalized.head(5))

def normalize_price_info():
    practice_merged = c.merge_json_return_price("files/practice")["cards"]

    practice_merged_normalized = pd.json_normalize(practice_merged, sep = "_")

    file_path = "files/practice_normalized_price.csv"

    practice_merged_normalized.to_csv(file_path, index = False)

    print(practice_merged_normalized.head(5))


def normalize_card_info_custom(folder_path, custom_name):

    practice_merged = c.merge_json_return(f"files/{folder_path}")["cards"]

    practice_merged_normalized = pd.json_normalize(practice_merged, sep = "_")

    file_path = f"files/normalized_files/{custom_name}.csv"

    practice_merged_normalized.to_csv(file_path, index = False)

    print(practice_merged_normalized.head(2))

normalize_card_info_custom("ascended_heroes", "ascended_heroes_normalized")