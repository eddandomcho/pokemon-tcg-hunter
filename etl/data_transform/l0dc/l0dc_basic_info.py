import pandas as pd

practice_df = pd.read_csv("files/practice_normalized.csv")

new_df = practice_df[["results_id"
                      , "results_card_info_name"
                      , "results_card_info_set_name"
                      , "results_card_info_set_code"
                      , "results_card_info_set_id"
                      , "results_card_info_rarity"
                      , "results_card_info_card_type"]]

new_df.rename(columns = {
    "results_id" : "id"
    , "results_card_info_name" : "name"
    , "results_card_info_set_name" : "set_name"
    , "results_card_info_set_code" : "set_code"
    , "results_card_info_set_id" : "set_id"
    , "results_card_info_rarity" : "rarity"
    , "results_card_info_card_type" : "card_type"
}, inplace = True)

new_df.to_csv("./files/l0dc/l0dc_basic_info.csv", index = False)

# .rename()