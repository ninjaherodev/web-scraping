from bs4 import BeautifulSoup
import requests
import pandas as pd
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

response = requests.get(url, headers=headers)
response.encoding = 'utf8'
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # table = soup.find(id='constituents')
    # table = soup.find('table', class_='wikitable sortable')
    # table = soup.find(id="")
    table = soup.find("table", {"class": "wikitable sortable", "id": "constituents"})
    # Obtener los encabezados de la tabla
    headers = [header.text.strip() for header in table.find_all("th")]
    rows = table.find_all('tr')[1:4]
    print(headers)
    rowss = []
    for row in rows:
        cells = row.find_all("td")
        row_data = [cell.text.strip() for cell in cells]
        rowss.append(row_data)
        print('row_data:',row_data)
        for cell in cells:
            print(cell.text.strip())  # .strip() para eliminar espacios en blanco alrededor del texto
        print("---")
    df = pd.DataFrame(rowss, columns=headers)
    df.to_csv('tablaejemplo.csv',index=False)
    print('rows:', df)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")