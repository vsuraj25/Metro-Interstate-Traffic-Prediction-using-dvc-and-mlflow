from pymongo import MongoClient
import pandas as pd

connection_str = "mongodb+srv://vsuraj25:wulUIUgOO2j0llyg@cluster0.nbfiihk.mongodb.net/?retryWrites=true&w=majority"
database = 'Meteo_Interstate_Traffic_Data'
table = 'traffic_records'
initial_data_path = ".//data_given//Metro_Interstate_Traffic_Volume.csv"
upload_data_path = ".//data//raw//traffic_data.csv"

def upload_data(connection_str, database, table, initial_data_path, upload_data_path):
    client = MongoClient(connection_str)

    # Creating a Database with specified name
    db =  client.get_database(database)

    if table in db.list_collection_names():
        records = db.get_collection(table)
        all_records = records.find()
        # Converting Curser object into list
        cursor_list = list(all_records)

        data = pd.DataFrame(cursor_list).drop('_id', axis=1)

        data.to_csv(upload_data_path)

    else:
        records = db.traffic_records

        df = pd.read_csv(initial_data_path)

        # Converting the dataframe into sictionary as MongoDB stores values as records/dictionary
        df = df.to_dict(orient='records')

        # Inserting the records into our mongoDB Database in collection 'fire_records'
        records.insert_many(df)


        all_records = records.find()

        # Converting Curser object into list
        cursor_list = list(all_records)

        data = pd.DataFrame(cursor_list).drop('_id', axis=1)

        data.to_csv(upload_data_path)

upload_data(connection_str=connection_str,database=database,table=table,initial_data_path=initial_data_path,upload_data_path=upload_data_path)