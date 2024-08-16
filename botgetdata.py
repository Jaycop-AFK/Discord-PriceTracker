import requests
from bs4 import BeautifulSoup
import time

url = "http://www.xpcharter.com/product/30824/%E0%B8%A3%E0%B8%AB%E0%B8%B1%E0%B8%AA%E0%B8%AA%E0%B8%B4%E0%B8%99%E0%B8%84%E0%B9%89%E0%B8%B2-%E0%B8%A313280%E0%B8%81%E0%B8%B5%E0%B8%95%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B9%82%E0%B8%9B%E0%B8%A3%E0%B9%88%E0%B8%87%E0%B9%84%E0%B8%9F%E0%B8%9F%E0%B9%89%E0%B8%B2-model-s-%E0%B8%82%E0%B8%B2%E0%B8%A2%E0%B8%95%E0%B8%B2%E0%B8%A1%E0%B8%AA%E0%B8%A0%E0%B8%B2%E0%B8%9E-%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B8%A1%E0%B8%B5%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%99"

def fetch_price():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the price using the appropriate class
    price_tag = soup.find('tr', class_='priceTR').find('td', class_='bodyTD').find('span')

    # class="headerText" show print
    header_tag = soup.find('h1', class_='headerText')

    price = price_tag.text.strip()
    header = header_tag.text.strip()

    return price, header

def main():
    while True:
        try:
            price,header = fetch_price()
            print(f"Name: {header} Price: {price}")
        except Exception as e:
            print(f"Error fetching price: {e}")

        # Wait for 1 second before fetching the price again
        time.sleep(1)

if __name__ == "__main__":
    main()
