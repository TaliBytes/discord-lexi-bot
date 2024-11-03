import discord

#config
tokenFile = open('D:/Code/discord-bot/root/token.txt', 'r')
aToken = tokenFile.readline().strip()
tokenFile.close()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


#when bot logs in
@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')


#when bot sees a "hello" message
@client.event
async def on_message(message):
    if message.author == client.user:   #client.user is this bot
        return

    #$hello command
    if message.content.startswith('$hello'):
        await message.channel.send('Hiya! My name is Lexi and I wi... won\'t burn your house down!')


#run the bot
client.run(aToken)
