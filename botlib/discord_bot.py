import discord

#config
tokenFile = open('D:/Code/discord-bot/root/token.txt', 'r')
aToken = tokenFile.readline().strip()
tokenFile.close()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


#return val if var is null
def isnone(var, val):
    if var is None:
        return val
    return var


#parse command and return its name and args to process
def parseCmd(cmd):
    cmdPrfx = "${"          #prefix to denote start of cmd
    cmdSfx = "}"            #suffix to denote end of cmd
    cmdDelim = '|'          #delim to split cmdName and args
    cmdName = None
    cmdArgs = []

    #reformat the command
    cmd = cmd.strip()                       #remove whitespace
    cmd.replace('|}', '')                   #remove last arg if empty
    cmd.replace('||', '')                   #remove empty args
    cmdStartPos = cmd.index(cmdPrfx) + 2    #start position for cmd name and arguments
    cmdEndPos = cmd.index(cmdSfx)           #end position for cmd name and arguments
    cmd = cmd[cmdStartPos:cmdEndPos]        #store cmd without brackets

    if (cmdDelim not in cmd):
        cmdName = cmd                       #whole cmd is the name
        cmdArgs = None                      #no args were supplied

    else:
        cmdArgs = cmd.split(cmdDelim)           #extract arguments from full command
        cmdName = cmdArgs[0]                    #extract name from arglist (first argument)
        cmdArgs = cmdArgs[1:]                   #remove cmdName from args  (remaining arguments)

    return(cmdName, cmdArgs)



#when bot logs in
@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')


#when bot receives a command
@client.event
async def on_message(msg):
    #client.user is this bot ... don't respond
    if msg.author == client.user:
        return
    
    #if command
    if msg.content.startswith('${'):
        aCmd = parseCmd(msg.content)
        cmdName = aCmd[0].lower()
        cmdArgs = aCmd[1]

        #used for debug
        print('Received command ${' + cmdName + '} with args ' + (', ').join(cmdArgs) if cmdArgs else 'not supplied')

        #is command valid?
        if cmdName not in cmdList:
            await msg.channel.send('${' + cmdName + '} is not a valid command. Do $\{help\} to get a list of commands.')
            return
        else: 
            #get number of arguments required for a command    
            requiredArgs = cmdList[cmdName][2]

        #not enough args supplied
        if (len(isnone(cmdArgs,'')) < requiredArgs):
            cmdSyntax = cmdList[cmdName][1]      #get syntax
            await msg.channel.send('${' + cmdName + '} requires ' + str(requiredArgs) + ' argument(s); ' + 'syntax: ' + cmdSyntax)
            return


        #ACTUAL COMMAND OPTIONS BEGINS HERE:
        if (cmdName == 'say'):
            await msg.channel.send(cmdArgs[0])



#a list of valid commands, they usage, syntax, and number of arguments that they require
cmdList = {
    #name, usage, syntax, requiredArgs
    'say': ['Have Lexi send a message in the current channel.', '${say|message}', 1]
}



#start the bot
client.run(aToken)
