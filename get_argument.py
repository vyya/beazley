#!/usr/bin/env python3
# get_argument.py

import sys

if len(sys.argv) != 3:
    raise SystemExit('Usage conditions: get_argument.py percent amount')
percent = float(sys.argv[1])
amount = int(sys.argv[2])

first_month = amount + percent/360 * amount
import pdb; pdb.set_trace()
print(f'\nFirst month accumulated amount:{first_month.text}')
print('Amount we have got assuming we had {}$ amount and {} percentage rate'.format(amount, percent))


        
