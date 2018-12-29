# WhatBotCSV

A quick few scripts to turn ?bot billing profiles into a more human-readable CSV format. Use this to transport billing
profiles to remote VPS, or make bulk edits with a program like Excel/Numbers.

Note: its a good idea to backup your billing profiles somewhere safe before and after using this tool, just in case it breaks.

`quickTask` field defaults to false if it doesn't recognize 

`_id` field is automatically generated if the field is left blank


## Installation

Requires Python3.

No external packages necessary. Just clone and run the respective Python files.

`git clone`

`cd WhatBotCSV`


## Usage

Input files go in the input db or csv directories.

Output files will be written to the output folder.


```bash
# to turn ?bot format into csv format
$ python3 db_to_csv.py


# to turn csv format into ?bot format:
$ python3 csv_to_db.py
```



Ping me on slack if you have issues.

## Todo

* [ ] automatically find billing.db location
* [ ] command line args
* [ ] more export options