import globalVars

#commands that this module contains... gets added to config.cmdList
module_cmdList = {
    #name, usage, syntax, requiredArgs
    'ROLES-LIST': ['Ask Lexi what roles exist on the server.', globalVars.cmdStrt + '{roles}', 0, 1],
    'ROLES-JOINED': ['Have Lexi list which roles a server member has', globalVars.cmdStrt + '{roles-joined|serverMember}', 1, 1],
    'ROLE-CREATE': ['Have Lexi create a new server role. Admin only.', globalVars.cmdStrt + '{role-create|roleName}', 1, 2],
    'ROLE-DELETE': ['Have Lexi delete a server role. Admin only.', globalVars.cmdStrt + '{role-delete|roleName}', 1, 2],
    'ROLE-GRANT': ['Have Lexi grant a role from the ' + globalVars.cmdStrt + '{roles} list. Only admins can use serverMember arg. Leave blank for self.', globalVars.cmdStrt + '{role-grant|roleName} or ' + globalVars.cmdStrt + '{role-grant|roleName|serverMember}', 1, 1],
    'ROLE-REVOKE': ['Have Lexi revoke a role from a ' + globalVars.cmdStrt + '{roles-joined|serverMember} list. Only admins can use serverMember arg. Leave blank for self.', globalVars.cmdStrt + '{role-revoke|roleName} or ' + globalVars.cmdStrt + '{role-revoke|roleName|serverMember}', 1, 1],
}



"""
            elif (cmdName == 'ROLES-LIST'):
                await msg.channel.send('${{ROLES-LIST}} is an incomplete feature')


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
