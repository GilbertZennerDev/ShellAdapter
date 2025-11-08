def setshell(cmd):
	supported_shells = ['b', 'ps']
	cmdsplitted = cmd.split()
	if len(cmdsplitted) != 3: return 'NULL', 'NULL'
	if cmdsplitted[0] == 'set' and len(cmdsplitted) == 3:
		i_sh = cmdsplitted[1]
		o_sh = cmdsplitted[2]
	if i_sh and o_sh in supported_shells: return i_sh, o_sh
	else: return 'NULL', 'NULL'