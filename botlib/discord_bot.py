import discord

#config
tokenFile = open('D:/Code/discord-bot/root/token.txt', 'r')
aToken = tokenFile.readline().strip()
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


#when bot is logged in
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


#when bot sees a messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hiya!')

client.run(aToken)
