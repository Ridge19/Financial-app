from SAccountOOP import SAccount #importing the SAccount class from SAccount OOP
from CAccountOOP import CAccount #importing the CAccount class from CAccountOOP
import re #string search library 


class Bank: #bank class (main class)
    def __init__(self):
        self.__CAccount = []
        self.__SAccount = []
        self.__accIdx = -1
        self.__accObj = None

    def loadSAccount(self):
        fr = open("C:/Users/Ridge/Downloads/Maxdora-Fianancial-S3934367-Ridge-FINAL/Python Assignment 02/CAccounts.txt", "r") #will read SAccounts text file 

        for f in fr:
            f = f.rstrip("\n")
            temp = f.split(";") #will check for ';' and will display in a new line 

            if len(temp) == 3: 
                s = SAccount(int(temp[0]), temp[1], float(temp[2]), maxAmt=500)
                self.__SAccount.append(s)
            else:
                s = SAccount(int(temp[0]), temp[1], float(temp[2]), float(temp[3]))
                self.__SAccount.append(s)

        fr.close()

    def loadCAccount(self):
        fr = open("C:/Users/Ridge/Downloads/Maxdora-Fianancial-S3934367-Ridge-FINAL/Python Assignment 02/CAccounts.txt", "r") #will read CAccounts text file

        for f in fr:
            f = f.rstrip("\n")
            temp = f.split(";")

            if len(temp) == 3:
                c = CAccount(int(temp[0]), temp[1], float(temp[2]))
                self.__CAccount.append(c)
            else:
                c = CAccount(int(temp[0]), temp[1], float(temp[2]), float(temp[3]))
                self.__CAccount.append(c)

        fr.close()

    def menu(self): #main menu, what users sees when they open the application 
        while True:
            print("======== MAXDORA FINANCIAL - MAIN MENU ========")
            print("1. Enter Checking account number")
            print("2. Enter Saving account number")
            print("3. Display Checking Account information")
            print("4. Display Saving Account information")
            print("5. Exit application")
            print("===================================")
            opt = input("Select Option: ")

            if opt == "1":
                accNo = input("Enter Checking Account Number: ")

                if not accNo.isdigit():
                    print("Invalid input entered for Checking Account Number. Try again")
                    self.menu()

                self.__accIdx = self.getCAccount(accNo)

                if self.__accIdx != -1:
                    self.checkingMenu() #if option entered is valid, checking menu function will run 
                else:
                    print("Account does not exist, try again")
            elif opt == "2":
                accNo = input("Enter Saving Account Number: ")

                if not accNo.isdigit():
                    print("Invalid input entered for Saving Account Number. Try again.")
                    self.menu()

                self.__accIdx = self.getSAccount(accNo)

                if self.__accIdx != -1:
                    self.savingMenu()
                else:
                    print("Account does not exist, try again")
            elif opt == "3": #this option displays information from the txt file, seperated by * characters. runs in a for loop until all information is displayed.
                print("==== Checking Account ====")
                for c in self.__CAccount:
                    print(c)
                    print("********")
            elif opt == "4":
                print("==== Saving Account ====")
                for s in self.__SAccount:
                    print(s)
                    print("********")
            elif opt == "5":
                print("Exiting application! Thankyou! :)")
                exit()
            else:
                print("Invalid option, try again")

    def checkingMenu(self): #checking menu
        self.__accObj = self.__CAccount[self.__accIdx]

        while True:
            print("======== CHECKING MENU ========")
            print("======== " + (str(self.__accObj.getAccNam())) + " " + str(self.__accObj.getCAccNo()) + " ========")
            print("1. Enter Deposit amount")
            print("2. Enter Withdrawal amount")
            print("3. Display current balance")
            print("4. Account details")
            print("5. Back to main menu")
            opt = input("select Option: ")

            if opt == "1": #deposit
                amount = input("Enter Deposit Amount: $")

                if re.search("^[0-9]+\.*[0-9]*$", amount):
                    self.__accObj.Deposit(amount)
                    self.__CAccount[self.__accIdx] = self.__accObj
                    fw = open("C:\\Users\\Ridge\\Downloads\\Maxdora-Fianancial-S3934367-Ridge-FINAL\\Python Assignment 02\\AccountReceipt.txt", "w") #prints reciept to text file named AccountReciept.txt 
                    fw.write("======== MAXDORA FINANCIAL ========")
                    fw.write("\nAccount number: " + str(self.__accObj.getCAccNo()))
                    fw.write("\nAccount Name: " + str(self.__accObj.getAccNam()))
                    fw.write("\nDeposit Amount: $" + amount)
                    fw.write("\nCurrent Balance: $" + str(self.__accObj.getBal()))
                    print("\nReciept printed. Thankyou") #confirmation message that reciept is printed. 
                    fw.close() 
                else:
                    print("Invalid input entered for deposit amount")
                    print("deposit failed.")
            elif opt == "2": #withdrawal
                amount = input("Enter Withdrawal Amount: $")

                if re.search("^[0-9]+\.*[0-9]*$", amount):
                    self.__accObj.Withdraw(amount)
                    self.__CAccount[self.__accIdx] = self.__accObj
                    fw = open("C:\\Users\\Ridge\\Downloads\\Maxdora-Fianancial-S3934367-Ridge-FINAL\\Python Assignment 02\\AccountReceipt.txt", "w")
                    fw.write("======== MAXDORA FINANCIAL ========")
                    fw.write("\nAccount number: " + str(self.__accObj.getCAccNo()))
                    fw.write("\nAccount Name: " + str(self.__accObj.getAccNam()))
                    fw.write("\nWithdraw Amount: $" + amount)
                    fw.write("\nCurrent Balance: $" + str(self.__accObj.getBal()))
                    fw.close()
                    print("\nReciept printed. Thankyou")
                else:
                    print("Invalid input entered for withdrawal amount")
                    print("withdrawal failed.")
            elif opt == "3": #show balance 
                amount = input("Current Balance: $" + str(self.__accObj.getBal()))
                self.__accObj.getBal()
                self.__CAccount[self.__accIdx] = self.__accObj
                fw = open("C:\\Users\\Ridge\\Downloads\\Maxdora-Fianancial-S3934367-Ridge-FINAL\\Python Assignment 02\\AccountReceipt.txt", "w")
                fw.write("======== MAXDORA FINANCIAL ========")
                fw.write("\nAccount number: " + str(self.__accObj.getCAccNo()))
                fw.write("\nAccount Name: " + str(self.__accObj.getAccNam()))
                fw.write("\nCurrent Balance: $" + str(self.__accObj.getBal()))
                fw.close()
                print("\nReciept Printed. Thankyou")
            elif opt == "4": #display account details / information
                print("======== ACCOUNT DETAILS: ========")
                print(self.__CAccount[self.__accIdx])
            elif opt == "5":
                self.menu()
            else:
                print("Invalid option selected. Try again")

    def savingMenu(self): #saving menu function
        self.__accObj = self.__SAccount[self.__accIdx]

        while True:
            print("======== SAVING MENU ========") 
            print("======== " + (str(self.__accObj.getAccNam())) + " " + str(self.__accObj.getSAccNo()) + " ========")
            print("1. Enter Deposit amount")
            print("2. Enter Withdrawal amount")
            print("3. Display current balance")
            print("4. Account information")
            print("5. Back to main menu")
            opt = input("select Option: ")

            if opt == "1": #deposit 
                amount = input("Enter Deposit Amount: $")

                if re.search("^[0-9]+\.*[0-9]*$", amount):
                    self.__accObj.Deposit(amount)
                    self.__SAccount[self.__accIdx] = self.__accObj
                    fw = open("C:\\Users\\Ridge\\Downloads\\Maxdora-Fianancial-S3934367-Ridge-FINAL\\Python Assignment 02\\AccountReceipt.txt", "w")
                    fw.write("======== MAXDORA FINANCIAL ========")
                    fw.write("\nAccount number: " + str(self.__accObj.getSAccNo()))
                    fw.write("\nAccount Name: " + str(self.__accObj.getAccNam()))
                    fw.write("\nDeposit Amount: $" + amount)
                    fw.write("\nCurrent Balance: $" + str(self.__accObj.getBal()))
                    fw.close()
                    print("\nReciept printed. Thankyou")
                else:
                    print("Invalid input entered for deposit amount")
                    print("deposit failed.")
            elif opt == "2": #withdrawal 
                amount = input("Enter Withdrawal Amount: $")

                if re.search("^[0-9]+\.*[0-9]*$", amount):
                    self.__accObj.Withdraw(amount)
                    self.__SAccount[self.__accIdx] = self.__accObj
                    fw = open("C:\\Users\\Ridge\\Downloads\\Maxdora-Fianancial-S3934367-Ridge-FINAL\\Python Assignment 02\\AccountReceipt.txt", "w")
                    fw.write("======== MAXDORA FINANCIAL ========")
                    fw.write("\nAccount number: " + str(self.__accObj.getSAccNo())) 
                    fw.write("\nAccount Name: " + str(self.__accObj.getAccNam()))
                    fw.write("\nWithdraw Amount: $" + amount)
                    fw.write("\nCurrent Balance: $" + str(self.__accObj.getBal()))
                    fw.close()
                    print("\nReciept Printed. Thankyou.")
                else:
                    print("Invalid input entered for withdrawal amount")
                    print("withdrawal failed.")
            elif opt == "3": #display current balance 
                amount = input("Current Balance: $" + str(self.__accObj.getBal()))

                if re.search("^[0-9]+\.*[0-9]*$", amount):
                    self.__accObj.getBal()
                    self.__SAccount[self.__accIdx] = self.__accObj
                    fw = open("C:\\Users\\Ridge\\Downloads\\Maxdora-Fianancial-S3934367-Ridge-FINAL\\Python Assignment 02\\AccountReceipt.txt", "w")
                    fw.write("======== MAXDORA FINANCIAL ========")
                    fw.write("\nAccount number: " + str(self.__accObj.getSAccNo()))
                    fw.write("\nAccount Name: " + str(self.__accObj.getAccNam()))
                    fw.write("\nCurrent Balance: $" + str(self.__accObj.getBal()))
                    print("\nReciept printed. Thankyou")
                    fw.close()
            elif opt == "4": #show account details 
                print("======== ACCOUNT DETAILS: ========")
                print(self.__SAccount[self.__accIdx])
            elif opt == "5":
                self.menu()
            else:
                print("Invalid option selected. Try again")

    #getter class for CAccount and SAccount so that parameters arent undefined 
    def getCAccount(self, accNo):
        for c in self.__CAccount:
            if int(accNo) == c.getCAccNo():
                return self.__CAccount.index(c)

        return -1

    def getSAccount(self, accNo):
        for s in self.__SAccount:
            if int(accNo) == s.getSAccNo():
                return self.__SAccount.index(s)

        return -1

    #function runs loading for both accounts and menu
    def main(self):
        self.loadSAccount()
        self.loadCAccount()
        self.menu()

#runs main class which is named 'Bank' 
bank = Bank()
#after bank class is executed, main class is executed next. 
bank.main()
