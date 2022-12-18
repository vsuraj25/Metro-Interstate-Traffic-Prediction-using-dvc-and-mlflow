from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb+srv://vsuraj25:wulUIUgOO2j0llyg@cluster0.nbfiihk.mongodb.net/?retryWrites=true&w=majority")

# Creating a Database with specified name
db =  client.get_database('Meteo_Interstate_Traffic_Data')

records = db.traffic_records

df = pd.read_csv('.//Metro_Interstate_Traffic_Volume.csv')

# Converting the dataframe into sictionary as MongoDB stores values as records/dictionary
df = df.to_dict(orient='records')

# Inserting the records into our mongoDB Database in collection 'fire_records'
db.traffic_records.insert_many(df)


all_records = records.find()

# Converting Curser object into list
cursor_list = list(all_records)

data = pd.DataFrame(cursor_list).drop('_id', axis=1)

data.to_csv()