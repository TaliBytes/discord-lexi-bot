import discord

#config
tokenFile = open('root/token.txt', 'r')
aToken = tokenFile.readline().strip()
tokenFile.close()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

jokes = '../root/jokes.txt'
nsfw_jokes = 'root/nsfw_jokes.txt'


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
        cmdArgs = cmd.split(cmdDelim)       #extract arguments from full command
        cmdName = cmdArgs[0]                #extract name from arglist (first argument)
        cmdArgs = cmdArgs[1:]               #remove cmdName from args  (remaining arguments)

    return(cmdName.upper(), cmdArgs)



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
    if (msg.content.strip().startswith('${') & msg.content.strip().endswith('}')):
        aCmd = parseCmd(msg.content)
        cmdName = aCmd[0]
        cmdArgs = aCmd[1]

        #used for debug
        print('Received command ${' + cmdName.lower() + '} from ' + str(msg.author) + ' with args ' + (', '.join(f'"{arg}"' for arg in cmdArgs) if cmdArgs else 'not supplied'))

        #is command valid?
        if cmdName not in cmdList:
            print('${' + cmdName + '} is an invalid command.')
            await msg.channel.send('${' + cmdName + '} is not a valid command. Do $\{help\} to get a list of commands.')
            return
        else: 
            #get number of arguments required for a command    
            requiredArgs = cmdList[cmdName][2]

        #not enough args supplied
        if (len(isnone(cmdArgs,'')) < requiredArgs):
            cmdSyntax = cmdList[cmdName][1]             #get syntax for error message
            print('Incorrect ${' + cmdName + '} syntax; correct: ' + cmdSyntax)
            await msg.channel.send('${' + cmdName + '} requires ' + str(requiredArgs) + ' argument(s); ' + 'syntax: ' + cmdSyntax)
            return


        #ACTUAL COMMAND OPTIONS BEGIN HERE:
        if (cmdName == 'SAY'):
            await msg.channel.send(cmdArgs[0])
            return
        
        elif (cmdName == 'HELP'):
            print('HELP command incomplete')
            return

        else:
            #the cmd logic is missing or cmd is incorrectly considered valid; so this debug message is sent.
            print('cmdErr-01... a cmd passed the "cmdName not in cmdList" check, but logic is absent.')
            await msg.channel.send('cmdErr-01. Please contact a developer to debug.')



#a list of valid commands, they usage, syntax, and number of arguments that they require
cmdList = {
    #name, usage, syntax, requiredArgs
    'SAY': ['Have Lexi send a message in the current channel.', '${say|message}', 1],
    'HELP': ['Have Lexi tell list all commands ($\{help\}) or details about one command (${help|cmdName}).', '$\{help\} or ${help|cmdName}', 0],
    'BADGUY': ['Command intentionally missing logic for debug/test purposes.', '$\{badguy\}', 0]
}



#start the bot
client.run(aToken)
