import requests
from bs4 import BeautifulSoup

url = "https://www.ethiobookreview.com/amharic"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

product_elements = soup.find_all('div', class_='product')

books = []
for element in product_elements:
    title_element = element.find('h5', class_='product-body')
    if title_element is not None:
        title = title_element.text.strip()
    else:
        title = "N/A"

    img_element = element.find('img')
    if img_element is not None:
        img_url = img_element['src']
    else:
        img_url = "N/A"

    category_element = element.find('h6')
    if category_element is not None:
        category = category_element.text.strip()
    else:
        category = "N/A"

    price_element = element.find('h5', style='color:red;')
    if price_element is not None:
        price = price_element.text.strip()
    else:
        price = "N/A"

    read_now_link_element = element.find('a')
    if read_now_link_element is not None:
        read_now_link = read_now_link_element['href']
    else:
        read_now_link = "N/A"

    books.append({'title': title, 'img_url': img_url, 'category': category, 'price': price, 'read_now_link': read_now_link})

# Print the scraped data
for book in books:
    print(f"Title: {book['title']}")
    print(f"Image URL: {book['img_url']}")
    print(f"Category: {book['category']}")
    print(f"Price: {book['price']}")
    print(f"Read Now Link: {book['read_now_link']}")
    print()