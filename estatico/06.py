from lxml import html
import requests
import pandas as pd
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = 'https://www.eltiempo.es/salamanca.html?v=por_hora'

response = requests.get(url, headers=headers)
response.encoding = 'utf8'
if response.status_code == 200:
    page_content = response.content
    soup = html.fromstring(page_content)
    headers = soup.xpath('//*[@id="main"]/div[4]/div/main/section[4]/section/article/div[1]/div/table/thead/tr/*')
    headersFormat = [header.text for header in headers[:-1]]
    print(headersFormat)

    imagen = soup.xpath('//*[@id="main"]/div[4]/div/main/section[4]/section/article/div[1]/div/table/tbody/tr[1]/td[2]/p/img')
    print(imagen[0].attrib['src'])

    # datos = soup.xpath('//*[@id="main"]/div[4]/div/main/section[4]/section/article/div[1]/div/table/tbody/tr[1]')
    # print(datos.text)
    # for data in datos:
    #     print(data.text)
    # extracted_data = []
    # for data in datos:
    #     cells = data.find_all("td")
    #     row_data = []
    #     for i,cell in enumerate(cells[:-1]):
    #         cell_text = cell.text.strip()
    #         if i == 1:  
    #             cell_text = cell_text[:-1] 
    #         elif i in [2, 3]: 
    #             cell_text = cell_text.split("\n")[0]  
    #         row_data.append(cell_text)
    #     extracted_data.append(row_data)
    #     print(row_data)
    # df = pd.DataFrame(extracted_data, columns=headersFormat)
    # df.to_csv('tiempo.csv',index=False)
    # print(df)
    # print(datos[0].find_all("td")[0].find('p').text)
    # print(datos[0].find_all("td")[1].find('p').text.strip()[:-1])
    # print(datos[0].find_all("td")[2].find('p').text.strip().split("\n")[0])
    # print(datos[0].find_all("td")[3].find('p').text.strip().split("\n")[0])
    # print(datos[0].find_all("td")[4].find('p').text.strip().split(" ")[0])
    # print(datos[0].find_all("td")[5].find('p').text.strip().split(" ")[0])
    # print(datos[0].find_all("td")[6].find('p').text.strip().split(" ")[0])
    # print(datos[0].find_all("td")[7].find('p').text.strip().split(" ")[0])
  
   
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")