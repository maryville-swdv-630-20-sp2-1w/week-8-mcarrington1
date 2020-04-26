from datetime import datetime
from validatepayment import *
from storenotifier import *

class OrderSubmitter:
    '''
    Notify a store of an order. Store can directly query order details afterwards.
    '''

    def __init__(self, paymentId, orderManifest, storeId, orderType, account, password):
        self.orderManifest = orderManifest
        self.orderType = orderType
        self.storeId = storeId
        self.account = account
        self.password = password
        self.paymentId = paymentId
    
    def __performAccountAndPaymentValidation(self):
        accountValidationStatus = self.account.validatePassword(self.password)
        paymentValidationStatus = ValidatePayment(self.paymentId).authorize()
        return accountValidationStatus, paymentValidationStatus
                
    def submitOrder(self):
        if (self.__performAccountAndPaymentValidation()):
            StoreNotifier().notifyStoreOfOrder(self.storeId, self.orderManifest)
            return True
        else:
            print('Unable to submit order!')
            return False