import requests
from lxml import  html

url = 'https://http.cat/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
# Realizar la solicitud HTTP
response = requests.get(url, headers=headers)
response.encoding = 'utf8'
if response.status_code == 200:
    page_content = response.content
    tree = html.fromstring(page_content)

    codes = tree.xpath('//ul[@class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 list-none p-0"]/li//div[contains(@class, "text-[2rem]")]/text()')
    descriptions = tree.xpath('//ul[@class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 list-none p-0"]/li//p/text()')
    
    for code, description in zip(codes, descriptions):
        print(f"{code.strip()} - {description.strip()}")
    
  
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")