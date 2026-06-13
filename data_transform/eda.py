import pandas as pd

df = pd.read_csv("files/practice_기초정보.csv")

print(df.groupby(by = "card_type").size())