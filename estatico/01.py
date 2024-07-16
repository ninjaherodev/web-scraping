import requests
from lxml import html

url = 'https://www.wikipedia.org/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
# Realizar la solicitud HTTP
response = requests.get(url, headers=headers)
response.encoding = 'utf8'
if response.status_code == 200:
    page_content = response.content
    tree = html.fromstring(page_content)

    # ingles = tree.get_element_by_id('js-link-box-en')
    # print(ingles.text_content())
    
    languages = tree.xpath('//div[contains(@class, "central-featured-lang")]/a/strong/text()')
    for language in languages:
        print(language)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
