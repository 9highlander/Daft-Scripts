import os
import json

def read_json(subfolder, file_name, variable_name):
    current_directory = os.getcwd()
    print("current directory",current_directory)
    file_path = current_directory + '\\' + subfolder + '\\' + file_name
    print("file path",file_path)
    if file_path:
        with open(file_path, 'r') as file:
                data = json.load(file)
        return data[variable_name]