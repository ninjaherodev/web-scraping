import requests
from lxml import html
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = 'https://www.eltiempo.es/salamanca.html?v=por_hora'

response = requests.get(url, headers=headers)
response.encoding = 'utf8'
if response.status_code == 200:
    tree = html.fromstring(response.content)
    
    # Extraer encabezados
    headers = tree.xpath('//*[@id="main"]/div[4]/div/main/section[4]/section/article/div[1]/div/table/thead/tr/*')
    headersFormat = headers[:-1]  # Excluir el último encabezado
   

    # Extraer datos del cuerpo de la tabla
    datos = tree.xpath("//section[contains(@class, 'block_full') and contains(@class, 'row_number_4')]//table/tbody/tr[contains(@class, 'tab-pane')]")
    
    extracted_data = []
    for data in datos:
        cells = data.xpath("td")
        row_data = []
        for i, cell in enumerate(cells[:-1]):
            cell_text = cell.xpath(".//text()")
            cell_text = ''.join(cell_text).strip()
            if i == 1:  # Segunda columna
                cell_text = cell_text[:-1]
            elif i in [2, 3]:  # Tercera y cuarta columnas
                cell_text = cell_text.split("\n")[0]
            row_data.append(cell_text)
        extracted_data.append(row_data)
        print(row_data)
    
    # df = pd.DataFrame(extracted_data, columns=headersFormat)
    # df.to_csv('tiempo.csv', index=False)
    # print(df)
  
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")