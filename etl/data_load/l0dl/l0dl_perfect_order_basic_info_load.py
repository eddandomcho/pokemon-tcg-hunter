import pandas as pd
from sqlalchemy import create_engine

# Change this
df = pd.read_csv("files/l0dc/l0dc_perfect_order_normalized.csv")

username = "student"      # default user
password = ""              # the password you set during installation
host = "localhost"         # if running locally
port = "5432"              # default PostgreSQL port
database = "pokehunter"    # the database you created earlier

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

# Change this
table_name = "perfect_order_basic_info"
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"✅ Data successfully loaded into table '{table_name}' in database '{database}'.")