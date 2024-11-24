import globalVars

#commands that this module contains... gets added to config.cmdList
module_cmdList = {
    #name, usage, syntax, requiredArgs
    'ROLES_LIST': ['Ask Lexi what roles exist on the server.', globalVars.cmdStrt + '{roles_list}', 0, 1],
    'ROLES_JOINED': ['Have Lexi list which roles a server member has', globalVars.cmdStrt + '{roles_joined|serverMember}', 1, 1],
    'ROLE_CREATE': ['Have Lexi create a new server role. Admin only.', globalVars.cmdStrt + '{role_create|roleName}', 1, 2],
    'ROLE_DELETE': ['Have Lexi delete a server role. Admin only.', globalVars.cmdStrt + '{role_delete|roleName}', 1, 2],
    'ROLE_GRANT': ['Have Lexi grant a role from the ' + globalVars.cmdStrt + '{role_grant} list. Only admins can use serverMember arg. Leave blank for self.', globalVars.cmdStrt + '{role_grant|roleName} or ' + globalVars.cmdStrt + '{role_grant|roleName|serverMember}', 1, 1],
    'ROLE_REVOKE': ['Have Lexi revoke a role from a ' + globalVars.cmdStrt + '{roles_revoke|serverMember} list. Only admins can use serverMember arg. Leave blank for self.', globalVars.cmdStrt + '{role_revoke|roleName} or ' + globalVars.cmdStrt + '{role_revoke|roleName|serverMember}', 1, 1],
}



async def roles_list_command(msg, cmdArgs, client):
    await msg.channel.send('{ROLES_LIST} is an incomplete feature')



async def roles_joined_command(msg, cmdArgs, client):
    await msg.channel.send('{ROLES_LIST} is an incomplete feature')



async def roles_create_command(msg, cmdArgs, client):
    await msg.channel.send('{ROLES_LIST} is an incomplete feature')



async def roles_delete_command(msg, cmdArgs, client):
    await msg.channel.send('{ROLES_LIST} is an incomplete feature')



async def roles_grant_command(msg, cmdArgs, client):
    await msg.channel.send('{ROLES_LIST} is an incomplete feature')



async def roles_revoke_command(msg, cmdArgs, client):
    await msg.channel.send('{ROLES_LIST} is an incomplete feature')
