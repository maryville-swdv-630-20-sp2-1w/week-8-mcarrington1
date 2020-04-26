class StoreNotifier:
    """
    This will take an order object and use it to notify a store.
    """
    def __init__(self):
        self.isNotificationIsSuccessful = False
    
    def notifyStoreOfOrder(self, storeId, order):
        # Stub code here that would send a notification to the store
        print('Store {} has been notified with order manifest:{}'.format(storeId, order))
        
        # We would return an acknowledgement that it has been received here
        # Flipping to successful notification for the purposes of this stub
        self.isNotificationSuccessful = True
        if (self.isNotificationSuccessful):
            return True
        else:
            return False