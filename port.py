import csv
import glob
def sev_files(filename, *, errors = 'warn'):
    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("Errors must be one of 'warn', 'silent', 'raise'")
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
        total += row[2] * row[3]
        
    return total
""" files = glob.glob('Data/portfolio*.csv')
for file in files:
    data = file
    total = sev_files(data) """
total = sev_files('Data/missing.csv', errors = 'silent')
print('Total cost=', total)
