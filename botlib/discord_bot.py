import discord
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




#an alphabetical-ordered list of valid commands, they usage, syntax, and number of arguments that they require
cmdList = {
    #name, usage, syntax, requiredArgs
    'ROLES': ['Ask Lexi what rolls exist on the server.', '${{roles}}', 0],
    'BADGUY': ['Command intentionally missing logic for debug/test purposes.', '${{badguy}}', 0],           #LEAVE BADGUY ON FIRST LINE

    #commands to iterate over when using ${help}...
    'ROLES-JOINED': ['Have Lexi list what roles a server member has', '${roles-joined|serverMember}', 1],
    'ROLE-CREATE': ['Have Lexi create a new server roll. Admin only.', '${roll-create|roleName}', 1],
    'ROLE-DELETE': ['Have Lexi delete a server roll. Admin only.', '${roll-delete|roleName}', 1],
    'ROLE-GRANT': ['Have Lexi grant a roll from the ${{roles}} list. Only admins can use serverMember arg. Leave blank for self.', '${role-grant|roleName} or ${role-grant|roleName|serverMember}', 1],
    'ROLE-REVOKE': ['Have Lexi revoke a roll from a ${roles-joined|serverMember} list. Only admins can use serverMember arg. Leave blank for self.', '${role-revoke|roleName} or ${role-revoke|roleName|serverMember}', 1],
}

#import additional modules
module_dir = os.path.join(os.path.dirname(__file__), 'modules')
for filename in os.listdir(module_dir):
    if filename.endswith('.py'):
        module_name = filename[:-3]
        module = importlib.import_module(f"modules.{module_name}")
        
        #add each module's commands to cmdList
        cmdList.update(module.module_cmdList)

        #register each async function in the module as a command
        for name, func in inspect.getmembers(module, inspect.iscoroutinefunction):
            globals()[name] = func

        #print("Registered commands:", cmdList) #USE FOR DEBUGGING WHAT COMMANDS ARE ACTIVE

#sort cmd list alphabetically
cmdList = dict(sorted(cmdList.items()))  




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
    
    if (msg.content.strip().startswith('${') & msg.content.strip().endswith('}')):
        #prase command for processing
        aCmd = parseCmd(msg.content)
        cmdName = aCmd[0]
        cmdArgs = aCmd[1]

        print('Received command ${' + cmdName.lower() + '} from ' + str(msg.author) + ' with args ' + (', '.join(f'"{arg}"' for arg in cmdArgs) if cmdArgs else 'not supplied'))

        #is command valid?
        if cmdName not in cmdList:
            print('${' + cmdName + '} is an invalid command.')
            await msg.channel.send('${' + cmdName + '} is not a valid command. Do ${{help}} to get a list of commands.')
            return
        else: 
            #get number of arguments required for a command    
            requiredArgs = cmdList[cmdName][2]

        #not enough args supplied
        if (len(isnone(cmdArgs,'')) < requiredArgs):
            cmdSyntax = cmdList[cmdName][1]             #get syntax for error message
            print('Incorrect ${' + cmdName + '} syntax; correct: ' + cmdSyntax)
            await msg.channel.send('${' + cmdName + '} requires ' + str(requiredArgs) + ' argument(s); ' + 'Syntax: ' + cmdSyntax)
            return

        #process the command
        if cmdName in cmdList:
            #get command function
            command_function = globals().get(f"{cmdName.lower()}_command")

            #execute command function
            if command_function:
                await command_function(msg, cmdArgs)

            #the cmd logic is missing or cmd is incorrectly considered valid; so this debug message is sent.
            else:
                print(f'cmdErr-01... {cmdName} passed the "cmdName in cmdList" check, but logic is absent.')
                await msg.channel.send(f'cmdErr-01... {cmdName} is not implemented yet.')

        #command not in list
        else:
            await msg.channel.send('${' + cmdName + '} is not a valid command. Do ${{help}} to get a list of commands.')




#start the bot
client.run(aToken)
