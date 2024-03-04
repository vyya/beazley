#!/usr/bin/env python3
principal = 500000
payment = 2684.11
rate = 0.05
total_paid = 0
month = 0
# Extra payment info
extra_payment = 1000
extra_payment_start_month = 1
extra_payment_end_month = 60
while principal > 0:
    month +=1
    if month <= extra_payment_end_month:
        total_payment = payment + extra_payment
    else:
        total_payment = payment

    interest = principal*(rate/12)
    print('Interest:', interest)
    #raise SystemExit(0)
    principal = principal + interest - total_payment
    #print('Principal:', principal)
    total_paid += total_payment
print('Total paid:', total_paid, 'For period:', month/12)