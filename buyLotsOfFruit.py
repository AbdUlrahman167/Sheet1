# buyLotsOfFruit.py
# -----------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
To run this script, type

  python buyLotsOfFruit.py

Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:

Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
"""
from __future__ import print_function

fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}


def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples

    Returns cost of order
    """
    totalCost = 0.0
    "*** YOUR CODE HERE ***"
    for fruit, cost in orderList:
        if fruit not in fruitPrices:
            print("Sorry %s it doesn't exist" % (fruit))
            print("Edit your list,please")
            return None
        else:
            totalCost += cost * fruitPrices[fruit]

    
    return totalCost


# Main Method
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orderList = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]
    print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))
    
    
    
#if you wanna use input orders from user follow this code
'''
# create your orderList
n = int(input("No.kinds: "))
d = {}
for i in range(n):
    key = str(input("fruit: "))
    value = float(input("No.= "))
    d[key] = value
orderlist = list(d.items())
print("Your order is %s and its cost's" % (orderlist))

# following line depends on owner of shop
price_of_fruits = {'Apples': 20.00, 'Mango': 25.00, 'Oranges': 15.00,
                   'Banana': 15.00, 'Strawberries': 15.00, 'Clementine': 5.00}

# cal.its cost
def buy_lots_of_fruit(orderlist):
    cost = 0.0
    for key, value in orderlist:
        if key not in price_of_fruits:
            print("Sorry %s it doesn't exist" % (key))
            print("Edit your list,please")
            return None
        else:
            cost += value * price_of_fruits[key]

    return cost
print(buy_lots_of_fruit(orderlist))
'''
