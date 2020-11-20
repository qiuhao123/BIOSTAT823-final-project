import pandas as pd
from resources.config import PostgresConfigs
from sqlalchemy import create_engine

connection_string = f'''postgresql://{PostgresConfigs.USERNAME}:{PostgresConfigs.PASSWORD}@{PostgresConfigs.SERVER}:{PostgresConfigs.PORT}/{PostgresConfigs.DATABASE}'''

engine = create_engine(connection_string)

def query_database(query):
    return pd.read_sql_query(query, engine)
    
