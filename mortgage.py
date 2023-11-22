#!/usr/bin/env python3

# mortgage calculator
# Find out for how long to pay off a mortgage

principal = 500000
payment = 2684.11
rate = 0.05
total_paid = 0

# Extra payment info
extra_payment = 1000
extra_payment_start_month = 1
extra_payment_end_month = 60
month = 0

while principal > 0:
    month +=1
    interest = principal*(rate/12)
    print(f'Interst:{interest}')
    principal = principal + interest - payment
    print(f'Principal before extra:{principal}')
    if month in range(extra_payment_start_month, extra_payment_end_month+1):
        principal = principal - extra_payment
    print(f'Principal:{principal}')
    total_paid += payment
    print(f'Total paid: {total_paid}')
    print(f'Month:{month}')
    
    
    #import pdb; pdb.set_trace()
print(f'Total paid: {total_paid}')