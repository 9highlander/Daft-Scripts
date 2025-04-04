import os
import shutil

def move_file(destination_folder,subfolder, file_name):
    # Get the current directory
    current_directory = os.getcwd()
    # Name of the destination subfolder
    if destination_folder != ' ' :
        destination = destination_folder
    else :
        destination = current_directory + subfolder
    # Create the full path of the source file
    source_file = os.path.join(current_directory, file_name)
    # Create the full path of the destination
    destination_path = os.path.join(current_directory, destination)
    # Create the subfolder if it doesn't exist 
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    # Full path of the destination file
    destination_file = os.path.join(destination_path, file_name)
    # Check if the file already exists in the destination
    if os.path.exists(destination_file):
        os.remove(destination_file)        
    # Move the file
    shutil.move(source_file, destination_file)