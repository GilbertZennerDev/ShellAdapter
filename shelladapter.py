'''
Plain English Thoughts

I am building a universal shell adapter
for now only bash to PowerShell
so you enter a bash command
cp -r file file2
and it gets translated to PowerShell
Copy-Item -Path '{file}' -Destination '{file2}' -Force"

I am struggling with continuing.

I have implemented cp -r and rm
What next?
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
	if el[0] == 'cp':
		if el[1] == '-r': return cp(el[2], el[3])
		return cp(el[1], el[2])
	if el[0] == 'rm':
		return rm(el[1])
	return txt

def try_run(cmd):
	o = 'Nothing'
	try:
		o = sp.run(give_command(parseInput(cmd)), capture_output=True, text=True, check=True)
		if o.stdout: print(o.stdout)
		if o.stderr: print(o.stderr)
		print(f"Command {cmd} executed successfully!")
	except Exception as e: print(e); exit()

def run_command():
	#cmd = 'rm file2'
	#try_run(cmd)
	#cmd = 'cp -r file file2'
	#try_run(cmd)
	#cmd = 'ls'
	#try_run(cmd)
	cmd = input('Enter Command: ')
	try_run(cmd)

if __name__ == '__main__':
	greet()
	run_command()