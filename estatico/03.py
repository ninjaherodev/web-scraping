from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = 'https://stackoverflow.com/questions/'

response = requests.get(url, headers=headers)
response.encoding = 'utf8'
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
     # soup = BeautifulSoup(response.text)
     # Extraer las preguntas
    questions = soup.find_all('div', class_='s-post-summary')
    for question in questions:
        # Título de la pregunta
        title_tag = question.find('h3', class_='s-post-summary--content-title')
        title = title_tag.find('a').get_text(strip=True)
        # title = title_tag.get_text(strip=True) if title_tag else 'N/A'
        
        # Enlace de la pregunta
        link_tag = title_tag.find('a') if title_tag else None
        link = f"https://stackoverflow.com{link_tag['href']}" if link_tag else 'N/A'
        
        # Resumen de la pregunta
        excerpt_tag = question.find('div', class_='s-post-summary--content-excerpt')
        excerpt = excerpt_tag.get_text(strip=True) if excerpt_tag else 'N/A'
        
        print(f"Título: {title}")
        # print(f"Enlace: {link}")
        # print(f"Resumen: {excerpt}")
        print('-' * 80)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")