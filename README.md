# DaftScripts - daft.ie search with public transport time
A script that use daftlisting library to enable interaction with [Daft.ie](https://daft.ie) and call Google Maps API to know the distance with public transport.
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

Simply run  main.py and compile the search fields. You can save ypur input searches file for future usure.
If ypu choose to use Google Maps Api you need to insert your API key in the json file(Daftscript/api/api/qpi_maps).
Make sure to consider the date and time you give to google maps api because affect the time calculated
