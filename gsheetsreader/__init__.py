from gsheets import Sheets
import pandas as pd
from matplotlib import pyplot as plt
import os
path=os.getcwd()
abspath1=os.path.join(path,"client_secrets.json") #edit your client_secret_json here with the the help of googleapis and entering into google developer console
abspath2=os.path.join(path,"storage.json.json")#edit this also same 
sheets = Sheets.from_files(abspath1,abspath2)
url="https://docs.google.com/spreadsheets/d/1SrZfvr2ee54r7HR1jGtAE9zHIj_Y-UzK9ok8bdwkpqc/edit#gid=0"#url for your current spreadsheets that you want to work with
s=sheets.get(url)
sheet_no=int(input())#sheet no you want to get ex:0,1in this case i have used 0 because i have one sheet only present
s.sheets[sheet_no].to_csv('Spam.csv', encoding='utf-8', dialect='excel')#converting that sheets into csv file for local manipulation
df=pd.read_csv('Spam.csv')
ax = plt.gca()

df.plot(kind='line',x='timestamp',y='average_sales',ax=ax)
plt.savefig('output.png')





