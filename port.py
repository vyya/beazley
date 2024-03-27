#!/usr/bin/env python3
total_cost = 0.0
with open('Data/portfolio.csv', 'r') as f:
    omit = next(f)
    for line in f:
        line = line.strip() #strip whitespaces
        line = line.split(',') 
        """ split line by comma delimeter creates set of
        lists """
        line[0] = line[0].strip('"')
        line[1] = line[1].strip('"') # get rid of quotation marks
        line[2] = int(line[2])
        line[3] = float(line[3]) #convert string to integer
        total_cost += line[2] * line[3]
        print(line)
    print(f'Total cost of all shares is {total_cost}')