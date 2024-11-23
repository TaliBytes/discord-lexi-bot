import discord
import globalVars
import importlib
import inspect
import os



#config
tokenFile = open('root/token.txt', 'r')
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
    cmdPrfx = globalVars.cmdStrt + '{'          #prefix to denote start of cmd
    cmdSfx = "}"                                #suffix to denote end of cmd
    cmdDelim = globalVars.cmdDlm                #delim to split cmdName and args
    cmdName = None
    cmdArgs = []

    #reformat the command
    cmd = cmd.strip()                       #remove whitespace
    cmd.replace(cmdDelim + '}', '')                   #remove last arg if empty
    cmd.replace(cmdDelim + cmdDelim, '')    #remove empty args
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





#get the configuration settings from the file
def syncConfig():
    with open('root/config.txt', 'r') as file:
        config = {}

        for line in file:
            line = line.strip()

            #ignore comments and blank lines
            if not line or line.startswith('#'): continue

            if '=' in line:
                variable, value = line.split('=', 1)
                config[variable.strip()] = value.strip()

    cmdStrt = config['commandStart']
    cmdDlm = config['commandDelimiter']
    ownerID = config['ownerDiscordID']

    #store config.txt value or defaults into the globalVars
    globalVars.cmdStrt = isnone(cmdStrt, '$')
    globalVars.cmdDlm = isnone(cmdDlm, '|')
    globalVars.ownerID = int(ownerID)

    #fatal errors... bot MUST have certain config settings to run correctly
    if globalVars.cmdStrt is None or globalVars.cmdDlm is None or globalVars.ownerID in (0, None):
        print('\nFATAL CONFIGURATION ERROR!')
        if (globalVars.cmdStrt is None): print('Must include commandStart value in config.txt')
        if (globalVars.cmdDlm is None): print('Must include commandDelimiter value in config.txt')
        if (globalVars.ownerID in (0, None)): print('Must include ownerDiscordID value in config.txt')
        os._exit(1)





#import additional modules and commands
def syncCmdList():
    module_dir = os.path.join(os.path.dirname(__file__), 'modules')
    for filename in os.listdir(module_dir):
        if filename.endswith('.py'):
            module_name = filename[:-3]
            module = importlib.import_module(f"modules.{module_name}")

            #add each module's commands to cmdList
            globalVars.cmdList.update(module.module_cmdList)

            #register each async function in the module as a command
            for name, func in inspect.getmembers(module, inspect.iscoroutinefunction):
                globals()[name] = func

            #print('\nRegistered commands:', globalVars.cmdList) #USE FOR DEBUGGING WHAT COMMANDS ARE ACTIVE

    #sort cmd list alphabetically
    globalVars.cmdList = dict(sorted(globalVars.cmdList.items())) 





def getAccessLevel(discordID):
    #REPLACE WITH ACTUAL LOGIC
    globalVars.accessLevel = 3 if (globalVars.ownerID == discordID) else 1
    return(globalVars.accessLevel)





#when bot logs in
@client.event
async def on_ready():
    print(f'Logged in as {client.user}.\n')

    syncConfig()    #initialize the configuration settings
    syncCmdList()   #prepare the command list variable





#when bot receives a command
@client.event
async def on_message(msg):
    #client.user is this bot ... don't respond
    if msg.author == client.user:
        return
    
    if (msg.content.strip().startswith(globalVars.cmdStrt + '{') & msg.content.strip().endswith('}')):
        #prase command for processing
        aCmd = parseCmd(msg.content)
        cmdName = aCmd[0]
        cmdArgs = aCmd[1]

        print('\nReceived command ' + globalVars.cmdStrt + '{' + cmdName + '} from ' + str(msg.author) + ' with args ' + (', '.join(f'"{arg}"' for arg in cmdArgs) if cmdArgs else 'not supplied'))

        #determines what access level this discord user has, and stores in globalVar
        userAccessLevel = getAccessLevel(msg.author.id)

        #insufficient permission/access level
        if (globalVars.cmdList[cmdName][3] > userAccessLevel):
            print('\n' + str(msg.author) + ' cannot access the ' + globalVars.cmdStrt + '{' + cmdName + '} command due to insufficient permissions.')
            await msg.channel.send('You don\'t have sufficient permissions to access the ' + globalVars.cmdStrt + '{' + cmdName.lower() + '} command. Do ' + globalVars.cmdStrt + '{help} to get a list of commands you can access. If you beleive this is in error, please contact a server administrator.')
            return

        #command is not valid
        if cmdName not in globalVars.cmdList:
            print('\n' + '${' + cmdName + '} is an invalid command. Failed discord_bot cmdName test.')
            await msg.channel.send(globalVars.cmdStrt + '{' + cmdName.lower() + '} is not a valid command. Do ' + globalVars.cmdStrt + '{help} to get a list of commands.')
            return

        #not enough args supplied
        if (len(isnone(cmdArgs,'')) < globalVars.cmdList[cmdName][2]):
            cmdSyntax = globalVars.cmdList[cmdName][1]             #get syntax for error message
            print('\n' + 'Incorrect ' + globalVars.cmdStrt + '{' + cmdName.lower() + '} syntax; correct: ' + cmdSyntax)
            await msg.channel.send(globalVars.cmdStrt  +'{' + cmdName.lower() + '} requires ' + str(globalVars.cmdList[cmdName][2]) + ' argument(s); ' + 'Syntax: ' + cmdSyntax)
            return

        #all checks passed... process the command
        if cmdName in globalVars.cmdList:
            #get command function
            command_function = globals().get(f"{cmdName.lower()}_command")

            #execute command function
            if command_function:
                await command_function(msg, cmdArgs, client)

            #the cmd logic is missing or cmd is incorrectly considered valid; so this debug message is sent.
            else:
                print(f'\ncmdErr-01... {cmdName} passed the "cmdName in cmdList" check, but logic is absent.')
                await msg.channel.send(f'cmdErr-01... {cmdName.lower()} is not implemented yet.')





#start the bot
client.run(aToken)
