#!/usr/bin/env python3
import csv
def read_portfolio(filename):
    """ 
     read a CSV file with name, date, shares, price
     data into list
    """
    portfolio = []  # list of records
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        omit = next(f)
        for row in rows:
            #print(row)
            """ line = line.strip() #strip whitespaces
            line = line.split(',') 
            split line by comma delimeter creates set of lists 
        
            line[0] = line[0].strip('"')
            line[1] = line[1].strip('"') # get rid of qpythonuotation marks
            """
            row[2] = int(row[2])
            row[3] = float(row[3]) #convert string to integer
            #record = tuple(row)
            record = {
                'name' : row[0],
                'date' : row[1],
                'shares' : row[2],
                'price' : row[3]
            }
            portfolio.append(record)
            
    return portfolio
portfolio = read_portfolio('Data/portfolio.csv')
total = 0.0
for holding in portfolio:
    total += holding['shares'] * holding['price']
print(portfolio) 
#total = portfolio_cost('Data/portfolio.csv')
print(f'Total cost of all shares is {total}')