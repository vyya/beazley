import csv
import glob
def read_portfolio(filename, *, errors = 'warn'):
    """ Read a CSV file with name, date, shares, price into a list """
    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("Errors must be one of 'warn', 'silent', 'raise'")
    portfolio = [] # list of records
    total = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        rownumber = 0
        for rownumber, row in enumerate(rows, start=1):
            """ line = line.strip() # strip whitespace off
            parts = line.split(',')
            parts[0] = parts[0].strip('"')
            parts[1] = parts[1].strip('"') """
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except Exception as err:
                if errors == 'warn':
                    print('Row:', rownumber, 'Bad row', row)
                    print('Reason', err)
                elif errors == 'raise':
                    raise # Re-raises the last exception
                else:
                    pass
            continue # skips to the next row
        #record = tuple(row)
        record = {
            'name' : row[0],
            'date' : row[1],
            'shares' : row[2],
            'price' : row[3]
        } 
        portfolio.append(record)
        print(row)
    return portfolio
""" files = glob.glob('Data/portfolio*.csv')
for file in files:
    data = file
    total = sev_files(data) """
portfolio = read_portfolio('Data/portfolio.csv')
total = 0.0
for holding in portfolio:
   total += holding['shares'] * holding['price'] # shares * price
print(portfolio)
# total = sev_files('Data/portfolio.csv', errors = 'silent')
print('Total cost=', total)
