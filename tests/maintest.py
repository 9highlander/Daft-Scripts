import subprocess
import os

path = "../daft_scripts/daft_scripts.py"

# Percorso relativo al file da eseguire
script_path = os.path.join(os.path.dirname(__file__), path)

# Esecuzione dello script
subprocess.run(['python', script_path])
