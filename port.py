import csv
total = 0.0
with open('Data/portfolio3.csv', 'r') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        """ line = line.strip() # strip whitespace off
        parts = line.split(',')
        parts[0] = parts[0].strip('"')
        parts[1] = parts[1].strip('"') """
        row[2] = int(row[2])
        row[3] = float(row[3])
        total += row[2] * row[3]
        print(row)
    print('Total cost=', total)
