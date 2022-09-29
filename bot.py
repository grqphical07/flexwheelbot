import discord
from discord.ext.commands import *
import os
from dotenv import load_dotenv
import scraper
import threading
import time

async def check_flexwheels(client:Bot):
    await client.wait_until_ready()
    last_result = None
    channel_id = 1024898745323753525
    while True:
        channel = client.get_channel(channel_id)
        result = scraper.check_flexwheels(SKU)
        if result != last_result:
            if result == 1:
                await channel.send("Sorry, there are no flexwheels in stock :(")
            elif result == 0:
                await channel.send("We got flex wheels :)")
        last_result = result
        time.sleep(30)

load_dotenv()

KEY = os.getenv("TOKEN")
SKU = "217-6353"

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = Bot(intents=intents, command_prefix="$")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.loop.create_task(check_flexwheels(client))

@client.command()
async def flexwheels(ctx, arg=""):
    result = scraper.check_flexwheels(SKU)
    if result == 1:
        await ctx.send("Sorry, there are no flexwheels in stock :(")
    elif result == 0:
        await ctx.send("We got flex wheels :)")



client.run(KEY)