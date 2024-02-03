import requests
from bs4 import BeautifulSoup
from telegram import ForceReply, Update, InputMediaPhoto
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


BOT_TOKEN = '6675490107:AAGqekKFOOVj-qQcuJXfmH_5NVuoxxrUgCw'



async def scrape_data():
   
    url = 'https://www.ethiobookreview.com/amharic'
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup( html,'html.parser')
    product_elements = soup.find('div', class_='product')
    element = product_elements.find_all('article', class_='product')

    books = []
    for element in element:
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
    return books
  


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! use /books to get the Amharic Books",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("use /books to get recent books ")


async def get_books(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    recent_books = await scrape_data()
    
    for element in element:
        title = element['Title']
        image = element['Image']
        catagort = element['Catagory']
        passrice = element['Price']
        read_now_list = element['Read_Now_List']

        
    for book in book[:5]:
        message += f"Title: {book['title']}\n"
        message += f"Image URL: {book['img_url']}\n"
        message += f"Category: {book['category']}\n"
        message += f"Price: {book['price']}\n"
        message += f"Read Now Link: {book['read_now_link']}\n\n"

def main() -> None:
    
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    application.add_handler(CommandHandler("books", get_books))

 
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()