with open('Data/portfolio.csv', 'r') as f:
    for line in f:
        line = line.strip() #strip whitespaces
        print(line)