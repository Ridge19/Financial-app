class CAccount:
    def __init__(self, accNo, accNam, bal, minAmt=50):
        self.__accNo = accNo
        self.__accNam = accNam
        self.__bal = bal
        self.__minAmt = minAmt


    def getCAccNo(self): #getter for CAccount Number
        return self.__accNo

    def getAccNam(self): #getter for Account Name 
        return self.__accNam

    def getBal(self): #getter for balance 
        return self.__bal

    def Deposit(self, amount): #Deposit function
            print("Transaction completed! deposit recieved")
            self.__bal += float(amount) #Adds deposit to balance 
            self.__bal = round(self.__bal, 2) #rounds it off by 2
            print("Balance: " + str(self.__bal)) #displays NEW balance 

    def Withdraw(self, amount): #Withdraw function
        if float(amount) < self.__minAmt: #minimum amount for deposit is defined as 50. if less than, program will return error (Transaction failed)
            print("Deposit amount is less than minimum amount! invalid transaction")
            print("Transaction failed")
            return False
            
        elif float(amount) > self.__bal: #if amount is greater than balance, withdrawal will fail.  
            print("cannot withdraw! you do not have enough money.")
            print("withdrawal failed.")
            return False

        else:
            print("Transaction completed!") #if bigger than 50, program will accept transaction and will print in reciept. 
            self.__bal -= float(amount)
            self.__bal = round(self.__bal, 2)
            print("Balance: " + str(self.__bal))
            return True

    def __str__(self): #what program displays when getter function is called (show account information / show information)
        return "Account Number: " + str(self.__accNo) + "\nAccount Name: " + str(self.__accNam) + "\nBalance: $" + str(self.__bal) + "\nMinimum Amount: " + str(self.__minAmt)