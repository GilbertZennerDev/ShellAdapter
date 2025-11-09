'''
Plain English Thoughts

I am building a universal shell adapter
for now only bash to PowerShell
so you enter a bash command
cp -r file file2
and it gets translated to PowerShell
Copy-Item -Path '{file}' -Destination '{file2}' -Force"

'''

import sys
import subprocess as sp
from bash_functions import *
from set_shell import *

def greet():
	NAME = 'Shell Adapter'
	print("Welcome to", NAME)

def give_command(cmd):
	return [
		'powershell.exe',
		'-Command',
		cmd
	]

def parseInput(txt):
	el = txt.split(' ')
	for i in range(10): el.append('')
	if el[0] in ['rm', 'cp', 'cd', 'pwd', 'cat']: return give_function(el[0], *el[1:])
	return txt

def try_run(cmd):
	o = 'Nothing'
	try:
		o = sp.run(give_command(parseInput(cmd)), capture_output=True, text=True, check=True)
		if o.stdout: print(o.stdout)
		if o.stderr: print(o.stderr)
		print(f"Command {cmd} executed successfully!")
		return cmd
	except Exception as e: print(e); exit()

def run_command():
	while 1:
		cmd = input('Enter Command: ')
		if cmd == 'exit': exit()
		try_run(cmd)

if __name__ == '__main__':
	greet()
	run_command()