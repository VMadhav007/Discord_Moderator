#main.py
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

from helper import classify_toxicity

from collections import defaultdict
from datetime import timedelta

# Intents (you might need to enable specific intents from Discord Developer Portal)
intents = discord.Intents.default()
intents.members = True 
intents.messages = True
intents.message_content = True

# Define bot prefix and intents
bot = commands.Bot(command_prefix="!", intents=intents)
user_toxic_counts = defaultdict(int)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

# Example Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    output=classify_toxicity(message.content)
    filtered_output = {key: value for key, value in output.items() if value > 0.99 and key != "none"}

# Check if filtered_output is empty
    if filtered_output:
        await message.delete()
        user_toxic_counts[message.author.id] += 1
        await message.channel.send(f"{message.author.mention} - mind your language !")

        if user_toxic_counts[message.author.id] >= 3:
            try:
                timeout_duration = timedelta(minutes=1)  # Set timeout duration
                await message.author.timeout(timeout_duration, reason="Excessive use of toxic language")
                await message.channel.send(f"{message.author.mention} has been timed out for 5 minutes due to repeated toxic behavior.")
                user_toxic_counts[message.author.id] = 0
            except discord.Forbidden:
                await message.channel.send("I don't have permission to timeout this user.")
            except discord.HTTPException as e:
                await message.channel.send(f"Failed to timeout the user: {e}")
    await bot.process_commands(message)

    
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention} hi")

# Run the bot with your token
# Replace 'YOUR_BOT_TOKEN' with your bot's token from Discord Developer Portal
bot.run(os.getenv("DISCORD_ID"))