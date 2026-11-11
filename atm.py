class atmex:
   def __init__(self,pin,balance):
      self.pin=pin
      self.balance=balance
   def checkbalance(self):
      print(self.balance)
   def withdraw(self,wamnt):
      if self.balance>wamnt:
         self.balance-=wamnt
         print("it is withdrawn successfully")
      else:
         print("it is not written successfully")
         self.checkbalance()
   def deposit(self):
      damnt=int(input("enter the deposit amount:"))
      self.balance+=damnt
      print("it is deposited successfully")
      self.checkbalance()
   def validatepin(self):
      attempt=3
      while attempt>0:
         enteredpin=int(input("enter the 4 digit pin:"))
         if enteredpin==self.pin:
            print("it is validated")
            return True
         else:
            attempt-=1
            print("it is not validated")
      return False
      print("you are attempted too many steps")
   def run(self):
      if not self.validatepin():
         return
      while True:
            print("atm machine")
            print("1.check balance")
            print("2.withdraw amount")
            print("3.deposit amount")
            print("4.exit")
            choice=int(input("enter your choice:"))
            if choice==1:
               print(self.balance)
            elif choice==2:
               wamnt=int(input("enter the withdraw amount:"))
               self.withdraw(wamnt)
            elif choice==3:
               self.deposit()
            elif choice==4:
               print("exit")
               break
            else:
               print("invalid")
a=atmex(1234,1000)
a.run()
