# DaftScripts - daft.ie search with public transport time
A script with GUI that use daftlisting library to enable interaction with [Daft.ie](https://daft.ie) and call Google Maps API to know the distance with public transport.
I make the script for personal purpose because when i search for a home the commuting time factor is an important factor.
However at the moment this script is more a code exercise for exercise with API calling , pandas and other things.


## Installation

### Install `virtualenv` (optional)

```sh
python -m pip install virtualenv
```

### Create a Virtual Environment

```sh
python -m venv venv
```

| Code  | Explanation                     |
| ----- | ------------------------------- |
| `-m`  | executes module `venv`          |
| `env` | name of the virtual environment |

### Activate environment

```sh
source venv/bin/activate
```

### Install `requirements`

```sh
pip install -r requirements.txt
```

## Getting Started
### Insert Google Maps Api(optional)
If you choose to use Google Maps Api you need to insert your API key in the json file(Daftscript/api/api/qpi_maps).
There is already an example file api_maps_example.json , you can just rename it api_mapse.json.
Note than .gitignore file already excludes api_mapse.json file.

![image](https://github.com/user-attachments/assets/53235b80-e3dd-4966-ad24-ace98acd4750)


Make sure to consider the date and time you give to google maps api because affect the time calculated.

### Start the script
Simply run  daft_script.py (daft_scripts/daft/scripts.py) or maintest.py(tests/main_test.py) and compile the search fields. You can save your input searches file for future usure.
![image](https://github.com/user-attachments/assets/36abb30c-3506-409c-b7ff-fc4d1af3c051)


![image](https://github.com/user-attachments/assets/c6390fa1-7397-41f7-8f64-bb968154bd65)


### See  results
The results saved as a map in an html page (made with folium).
You can choose if open directly the results map in yout default browser or not.

![image](https://github.com/user-attachments/assets/6d7dfb46-fcdd-4d58-aae3-52620e21f624)

