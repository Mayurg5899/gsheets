from gsheets import Sheets
import pandas as pd
from matplotlib import pyplot as plt
import os
path=os.getcwd()
abspath1=os.path.join(path,"client_secrets.json") #edit your client_secret_json here with the the help of googleapis and entering into google developer console
abspath2=os.path.join(path,"storage.json.json")#edit this also same 
sheets = Sheets.from_files(abspath1,abspath2)
url="https://docs.google.com/spreadsheets/d/1SrZfvr2ee54r7HR1jGtAE9zHIj_Y-UzK9ok8bdwkpqc/edit#gid=0"
s=sheets.get(url)
s.sheets[0].to_csv('Spam.csv', encoding='utf-8', dialect='excel')
df=pd.read_csv('Spam.csv')
ax = plt.gca()

df.plot(kind='line',x='timestamp',y='average_sales',ax=ax)
plt.savefig('output.png')





