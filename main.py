import discord
from discord.ext import commands, tasks
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
from typing import Final
from discord import Intents
import asyncio


load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')


intents: Intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


tracked_prices = {}


def fetch_price(url: str):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        
        price_tag = soup.find('tr', class_='priceTR').find('td', class_='bodyTD').find('span')
        header_tag = soup.find('h1', class_='headerText')

        price = price_tag.text.strip()
        header = header_tag.text.strip()

        return header, price

    except Exception as e:
        return None, f"Error fetching price: {e}"


@tasks.loop(minutes=5)
async def check_price_updates():
    for user_id, (url, last_price) in tracked_prices.items():
        header, price = fetch_price(url)

        if header and price != last_price:  
            user = bot.get_user(user_id)
            tracked_prices[user_id] = (url, price)  
            await user.send(f"The price of {header} has changed to {price}.")
            await user.send(f"Check it out here: {url}")


@bot.command(name='track_price')
async def track_price_command(ctx, *, url: str):
    header, price = fetch_price(url)

    if header:
       
        await ctx.send(f"Tracking product: {header}\nCurrent Price: {price}")
        tracked_prices[ctx.author.id] = (url, price)  
    else:
        await ctx.send(price)

@bot.event
async def on_ready():
    check_price_updates.start() 
    print(f'bot online logged in as {bot.user}')

def main() -> None:
    bot.run(TOKEN)
    
    

if __name__ == '__main__':
    main()
