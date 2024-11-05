import discord

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
            await msg.channel.send('${' + cmdName + '} requires ' + str(requiredArgs) + ' argument(s); ' + 'Syntax: ' + cmdSyntax)
            return



        #ACTUAL COMMAND OPTIONS BEGIN HERE:
        if (cmdName == 'SAY'):
            aMsg = ''
            if (str(msg.author).lower() == 'ladysavant_'):
                aMsg = cmdArgs[0]
            else:
                aMsg = f'@everyone, behold {msg.author.mention}\'s futile attempt to wield the power that is me!\nKNOW YOUR PLACE, FIEND! Bow before Her Brilliance for only she may wield the TRUE say command with grace, wisdom, and tomfoolery.'

            await msg.delete()
            await msg.channel.send(aMsg)
            return
        

        elif (cmdName == 'HELP'):
            aMsg = ''

            if cmdArgs:
                targetCmdName = cmdArgs[0].upper()
                
                if targetCmdName not in cmdList:
                    aMsg = f'{targetCmdName} is not a valid command. Use ${{help}} for a list of commands.'
                else:
                    aMsg = (
                        f'The {targetCmdName} command... {cmdList[targetCmdName][0]}\n'     #the command, required args, usage
                        f'Syntax: {cmdList[targetCmdName][1]} requires {cmdList[targetCmdName][2]} argument(s).'
                    )
            else:
                aMsg = '## Available Commands For Lexi\n'
                for idx, cmd in enumerate(cmdList):
                    if idx == 0: continue #skip first command BADGUY
                    aMsg = (
                        f'{aMsg} '                  #current message, then append
                        f'- {cmdList[cmd][1]}\n'    #the command name/syntax
                    )
            
            await msg.channel.send(aMsg)
            return


        elif (cmdName == 'ROLES'):
            await msg.channel.send('$\{ROLES\} is an incomplete feature')


        elif (cmdName == 'ROLES-JOINED'):
            await msg.channel.send('${ROLES-JOINED} is an incomplete feature')


        elif (cmdName == 'ROLE-CREATE'):
            await msg.channel.send('${ROLE-CREATE} is an incomplete feature')

            
        elif (cmdName == 'ROLE-DELETE'):
            await msg.channel.send('${ROLE-DELETE} is an incomplete feature')


        elif (cmdName == 'ROLE-GRANT'):
            await msg.channel.send('${ROLE-GRANT} is an incomplete feature')


        elif (cmdName == 'ROLE-REVOKE'):
            await msg.channel.send('${ROLE-REVOKE} is an incomplete feature')


        #the cmd logic is missing or cmd is incorrectly considered valid; so this debug message is sent.
        else:
            print('cmdErr-01... a cmd passed the "cmdName not in cmdList" check, but logic is absent.')
            await msg.channel.send('cmdErr-01. Please contact a developer to debug.')



#an alphabetical-ordered list of valid commands, they usage, syntax, and number of arguments that they require
cmdList = {
    #name, usage, syntax, requiredArgs
    'BADGUY': ['Command intentionally missing logic for debug/test purposes.', '$\{badguy\}', 0],           #LEAVE BADGUY ON FIRST LINE

    #commands to iterate over when using ${help}...
    'HELP': ['Have Lexi tell list al\l commands ($\{help\}) or details about one command (${help|cmdName}).', '$\{help\} or ${help|cmdName}', 0],
    'ROLES': ['Ask Lexi what rolls exist on the server.', '$\{roles\}', 0],
    'ROLES-JOINED': ['Have Lexi list what roles a server member has', '${roles-joined|serverMember}', 1],
    'ROLE-CREATE': ['Have Lexi create a new server roll. Admin only.', '${roll-create|roleName}', 1],
    'ROLE-DELETE': ['Have Lexi delete a server roll. Admin only.', '${roll-delete|roleName}', 1],
    'ROLE-GRANT': ['Have Lexi grant a roll from the $\{roles\} list. Only admins can use serverMember arg. Leave blank for self.', '${role-grant|roleName} or ${role-grant|roleName|serverMember}', 1],
    'ROLE-REVOKE': ['Have Lexi revoke a roll from a ${roles-joined|serverMember} list. Only admins can use serverMember arg. Leave blank for self.', '${role-revoke|roleName} or ${role-revoke|roleName|serverMember}', 1],
    'SAY': ['Have Lexi send a message in the current channel.', '${say|message}', 1]
}



#start the bot
client.run(aToken)
