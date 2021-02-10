import pandas as pd
import subprocess

sheets_row = [
        {'DATE': '2021-02-09 20:18', 'TYPE': 'Mémorisation', 'PAGE': 569.2, 'DÉTAILS': 'al-Ma‘aridj V11 - V31', 'POUR DEMAIN': 'al-Ma‘aridj V19 - V39', 'MÉMORISATION': 'S71 V2-V7 (6L)'}, 
        {'DATE': '2021-02-08 20:44', 'TYPE': 'Mémorisation', 'PAGE': 569.1, 'DÉTAILS': 'al-Maaridj V1 - V21', 'POUR DEMAIN': 'al-Maaridj V11 - V31', 'MÉMORISATION': 'S70 V40-V44 + S71 V1'}, 
        {'DATE': '2021-02-07', 'TYPE': 'Off', 'PAGE': '', 'DÉTAILS': '', 'POUR DEMAIN': 'Révision reportée à la semaine pro.', 'MÉMORISATION': 'S70 V31 - V39 (5 Lignes)'}, 
        {'DATE': '2021-02-06', 'TYPE': 'Off', 'PAGE': '', 'DÉTAILS': '', 'POUR DEMAIN': '', 'MÉMORISATION': 'S70 V22 - V30 (5 Lignes)'}, 
        {'DATE': '2021-02-05', 'TYPE': 'Mémorisation', 'PAGE': 568.3, 'DÉTAILS': 'al-Haqqah V44 - al-Ma‘aridj V10', 'POUR DEMAIN': 'Révision Dimanche', 'MÉMORISATION': 'S70 V11 - V21 (5 Lignes)'}, 
        {'DATE': '2021-02-04', 'TYPE': 'Mémorisation', 'PAGE': 568.2, 'DÉTAILS': 'al-Haqqah V35-V52', 'POUR DEMAIN': '', 'MÉMORISATION': "al-Ma'aridj V1 - V10 (5 Lignes)"}
    ]

data = {'Type': [], 'Page': [], 'Détails': [], 'Demain': [], 'Mémorisation': []}
dates = []
for j in sheets_row:
    dates.append(j['DATE'])
    data['Type'].append(j['TYPE'])
    data['Page'].append(j['PAGE'])
    data['Détails'].append(j['DÉTAILS'])
    data['Demain'].append(j['POUR DEMAIN'])
    data['Mémorisation'].append(j['MÉMORISATION'])

df = pd.DataFrame(data, columns = ['Type', 'Page', 'Détails', 'Demain', 'Mémorisation'], index=dates)
print (df)

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

# OUTPUT AN HTML FILE
with open('myhtml.html', 'w') as f:
    f.write(html_string.format(table=df.to_html(classes='mystyle')))

subprocess.call(
    "wkhtmltoimage -f png --encoding utf-8 myhtml.html table2.png", shell=True)
