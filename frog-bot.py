import discord
from discord.ext import commands
import random
import requests
import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix='!')

@bot.command()
async def frogtime(ctx):
    random_string = str(random.randint(0, 5)) + str(random.randint(1, 4))  # add random number 01-54 for frog choice
    if not os.path.exists('frogs/' + random_string):
        print(f'generating new frog image #{random_string}')
        url = 'http://www.allaboutfrogs.org/funstuff/random/00'
        url += random_string + '.jpg'
        response = requests.get(url)
        with open('frogs/' + random_string + '.jpg', 'wb') as file:
            file.write(response.content)

    await ctx.send(file=discord.File('frogs/' + random_string + '.jpg'))

token = os.getenv('BOT_TOKEN')

bot.run(token)
