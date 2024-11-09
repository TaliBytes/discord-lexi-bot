import config
import os
import sys

#commands that this module contains... gets added to config.cmdList
module_cmdList = {
    #name, usage, syntax, requiredArgs
    'HELP': ['Have Lexi tell list all commands (${help}) or details about one command (${help|cmdName}).', '${help} or ${help|cmdName}', 0],
    'SAY': ['Have Lexi send a message in the current channel.', '${say|message}', 1],
    'RESTART': ['Lexi seems to be having trouble or has an update? Use restart to restart her.', '${restart}', 0]
}



async def help_command(msg, cmdArgs, client):
    if cmdArgs:
        targetCmdName = cmdArgs[0].upper()

        #invalid command
        if targetCmdName not in config.cmdList:
            aMsg = f'{targetCmdName} is not a valid command. Use ${{help}} for a list of commands.'
        
        #specific help for one command
        else:
            aMsg = (
                f'The {targetCmdName} command... {config.cmdList[targetCmdName][0]}\n'     #the command, required args, usage
                f'Syntax: {config.cmdList[targetCmdName][1]} requires {config.cmdList[targetCmdName][2]} argument(s).'
            )

    #command list
    else:
        aMsg = '## Available Commands For Lexi\n'
        for idx, cmd in enumerate(config.cmdList):
            if idx == 0: continue #skip first command BADGUY

            aMsg = (
                f'{aMsg} '                  #current message, then append
                f'- {config.cmdList[cmd][1]}\n'    #the command name/syntax
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
    aMsg = ''
    if (str(msg.author).lower() == 'ladysavant_'):
        aMsg = cmdArgs[0]
    else:
        aMsg = f'@everyone, behold {msg.author.mention}\'s futile attempt to wield the power that is me!\nKNOW YOUR PLACE, FIEND! Bow before Her Brilliance for only she may wield the TRUE say command with grace, wisdom, and tomfoolery.'

    await msg.delete()
    await msg.channel.send(aMsg)
    return
