import json
import os
import sqlalchemy
import pandas as pd
from utils import rename_columns

mapping_df = pd.read_csv("mapping/JSON_TABLE_Mapping.csv", encoding="utf-8")

# connection_string = '{connector}://{user}:{password}@{server}:{port}/nikshay'.format(
#     connector=os.environ['PG_CONNECTOR'],
#     user=os.environ['PG_USER'], password=os.environ['PG_PASSWORD'],
#     server=os.environ['PG_HOST'], port=os.environ['PG_PORT'])
connection_string1 = 'postgresql://postgres:postgres@localhost:5432'
engine = sqlalchemy.create_engine(connection_string1)
db_con = engine.connect()


def enroll_patient(handler):
    data = json.loads(handler.request.body)
    # print(data["fields"])
    data_df = pd.DataFrame([data["fields"]])
    try:
        data_df = rename_columns(data_df, mapping_df)
        data_df.to_sql("patient", db_con, if_exists='append', index=False)
        return "PASS"
    except:
        return "Columns not present "+ str(data_df)
        # return pass
