# Copyright 2018 Alexander Gompper
# Released under MIT License

import csv
import json


def main():
    print('<<< WHATBOT CSV PROFILE READER - DB TO CSV >>>')
    try:
        with open('input/db/billing.db', 'rb') as input_file:
            file_string = input_file.read().decode('utf-8')
            rows = file_string.split('\n')
            dicts = list()
            for row in rows:
                if row not in {None, '', '\n'}:
                    dicts.append(json.loads(row.strip('\n')))
            try:
                with open('output/csv/billing.csv', 'w') as f:
                    w = csv.DictWriter(f, dicts[0].keys())
                    w.writeheader()
                    w.writerows(dicts)
            except IOError:
                print('<<< [error] something went wrong writing the billing.csv output file >>>')
                exit(-1)
    except IOError:
        print('<<< [error] something went wrong reading the billing.db input file >>>')
        exit('-1')
    print('<<< COMPLETE >>>')


if __name__ == '__main__':
    main()
