from menuitem import *
from order import *
from account import *


# Normally a web UI would fill out this data for us and submit, Example Only.
def createOrderManifest():
    itemDrink = Drink("Pepsi", None, "Medium", 3.99, None)
    itemDrink.addExtraFlavor('chocolate')
    itemDrink.removeExtraFlavor()
    itemDrink.changeBrandName('Diet Pepsi')
    
    toppingsLeft = {'pepperoni': 'extra'}
    toppingsRight = {'jalapeno': 'light'}
    toppingsAll = {'roma tomatoes': 'regular'}
    itemPizza = Pizza('regular', toppingsLeft, toppingsRight, toppingsAll, 'deep dish', 'Large', 9.99, 'Well Done')
    itemPizza.addTopping('left', 'pineapple', 'light')
    itemPizza.removeTopping('all', 'roma tomatoes')
    
    itemAppetizer = Appetizer('mozzarella sticks', None, 'small', 1.99, None)
    itemAppetizer.changeAppetizerSauce('marinara sauce')
    
    return [itemDrink, itemPizza, itemAppetizer]

'''
Example of how a user can create an order, create an account, login, and submit the order.
'''
if __name__== '__main__':
    print('### Here is an example of a user ordering in the system ###')
    # Create the order manifest
    orderManifest = createOrderManifest()
    print(orderManifest)
    
    # User creates an account because they do not have one
    print('### User Creates Account ###')
    account = Account('matt','carrington','mjcarrington@icloud.com','3144946903','22 san camille ct. 63303','foo')
    print(account)
    
    # User now officially creates an Order
    print('### Creating Order ###')
    orderFactory = OrderFactory()
    carryoutOrder = orderFactory.createCarryOutOrder(account, 'R114')
    carryoutOrder.addOrderManifest(orderManifest)
    print(carryoutOrder)
    
    # validates pass and payment as part of submission
    print('### User Submits Order ###')
    carryoutOrder.submitOrder(account, 'foo2')