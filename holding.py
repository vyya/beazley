""" holding = {'name' : 'AA', 'date' : '21-09-2024', 'shares' : 100, 'price' : 100.53}
print(holding['name'])
print(holding['price'])

def cost(holding):
    return holding['shares'] * holding['price']

print(cost(holding)) """

class Holding(object):
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
    
    def sell(self, nshares):
        self.shares -= nshares
    
import csv
def read_portfolio(filename):
        portfolio = []
        with open(filename, 'r') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                 h = Holding(row[0], row[1], int(row[2]), float(row[3]))
                 portfolio.append(h)
        return portfolio
            
h = Holding('AOL', '2024-10-08', 200, 25.21)
h.sell(20)
print(h.cost(), h.shares)
portfolio = read_portfolio('Data/portfolio.csv')
total = 0
for h in portfolio:
     total += h.shares * h.price
print(total)
names = [h.name for h in portfolio]
print(names)