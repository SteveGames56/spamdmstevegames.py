import discord  
import asyncio   
from discord.ext import commands
import json
import aiohttp

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)


tokens = [
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_FIRST_BOT_TOKEN",
    "YOUR_SECOND_BOT_TOKEN",
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
    "YOUR_THIRD_BOT_TOKEN"
]

async def send(userid, token):
    payload = {
        "content": f""
    }
    url_create_dm = 'https://discord.com/api/v9/users/@me/channels'
    data = {
        "recipients": [f"{userid}"]
    }

    headers = {
        "authorization": f"Bot {token}"
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url_create_dm, json=data, headers=headers) as response:
                response_json = await response.json()
                for _ in range(3):  
                    url = f'https://discord.com/api/v9/channels/{response_json["id"]}/messages'
                    async with session.post(url, json=payload, headers=headers) as r:
                        pass
    except Exception as e:
        print(f'[ - ] Error: {e}')


@client.command()
@commands.cooldown(1, 120, commands.BucketType.user)
async def spam(ctx, user: discord.Member = None):
    if user is None:
        await ctx.author.send(embed=discord.Embed(title='Please mention a user to DM'))
    else:
        try:
            await user.send('Spamming in {user}')
        except discord.Forbidden:
            await ctx.send('User has DMs disabled.')
            return
        await ctx.author.send(embed=discord.Embed(title=f'✅ Successfully started spamming {user}'))

        tasks = [asyncio.create_task(send(userid=str(user.id), token=token.strip())) for token in tokens]
        await asyncio.gather(*tasks)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(title=f'{ctx.author}, please wait {round(error.retry_after, 2)} seconds before retrying.'))
    elif isinstance(error, commands.CommandInvokeError):
        original = error.original
        if isinstance(original, discord.errors.HTTPException) and original.code == 429:
            await asyncio.sleep(original.retry_after)
            await ctx.reinvoke()
        else:
            raise error

client.run('YOUR_MAIN_BOT_TOKEN')  
