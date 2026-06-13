import pandas as pd

df = pd.read_csv("files/practice_normalized_price.csv")

new_df = df[[ "card_info_name"
            , "card_info_clean_name"
            , "card_info_set_name"
            , "card_info_set_code"
            , "card_info_set_id"
            , "card_info_card_number"
            , "tcgplayer_url"
            , "cardmarket_url"
            , "tcgplayer_prices_low_price"
            , "tcgplayer_prices_mid_price"
            , "tcgplayer_prices_high_price"
            , "tcgplayer_prices_updated_at"
            , "tcgplayer_prices_direct_low_price"
            , "tcgplayer_prices_sub_type_name"
             
            ]]

new_df.rename(columns = {
    "card_info_name" : "card_name"
    , "card_info_clean_name" : "card_clean_name"
    , "card_info_set_name" : "card_set_name"
    , "card_info_set_code" : "card_set_code"
    , "card_info_set_id" : "card_set_id"
    , "card_info_card_number" : "card_number"
    , "tcgplayer_prices_low_price" : "low_price"
    , "tcgplayer_prices_mid_price" : "mid_price"
    , "tcgplayer_prices_high_price" : "high_price"
    , "tcgplayer_prices_updated_at" : "updated_at"
    , "tcgplayer_prices_direct_low_price" : "direct_low_price"
    , "tcgplayer_prices_sub_type_name" : "sub_type_name"
}, inplace = True)

new_df.to_csv("l0dc_tcgplayer_price_info.csv", index = False)