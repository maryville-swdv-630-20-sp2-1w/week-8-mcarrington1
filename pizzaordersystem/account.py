import string, random


class Account:
    """
    This is designed to be a base user account for a customer.
    """
    def __init__(self, firstName, lastName, email, phone, address, password):
        self.accountId = self.generateAccountId()
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.address = address
        self.orderHistory = []
        self.__password = password
        self.__isLocked = False
        self.__isTemporaryPassword = False
        self.__isVerified = False
        
    def __str__(self):
        return ('First Name: {}, Last Name: {}, Email: {}, Phone: {}, Address: {}, OrderHistory: {}'
                .format(self.firstName, self.lastName, self.email, self.phone, self.address,self.orderHistory))
    
    def __repr__(self):
        return ('firstName:{},lastName:{},email:{},phone:{},address:{},orderHistory{}:password:{},isLocked:{},temporaryPassword:{}'
                .format(self.firstName, self.lastName, self.email, self.phone, self.address,
                self.orderHistory, self.__password, self.__isLocked, self.__temporaryPassword))
    
    def validatePassword(self, attemptedPassword):
        if attemptedPassword == self.__password:
            return True
        else:
            return False
        
    def generateAccountId(self):
        return ''.join(random.choice(string.digits) for i in range(12))
        
    def generateRandomPassword(self):
        lettersAndDigits = string.ascii_letters + string.digits
        temporaryPassword = ''.join(random.choice(lettersAndDigits) for i in range(12))
        return temporaryPassword
    
    def changePassword(self, currentPassword, newPassword):
        if self.validatePassword(currentPassword):
            self.__password = newPassword
            print('Password Updated!')
            return True
        else:
            print('Initial Password is incorrect, Unable to change pass!')
            return False
            
    def verifyAccount(self, password):
        if self.validatePassword(password):
            self.__isVerified = True
        else:
            print('Unable to verify, password incorrect!')
    
    def resetPassword(self, email):
        self.__temporaryPassword = True
        # Stubbed code here that would send an email with a new temporary pass
        return self.__generateRandomPassword()
        
    def changeAccountLockStatus(self, isAccountLocked):
        self.__isLocked = isAccountLocked