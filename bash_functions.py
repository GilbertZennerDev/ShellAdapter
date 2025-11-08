def give_function(cmd, *files):
	obj = {
		'cp': f"Copy-Item -Path '{files[0]}' -Destination '{files[1]}' -Force",
		'rm': f"Remove-Item {files[0]}",
	}
	return obj[cmd]

def cp(source_file, destination_file):
	return f"Copy-Item -Path '{source_file}' -Destination '{destination_file}' -Force"

def rm(file):
	return f"Remove-Item {file}"