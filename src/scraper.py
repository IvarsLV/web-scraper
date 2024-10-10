import os
import requests
from bs4 import BeautifulSoup

URL = 'https://python.org'  # Замените на нужный URL

def scrape_site(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Найти все заголовки <h2>
        headings = [h2.text.strip() for h2 in soup.find_all('h2')]
        return headings
    else:
        print(f'Ошибка при получении страницы. Код статуса: {response.status_code}')
        return []

if __name__ == '__main__':
    data = scrape_site(URL)
    print('Найденные заголовки:', data)
    
    # Получаем абсолютный путь к папке data
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, '..', 'data')

    # Проверяем, существует ли папка data, если нет - создаём её
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Сохраняем заголовки в файл headings.txt
    file_path = os.path.join(data_dir, 'headings.txt')
    with open(file_path, 'w') as file:
        for item in data:
            file.write(f'{item}\n')
