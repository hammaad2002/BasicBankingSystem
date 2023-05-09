import os,time
class bank(object):
    def __initi__(self,acc=None,new_bal=0,data= None):
        self.data = data
        self.acc = acc
        self.new_balance = new_bal
    def login (self,data,acc):
        self.data = data
        self.acc = acc
        for i in range(0,len(data),2):
            temp = data[i]
            temp = temp[:-1]
            if self.acc == temp:
                return True
    def bal_print(self,data,acc):
        self.data = data
        self.acc = acc
        for i in range(0,len(data),2):
            temp = data[i]
            temp = temp[:-1]
            if self.acc == temp:
                print("Your balance is:",self.data[i+1])
    def bal_check(self,data,acc):
        self.data = data
        self.acc = acc
        for i in range(0,len(data),2):
            temp = data[i]
            temp = temp[:-1]
            if self.acc == temp:
                return self.data[i+1]
    def update_balance (self,data,acc,new_bal,filename):
        self.data = data
        self.acc = acc
        self.new_balance = new_bal
        for i in range(0,len(data),2):
            temp = data[i]
            temp = temp[:-1]
            if self.acc == temp:
                temp2 = open(filename,'r')
                temp3 =temp2.readlines()
                temp3[i+1] = new_bal
                temp2 = open(filename,'w')
                temp2.writelines(temp3)
                temp2.close()
                break
    def register (self,acc,new_bal,filename):
        self.acc = acc
        self.new_balance = new_bal
        temp = open(filename,'a')
        temp.write(self.acc+'\n')
        temp.write(self.new_balance+'\n')
        temp.close()
    def file_search(self,filename):
        for root, dirs, files in os.walk(os.getcwd()):
            if filename in files:
                return True
            else:
                return False

#calling bank class from here

ins_1 = bank()
file_name = 'Bank.txt'
if ins_1.file_search(file_name) == False:
    file_1 = open(file_name,'w+')
    falseAcc = 'xyz'
    falseBal  = '123'
    file_1.write(falseAcc+'\n')
    file_1.write(falseBal+'\n')
    file_1.close()
    file_1 =open(file_name,'r')
elif ins_1.file_search(file_name) == True :
    file_1 = open (file_name,'r')
data = file_1.readlines()
print("****BANK****")
acc = str(input("Enter account name: "))
if ins_1.login (data,acc) == True:
    ins_1.bal_print(data,acc)
else:
    print("You are not registered in this bank.")
    inp = str(input("Do you want to register ?(y/n): "))
    if inp == 'y':
        acc = str(input("Enter your account name: "))
        new_bal = int(input("Enter your balance :"))
        ins_1.register(acc,str(new_bal),file_name)
        print("Account registered")
    elif inp == 'n':
        exit()
    else:
        print("Wrong input exiting program in 3 seconds ...")
        time.sleep(3)
        exit()
balance = str(input("Do you want to withdraw from your account ?(y/n): "))
file_1.close()
file_1 = open(file_name,'r')
data = file_1.readlines()
if balance =='y':
    new_bal = int(input("Enter the amount you want to withdraw: "))
    temp = int(ins_1.bal_check(data,acc))
    if new_bal > temp:
        print ("You cannot withdraw amount greater than what you have. You only have ",ins_1.bal_check(data,acc),' in your account.')
    else:
        temp2 = temp - new_bal
        ins_1.update_balance(data,acc,str(temp2)+'\n',file_name)
        print('Balance Updated. Your new balance is Rs:',temp2)
elif balance =='n':
    balance_2 = str(input("Do you want to deposit in your bank account ?(y/n) :"))
    if balance_2 == 'y':
        new_bal = int(input("Enter the amount you want to deposit: "))
        temp = int(ins_1.bal_check(data,acc))
        temp2 = temp + new_bal
        ins_1.update_balance(data,acc,str(temp2)+'\n',file_name)
        print('Balance Updated. Your new balance is Rs:',temp2)
    elif balance_2 == 'n':
        quit()
    else:
        print ("Wrong input exiting program in 3 seconds ...")
        time.sleep(3)
        exit()
else:
    print(" Wrong input exiting program in 3 seconds ...")
    time.sleep(3)
    exit()
    


'''filename = 'hammad.txt'
read = open(filename,'r')
data = read.readlines()
print(data)
var = 'Ali Aman'
for i in range (0,len(data),3):
    temp = data[i]
    temp = temp[:-1]
    if temp == var :
        print("Searched"+str('123')+"moeed in index position",i)

data[0] = 'hahaha\n'
read = open(filename,'w')
read.writelines(data)
read.close()'''
