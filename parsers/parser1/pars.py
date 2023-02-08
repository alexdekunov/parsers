import asyncio

import aiohttp
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent

BASE_URL = "https://arbuz.kz/ru/collections/248748-chai_kofe_sladosti#/"
HEADERS = {"User-Agent": UserAgent().random}


'''созадём асинхронную функцию'''
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, "html.parser")

            items = soup.find_all("article", {"class": "product-item product-card"})
            for item in items:
                title = item.find("a", {"class": "product-card__title"})  #.text.strip()
                link = title.get("href")
                price = item.find("b").text.strip()

                print(f"TITLE: {title.text.strip()} | PRICE: {price} | LINK: https://arbuz.kz/{link}")
                print("--------------")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

'''
Как ПАРСИТЬ сайты на PYTHON?

'''
