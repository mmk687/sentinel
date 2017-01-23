# sentinel
Playing with shodan API

## Requirements

##shodan
pip install shodan

### argparse
pip install argparse

### pwn
pip install pwntools

### API Key
Get your API Key by [subscribing](https://shodan.io/store/member) a shodan member account.

## Setup
* Create a file named "key" at the project root, chmod it for reading, and fill it with your API key
* Enjoy the sentinel.py script.
* You can also create your own using lib files

## Usage
usage: sentinel.py [-h] [--search SEARCH] [--file FILE] [--netcams]

optional arguments:
  -h, --help       show this help message and exit
  --search SEARCH  term to search
  --file FILE      file to store search result
  --netcams        Look for netcams

