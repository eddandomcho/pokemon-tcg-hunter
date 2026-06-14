import pandas as pd

df = pd.read_csv("files/normalized_files/perfect_order_normalized.csv")

new_df = df[["results_id"
                      , "results_card_info_name"
                      , "results_card_info_set_name"
                      , "results_card_info_set_code"
                      , "results_card_info_set_id"
                      , "results_card_info_rarity"
                      , "results_card_info_card_type"
                      , "results_card_info_card_number"]]

new_df.rename(columns = {
    "results_id" : "id"
    , "results_card_info_name" : "name"
    , "results_card_info_set_name" : "set_name"
    , "results_card_info_set_code" : "set_code"
    , "results_card_info_set_id" : "set_id"
    , "results_card_info_rarity" : "rarity"
    , "results_card_info_card_type" : "card_type"
    , "results_card_info_card_number" : "card_number"
}, inplace = True)

new_df.fillna({"card_type": "Trainer"}, inplace=True)

new_df.to_csv("files/l0dc/l0dc_perfect_order_normalized.csv", index = False)