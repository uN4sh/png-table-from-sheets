# HTML & PNG Tables from GSheets

Generates an HTML and PNG stylized table from a Google Sheets. Requires GSheet API — or formatted-like data.
> 10.02.2021 @ Algiers — @vdElyn

- Get your Sheets API Credential JSON file [from here](https://gspread.readthedocs.io/en/latest/)
- Complete `config.ini` file
- Run the python `main.py` file
- Edit `df_style.css` to edit your table displaying

### Required modules
- `pandas` to create DataFrame 
- `gspread` to interact with GSheets API 
- `subprocess` to call external program
- `configparser` to parse .ini files
- `wkhtmltopdf` to convert DataFrame HTML result to PNG 

```python
$ pip install pandas gspread configparser
$ apt-get install wkhtmltopdf
```

### Results

Starting from this kind of tables from Google Sheets:


| Key index  | Field 1 | Field 2 |
| ------------- | ------------- | ------------- |
| Index  | Value 1  | Value 2 |
| Index  | Value 1  | Value 2 |

Generates:
