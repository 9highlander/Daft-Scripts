import webbrowser
import os

def open_html(subfolder, file_name):
    current_directory = os.getcwd()
    # Percorso del file HTML
    file_path = current_directory + '\\' + subfolder + '\\' + file_name
    # Converti il percorso del file in un URL file://
    file_url = 'file://' + os.path.abspath(file_path)
    print(file_url)
    # Apri il file nel browser predefinito
    webbrowser.open(file_url)

