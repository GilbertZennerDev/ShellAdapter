def give_function(cmd, *files):
	obj = {
		'cp': f"Copy-Item -Path '{files[0]}' -Destination '{files[1]}' -Force",
  		'mv': f"Move-Item -Path '{files[0]}' -Destination '{files[1]}' -Force",
		'rm': f"Remove-Item {files[0]}",
		'cd' : f"Set-Location {files[0]}",
		'pwd' : 'pwd',
		'cat' : f'Get-Content {files[0]}',
		'echo' : f'Write-Output {files[0]}',
	}
	return obj[cmd]