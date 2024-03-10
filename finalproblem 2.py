
#problem 2
# name : zeyad Elsayed mahmoud yousef  /// ID :  20230153
#name: Abd elrahman Yasser Ewees      /// ID  : 20230221
#name :Abd allah mouhmed Ebrahem zrok  ///ID  :  20220631

#to addition two binary number

def add_num(num1, num2):
    carry = 0
    result = ""
    final = ""
    num1 = str(num1)
    num2=str(num2)
    if len(num1) >= len(num2):
        tall = len(num1)
        num1 = num1.zfill(tall)
        num2 = num2.zfill(tall)
    else:
        tall = len(num2)
    num1 = num1.zfill(tall)
    num2 = num2.zfill(tall)
    for i in range(tall - 1, -1, -1):
        digit = int(num1[i]) + int(num2[i]) + carry
        if digit == 1:
            carry = 0
            result = "1" + result
            final = str(carry) + result
        elif digit == 2:
            result = "0" + result
            carry = 1
            final = str(carry) + result

        elif digit == 0:
            result = "0" + result
            carry = 0
            final = str(carry) + result
        else:
            result = "1" + result
            carry = 1
            final = str(carry) + result

    return final

# To get one's complement
def sub_2num(num1,num2):
    sub=""
    borrow=0
    x=len(num1)
    y=len(num2)
    if x>=y:
        tall=x
        num1=num1.zfill(tall)
        num2=num2.zfill(tall)
    else:
        tall=y
        num1=num1.zfill(tall)
        num2=num2.zfill(tall)
    for i in range(tall-1,-1,-1):
        a=num1[i]
        b=num2[i]
        bit=int(a)-int(b)+borrow
        if bit==0:
            borrow=0
            sub="0"+sub
        elif bit==1:
            borrow=0
            sub="1"+sub
        elif bit==-1:
            borrow=-1
            sub="1"+sub
        elif bit==-2:
            borrow=-1
            sub="0"+sub

    return sub


def ones_compelment(num1):
    res = ""
    num1 = str(num1)
    for i in num1:
        if i == "0":
            res =res+"1"
        else:
            res =res+"0"
    return res
#to get twe's complement
def twe_complement(num1):
    res = int(ones_compelment(num1))
    res=str(res)
    num2="1"
    second_step = add_num(res,num2)
    return second_step
while True:
    first_choice = input("**binary calculator**\nA)Insert a new number \nB)exit program\n ").upper()
    if first_choice == "A":
        num1 = str(input("please insert the first  number\n "))
        while int(num1) >= 0:
            digit = int(num1) % 10
            if digit != 0 and digit != 1:
                num1 = int(input("invalid number "))
            else:
                secand_choice = input(
                    "**please select the operation**\nA)one's complement\nB)twe's complement\nC)addition\nD)subtractoin").upper()
                while secand_choice not in ["A", "B", "C", "D"]:
                    secand_choice = input("invalid choice \nplease select A,B,C or D")
                else:
                    if secand_choice == "A":
                        num1 = str(num1)
                        print(ones_compelment(num1))
                        break
                    elif secand_choice == "C":
                        num2=input("enter the second num")
                        num1=str(num1)
                        print(add_num(num1,num2))
                        break
                    elif secand_choice == "B":
                        print(twe_complement(num1))
                        break
                    else:
                         num2 = int(input("enter the second bainary number \n"))
                         num1 = int(num1)
                         if  num1> num2:
                             num1=str(num1)
                             num2=str(num2)
                             print(sub_2num(num1,num2))
                             break

                         else:
                             num2=input("invalid number enter a valid number \n")
                             print(sub_2num(num1,num2))
                             break

    elif first_choice != "A" and first_choice != "B":
        first_choice = ("please select A or B")
    else:
        print("Exit program")















