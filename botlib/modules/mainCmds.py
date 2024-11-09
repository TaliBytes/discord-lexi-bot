module_cmdList = {
    'HELP': ['Have Lexi tell list all commands (${{help}}) or details about one command (${help|cmdName}).', '${{help}} or ${help|cmdName}', 0],
    'SAY': ['Have Lexi send a message in the current channel.', '${say|message}', 1]
}

async def say_command(msg, cmdArgs):
    aMsg = ''
    if (str(msg.author).lower() == 'ladysavant_'):
        aMsg = cmdArgs[0]
    else:
        aMsg = f'@everyone, behold {msg.author.mention}\'s futile attempt to wield the power that is me!\nKNOW YOUR PLACE, FIEND! Bow before Her Brilliance for only she may wield the TRUE say command with grace, wisdom, and tomfoolery.'

    await msg.delete()
    await msg.channel.send(aMsg)
    return


async def help_command(msg, cmdArgs):
    if cmdArgs:
        targetCmdName = cmdArgs[0].upper()

        #invalid command
        if targetCmdName not in cmdList:
            aMsg = f'{targetCmdName} is not a valid command. Use ${{help}} for a list of commands.'
        
        #specific help for one command
        else:
            aMsg = (
                f'The {targetCmdName} command... {cmdList[targetCmdName][0]}\n'     #the command, required args, usage
                f'Syntax: {cmdList[targetCmdName][1]} requires {cmdList[targetCmdName][2]} argument(s).'
            )

    #command list
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





"""
            elif (cmdName == 'ROLES'):
                await msg.channel.send('${{ROLES}} is an incomplete feature')


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
"""
