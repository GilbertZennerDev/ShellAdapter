def setshell():
	supported_shells = ['b', 'ps']
	i_sh = input('Choose input shell: b = bash, ps = powershell')
	o_sh = input('Choose output shell: b = bash, ps = powershell')
	if i_sh and o_sh in supported_shells: return i_sh, o_sh
	else: return 'NULL', 'NULL'