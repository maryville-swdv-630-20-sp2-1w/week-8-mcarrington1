import random, string
from datetime import datetime
from abc import ABC, abstractmethod
from account import *
from orderhistory import *
from ordersubmitter import *

"""
This is an example of an abstract factory pattern.
The purpose of this class is to create order objects that are submitted via the web client.
"""
class OrderFactory(object):
    """
    This is a factory class to create different order types.
    """    
    def createCarryOutOrder(self, *args, **kwargs):
        return CarryOutOrder(*args, **kwargs)
    def createDeliveryOrder(self, *args, **kwargs):
        return DeliveryOrder(*args, **kwargs)
    def createVolumeOrder(self, *args, **kwargs):
        return VolumeOrder(*args, **kwargs)
    
class Order(ABC):
    """
    This is the abstract Order class that will extend to different orders.
    @params account - account object
    @params orderManifest - list of menuItems that are being ordered
    """
    def __init__(self, account, storeId):
        self.account = account
        self.orderManifest = []
        self.status = "PENDING"
        self.orderId = generateRandomOrderId()
        self.orderPlaced = generateTimeStamp()
        self.additionalServiceCost = 0
        self.paymentId = self.__generatePaymentId()
        self.storeId = storeId
        
    def __str__(self):
        return ('Account: {}, OrderManifest: {}, Status: {}, OrderId: {}, OrderPlaced: {}'
        .format(self.account, self.orderManifest, self.status, self.orderId, self.orderPlaced))
    
    def addOrderManifest(self, orderManifest):
        self.orderManifest = self.__convertOrderManifestToLiteral(orderManifest)
    
    def __convertOrderManifestToLiteral(self, orderManifest):
        return ', '.join(str(x) for x in orderManifest)
    
    def __generatePaymentId(self):
        lettersAndDigits = string.ascii_letters + string.digits
        paymentId = ''.join(random.choice(lettersAndDigits) for i in range(16))
        return paymentId
    
    def updateStatus(self, newStatus):
        self.status = newStatus
        
    def saveOrderHistory(self):
        engine = create_engine('sqlite:///:memory:', echo=False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        orderOne = OrderHistory(self.orderId, self.account.accountId, datetime.utcnow(), self.orderManifest)
        session.add(orderOne)
        session.commit()
        
        session.close()
                
    def submitOrder(self, account, password):
        submission = OrderSubmitter(self.paymentId, self.orderManifest, self.storeId,
                                    self.getOrderType(), account, password)
        isSubmissionSuccessful = submission.submitOrder()
        
        # Only saving history if it was successfully submitted!
        if (isSubmissionSuccessful):
            self.status = "RECEIVED"
            self.saveOrderHistory()
            
    def cloneOrder(self, orderId):
        engine = create_engine('sqlite:///:memory:', echo=False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        orderManifest = session.query(OrderHistory.itemsOrdered).filter_by(orderId=orderId).first()
        
        session.close()
        
        return orderManifest
        
    @abstractmethod
    def getOrderType(self):
        pass
    
    """
    These are additional service costs, depending on the order type.
    """
    @abstractmethod
    def calcAdditionalServiceCosts(self):
        pass

class DeliveryOrder(Order):
    
    def getOrderType(self):
        return "delivery"
    
    def calcAdditionalServiceCosts(self):
        self.additionalServiceCost += 4.99
        
class CarryOutOrder(Order):
    def getOrderType(self):
        return "carry-out"
    
    def calcAdditionalServiceCosts(self):
        self.additionalServiceCost += 0
    
class VolumeOrder(Order):
    def getOrderType(self):
        return "volume order"
    
    def calcAdditionalServiceCosts(self):
        self.additionalServiceCost += 3.99
        
def generateRandomOrderId():
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))

def generateTimeStamp():
    return datetime.now();       