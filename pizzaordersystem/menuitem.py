class MenuItem:
    """
    The menu item class would ideally be a single item as part of a list for an "order".
    @params
    - size = this is the size of the menu item, e.g. medium, large
    - cost = this is the cost of the item, it would be driven by the system taking the input probably
    - specialInstructions = any instructions, such as sauce on the side, well done, etc.
    """
    def __init__(self, size, cost, specialInstructions=None):
        self.size = size # e.g. large, xl,
        self.cost = cost
        self.specialInstructions = specialInstructions
        
    def applyCoupon(self, discount):
        self.cost -= discount
        
    def addExtras(self, extraCost):
        self.cost += extraCost
        
class Drink(MenuItem):
    """
    The drink class inherits the MenuItem class.
    @params
    - brandName = e.g. Coke, Diet Coke, Pepsi
    - extraFlavor = Vanilla, Chocolate, Cherry
    """
    def __init__(self, brandName, extraFlavor, *args, **kwargs):
        self.brandName = brandName
        self.extraFlavor = extraFlavor
        super(Drink, self).__init__(*args, **kwargs)
        
    def __str__(self):
        return ('Drink: \n *Brand: {} \n *Flavor: {} \n *Size: {} \n *Special Instructions: {} \n *Cost: {}'
              .format(self.brandName, self.extraFlavor, self.size, self.specialInstructions, self.cost))
    
    def __repr__(self):
        return ('Size:{},Cost:{},SpecialInstructions:{},brandName:{},extraFlavor:{}'
            .format(self.size, self.cost, self.specialInstructions, self.brandName, self.extraFlavor))        
        
    def changeBrandName(self, newBrandName):
        self.brandName = newBrandName
    
    def addExtraFlavor(self, newFlavorName):
        self.extraFlavor = newFlavorName
       
    def removeExtraFlavor(self):
        self.extraFlavor = None
        
class Pizza(MenuItem):
    """
    The Pizza class inherits the MenuItem class.
    @params
    - cheeseAmount = amount of cheese
    - toppingsLeft = a dict that with K = topping name and V = amount
    - toppingsRight = a dict that with K = topping name and V = amount
    - toppingsAll = a dict that with K = topping name and V = amount
    - crustType = e.g. deep dish, NY style
    """    
    def __init__(self, cheeseAmount, toppingsLeft, toppingsRight, toppingsAll, crustType, *args, **kwargs):
        self.cheeseAmount = cheeseAmount
        self.toppingsLeft = toppingsLeft
        self.toppingsRight = toppingsRight
        self.toppingsAll = toppingsAll
        self.crustType = crustType
        super(Pizza, self).__init__(*args, **kwargs)
        
    def addTopping(self, toppingSide, toppingIngredient, toppingAmount):        
        self.__selectPizzaSideByName(toppingSide)[toppingIngredient] = toppingAmount
            
    def removeTopping(self, toppingSide, toppingIngredient):
        try:
            del self.__selectPizzaSideByName(toppingSide)[toppingIngredient]
        except KeyError:
            print("Topping {} on pizza side {} not found!".format(self.toppingIngredient, self.toppingSide))
        
    def __selectPizzaSideByName(self, toppingSide):
        toppingSide = toppingSide.lower()
        
        if toppingSide == 'left':
            return self.toppingsLeft
        elif toppingSide == 'right':
            return self.toppingsRight
        elif toppingSide == 'all':
            return self.toppingsAll
        else:
            print('no valid side provided (left/right/all)! Defaulting to all.')
            return self.toppingsAll
            
    def __str__(self):
        toppingLeftContents = ",".join((" {} ({})".format(*i) for i in self.toppingsLeft.items()))
        toppingRightContents = ",".join((" {} ({})".format(*i) for i in self.toppingsRight.items()))
        toppingsAllContents = ",".join((" {} ({})".format(*i) for i in self.toppingsAll.items()))
        
        return('Pizza: \n *Size: {} \n *Cheese Amount: {} \n *Crust Type: {} \n *Cost: {} \n *Special Instructions: {} \n *Left Toppings: {} \n *Right Toppings: {} \n *Left+Right Toppings: {}'
              .format(self.size, self.cheeseAmount, self.crustType, self.cost, self.specialInstructions, toppingLeftContents, toppingRightContents, toppingsAllContents))
    
    def __repr__(self):
        return ('Size:{},Cost:{},SpecialInstructions:{},cheeseAmount:{},toppingsLeft:{},toppingsRight:{},toppingsAll:{},crustType:{}'
            .format(self.size, self.cost, self.specialInstructions, self.cheeseAmount,
                    self.toppingsLeft, self.toppingsRight, self.toppingsAll, self.crustType))        
               
class Appetizer(MenuItem):
    """
    The appetizer class inherits the MenuItem class.
    @params
    - appetizerType = actual name of the appetizer
    - extraFlavor = Side sauce
    """
    def __init__(self, appetizerType, sauceType, *args, **kwargs):
        self.appetizerType = appetizerType
        self.sauceType = sauceType
        super(Appetizer, self).__init__(*args, **kwargs)
        
    def __str__(self):
        return ('Appetizer: \n *Type: {} \n *Sauce: {} \n *Size: {} \n *Special Instructions: {} \n *Cost: {}'
            .format(self.appetizerType, self.sauceType, self.size, self.specialInstructions, self.cost))
    
    def __repr__(self):
        return ('Size:{},Cost:{},SpecialInstructions:{},AppetizerType:{},SauceType:{}'
            .format(self.size, self.cost, self.specialInstructions, self.appetizerType, self.sauceType))
        
    def changeAppetizerType(self, newAppetizerType):
        self.appetizerType = newAppetizerType
    
    def changeAppetizerSauce(self, newSauceType):
        self.sauceType = newSauceType