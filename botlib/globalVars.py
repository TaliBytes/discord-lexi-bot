#config.py stores global variables and etc to be used across the project, such as accessLevel and cmdList

#0 is no access, 1 is normal user, 2 is admin, 3 is bot owner (super admin)
accessLevel = 0 

#an list of active commands, their usage, syntax, and number of arguments that they require
cmdList = {
    #name, usage, syntax, requiredArgs, requiredAccessLevel
}

#command prefix and delimiter
cmdStrt = None
cmdDlm = None
ownerID = None