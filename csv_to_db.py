# Copyright 2018 Alexander Gompper
# Released under MIT License

import csv
import json
import random
import string


def main():
    print('<<< WHATBOT CSV PROFILE READER - CSV TO DB >>>')
    try:
        with open('input/csv/billing.csv') as input_file:

            input_reader = csv.DictReader(input_file, fieldnames=[
                'name',
                'firstName',
                'lastName',
                'phone',
                'email',
                'address',
                'address2',
                'city',
                'state',
                'zipCode',
                'cardName',
                'cardNumber',
                'cardMonth',
                'cardYear',
                'cardCvv',
                '_id',
                'quickTask'
            ])
            next(input_reader)
            try:
                with open('output/db/billing.db', 'wb') as output_file:
                    for row in input_reader:
                        row['_id'] = ''.join(random.choices(string.ascii_letters + string.digits, k=16)) if row['_id'] in {'', None} else row['_id']
                        row['quickTask'] = True if row['quickTask'].lower() == 'true' else False
                        output_file.write(bytes((json.dumps(row) + '\n').encode('utf-8')))
            except IOError:
                print('<<< [error] something went wrong writing the billing.db output file >>>')
                exit(-1)
            print('<<< COMPLETE >>>')
    except IOError:
        print('<<< [error] something went wrong opening the billing.csv input file >>>')
        exit(-1)


if __name__ == '__main__':
    main()
