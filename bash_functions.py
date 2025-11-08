def cp(source_file, destination_file):
	return f"Copy-Item -Path '{source_file}' -Destination '{destination_file}' -Force"

def rm(file):
	return f"Remove-Item {file}"

def ls():
    return 'ls'