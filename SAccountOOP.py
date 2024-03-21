class SAccount:
    def __init__(self, accNo, accNam, bal, maxAmt=500):
        self.__accNo = accNo
        self.__accNam = accNam
        self.__bal = bal
        self.__maxAmt = maxAmt


    def getSAccNo(self): #acc number
        return self.__accNo

    def getAccNam(self): #acc name 
        return self.__accNam

    def getBal(self): #get balance
        return self.__bal

    def Deposit(self, amount): #deposit class
            print("Transaction completed! Deposit recieved") 
            self.__bal += float(amount) #adds user input (amount) to balance
            self.__bal = round(self.__bal, 2) #rounds off to 2 decimal places 
            print("Balance: " + str(self.__bal)) #prints balance

    def Withdraw(self, amount): #withdraw function
        if float(amount) < self.__maxAmt: #maximum limit set, if withdraw amount is less than than, it will display an error message
            print("Withdrawal amount is less than the limit. Invalid transaction")
            print("Transaction failed")
            return False

        elif float(amount) > self.__bal: # if amount is less than balance, program will return an error message. cannot have negative money
            print("cannot withdraw! you do not have enough money.")
            print("Withdrawal failed.")
            return False

        else: 
            print("Transaction completed!") #if parameters above are both false, withdrawal will be successful. 
            self.__bal -= float(amount) #will minus user input (amount) to balance
            self.__bal = round(self.__bal, 2) #round it off to 2 decimal places
            print("Balance: " + str(self.__bal)) #display balance 
            return True

        

    def __str__(self): #information displayed when show information / show account information option is selected.
        return "Account Number: " + str(self.__accNo) + "\nAccount Name: " + str(self.__accNam) + "\nBalance: $" + str(self.__bal) + "\nMaximum Amount: " + str(self.__maxAmt)
