#!/usr/bin/env python3
import csv
def portfolio_cost(filename):
    """ 
     Compute total shares*price for a CSV file with name, date, shares, price
     data
    """
    total_cost = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        omit = next(f)
        for row in rows:
            print(row)
            """ line = line.strip() #strip whitespaces
            line = line.split(',') 
            split line by comma delimeter creates set of lists 
        
            line[0] = line[0].strip('"')
            line[1] = line[1].strip('"') # get rid of qpythonuotation marks
            """
            row[2] = int(row[2])
            row[3] = float(row[3]) #convert string to integer
            total_cost+= row[2] * row[3]
    return total_cost

total = portfolio_cost('Data/portfolio.csv')
print(f'Total cost of all shares is {total}')