import csv
import glob
def sev_files(filename):
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
            except ValueError as err:
                print('Row:', rownumber, 'Bad row', row)
                print('Reason', err)
                continue # skips to the next row  
            total += row[2] * row[3]
            print(row)
    return total
""" files = glob.glob('Data/portfolio*.csv')
for file in files:
    data = file
    total = sev_files(data) """
total = sev_files('Data/missing.csv')
print('Total cost=', total)
