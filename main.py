# 10.02.2021 @algiers
# https://github.com/vdElyn/png-table-from-sheets

import pandas as pd
import subprocess, gspread, configparser

# Parsing entries
config = configparser.ConfigParser()
config.read('config.ini')

sheets_api_credential_json_path = config['SheetsAPI']['sheets_api_credential_json_path']
sheets_file_name = config['SheetsAPI']['sheets_file_name']
sheet_name = config['SheetsAPI']['sheet_name'] if len(config['SheetsAPI']['sheet_name']) > 1 else None

limit = int(config['Table']['Limit']) if len(config['Table']['Limit']) > 1 else None
key_indexes = config['Table']['key_indexes']
if len(sheets_api_credential_json_path) == 0 or len(sheets_file_name) == 0 or len(key_indexes) == 0: 
  print('Only `sheet_name` and `limit` args can be null.')
  exit()

# Connect to Sheets API & open file 
gc = gspread.service_account(filename=sheets_api_credential_json_path)
sh = gc.open(sheets_file_name)

# Get records from Sheet
sheets_row = sh.sheet1.get_all_records() if sheet_name is None else sh.worksheet(sheet_name).get_all_records()
sheets_row = sheets_row[:limit]

# Get indexes (line)
index = []
for row in sheets_row:
  index.append(row[key_indexes])

# Get columns header - wanted format:
# columns = ['FIELD1', 'FIELD2']
columns = []
for col in sheets_row[0]:
  if col == key_indexes: continue # On ajoute pas la colonne définie comme Index (lignes)
  columns.append(col)

# Setup data columns - wanted format:
# data = {
#   'FIELD1': [value1, value2],
#   'FIELD2': [value1, value2]      
# }
data = {}
for col in columns:
  data[col] = []

# Formatting data dict
for col in data:
  for row in sheets_row:
    data[col].append(row[col])

df = pd.DataFrame(data, columns = columns, index = index)
print(df)

pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>

html_string = '''
<html>
  <meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
  <head><title>HTML Pandas Dataframe with CSS</title></head>
  <link rel="stylesheet" type="text/css" href="df_style.css"/>
  <body>
    {table}
  </body>
</html>.
'''

# Génère un fichier HTML de la `pandas.DataFrame` avec le header CSS
with open('df_tmp.html', 'w') as f:
    f.write(html_string.format(table=df.to_html(classes='mystyle')))

# Convertit le fichier HTML généré en PNG > table.png
subprocess.call("wkhtmltoimage -f png --encoding utf-8 df_tmp.html table.png", shell=True)
