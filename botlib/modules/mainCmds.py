import globalVars
import os
import sys

#commands that this module contains... gets added to config.cmdList
module_cmdList = {
    #name, usage, syntax, requiredArgs, required access level (1 - normal user, 2 - admin, 3 - bot owner)
    'HELP': ['Have Lexi tell list all commands (' + globalVars.cmdStrt + '{help}) or details about one command (' + globalVars.cmdStrt + '{help|cmdName}).', globalVars.cmdStrt + '{help} or ' + globalVars.cmdStrt + '{help|cmdName}', 0, 1],
    'SAY': ['Have Lexi send a message in the current channel.', globalVars.cmdStrt + '{say|message}', 1, 1],
    'RESTART': ['Lexi seems to be having trouble or has an update? Use restart to restart her.', globalVars.cmdStrt + '{restart}', 0, 2]
}



async def help_command(msg, cmdArgs, client):
    if cmdArgs:
        targetCmdName = cmdArgs[0].upper()

        #lookup of command failed
        if targetCmdName not in globalVars.cmdList:
            print(f'{globalVars.cmdStrt}{targetCmdName} is an invalid command. Failed help command lookup.')
            aMsg = f'{targetCmdName} is not a valid command. Use {globalVars.cmdStrt}{{help}} for a list of commands.'
        
        #specific help for one command
        else:
            aMsg = (
                f'The {targetCmdName} command... {globalVars.cmdList[targetCmdName][0]}\n'     #the command, required args, usage
                f'Syntax: {globalVars.cmdList[targetCmdName][1]} requires {globalVars.cmdList[targetCmdName][2]} argument(s).'
            )

    #command list
    else:
        aMsg = '## Available Commands For Lexi\n'
        for cmd in globalVars.cmdList:
            #user access level required to use command is insufficient; therefore, skip...
            if globalVars.cmdList[cmd][3] > globalVars.accessLevel: continue

            aMsg = (
                f'{aMsg} '                          #current message, then append
                f'- {globalVars.cmdList[cmd][1]}\n'     #the command name/syntax
            )

    await msg.channel.send(aMsg)
    return



async def restart_command(msg, cmdArgs, client):
    """Restarts the bot."""
    await msg.channel.send('Restarting...')
    await client.close()

    # Restart bot
    os.execv(sys.executable, [sys.executable] + sys.argv)



async def say_command(msg, cmdArgs, client):
    aMsg = str(msg.author) + ' says "' + cmdArgs[0] + '"'

    await msg.delete()
    await msg.channel.send(aMsg)
    return
