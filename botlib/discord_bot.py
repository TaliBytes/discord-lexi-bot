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
    if message.content.startswith('${'):
        aCmd = parseCmd(message.content)
        cmdName = aCmd[0]
        cmdArgs = aCmd[1]

        if (cmdName == 'say'):
            await message.channel.send(cmdArgs[0])




#parse command and return its name and args to process
def parseCmd(cmd):
    cmdPrfx = "${"          #prefix to denote start of cmd
    cmdSfx = "}"            #suffix to denote end of cmd
    cmdDelim = '|'          #delim to split cmdName and args

    cmd = cmd.strip()
    cmdName = None
    cmdArgs = []

    cmdStartPos = cmd.index(cmdPrfx) + 2    #start position for cmd name and arguments
    cmdEndPos = cmd.index(cmdSfx)           #end position for cmd name and arguments
    cmd = cmd[cmdStartPos:cmdEndPos]        #store cmd without brackets

    cmdArgs = cmd.split(cmdDelim)           #extract arguments from full command
    cmdName = cmdArgs[0]                    #extract name from arglist
    cmdArgs = cmdArgs[1:]                   #remove cmdName from args

    return(cmdName, cmdArgs)



#run the bot
client.run(aToken)
