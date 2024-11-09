import config

#commands that this module contains... gets added to config.cmdList
module_cmdList = {
    #name, usage, syntax, requiredArgs
    'ROLES': ['Ask Lexi what rolls exist on the server.', '${{roles}}', 0],
    'ROLES-JOINED': ['Have Lexi list what roles a server member has', '${roles-joined|serverMember}', 1],
    'ROLE-CREATE': ['Have Lexi create a new server roll. Admin only.', '${roll-create|roleName}', 1],
    'ROLE-DELETE': ['Have Lexi delete a server roll. Admin only.', '${roll-delete|roleName}', 1],
    'ROLE-GRANT': ['Have Lexi grant a roll from the ${{roles}} list. Only admins can use serverMember arg. Leave blank for self.', '${role-grant|roleName} or ${role-grant|roleName|serverMember}', 1],
    'ROLE-REVOKE': ['Have Lexi revoke a roll from a ${roles-joined|serverMember} list. Only admins can use serverMember arg. Leave blank for self.', '${role-revoke|roleName} or ${role-revoke|roleName|serverMember}', 1],
}



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
