
# name : zeyad Elsayed mahmoud yousef  /// ID :  20230153
#name: Abd elrahman Yasser Ewees      /// ID  : 20230221
#name :Abd allah mouhmed Ebrahem zrok  ///ID  :  20220631

# octal to binary
def oct_bin(num):
    num_revers=num[::-1]
    bin=""
    for i in num_revers:
        if i =="0":
            bin="000"+bin
        elif i=="1":
            bin="001"+bin
        elif i=="2" :
            bin="010"+bin
        elif i=="3":
            bin="011"+bin
        elif i=="4" :
            bin="100"+bin
        elif i=="5":
            bin="101"+bin
        elif i=="6" :
            bin="110"+bin
        elif i=="7":
            bin="111"+bin
    return bin
# hexadicimal to binary
def hex_bin(num):
    num_revers=num[::-1]
    bin=""
    for i in num_revers:
        if i=="0":
            bin="0000"+bin
        elif i=="1":
            bin="0001"+bin
        elif i=="2" :
            bin="0010"+bin
        elif i=="3":
            bin="0011"+bin
        elif i=="4" :
            bin="0100"+bin
        elif i=="5":
            bin="0101"+bin
        elif i=="6":
            bin= "0110"+bin
        elif i=="7":
            bin="0111"+bin
        elif i=="8" :
            bin="1000"+bin
        elif i=="9" :
            bin="1001"+bin
        elif i== "A" or i=="a"  :
            bin="1010"+bin
        elif i=="B" or i=="b":
            bin="1011"+bin
        elif i=="C" or i=="c"  :
            bin="1100"+bin
        elif i=="D" or i=="d":
            bin="1101"+bin
        elif i=="E" or i=="e" :
            bin="1110"+bin
        elif i=="F"  or i=="f" :
            bin="1111"+bin
    return bin
# binary to octal
def bin_oct(num):
    oct=""
    while num>0:
        rem=num%1000
        rem=str(rem)
        if rem=="0" or rem=="00" or rem=="000":
            oct="0"+oct
        elif rem=="1" or rem=="01" or rem=="001":
            oct="1"+oct
        elif rem=="10" or rem=="010":
            oct="2"+oct
        elif rem=="11"  or rem=="011":
            oct="3"+oct
        elif rem=="100" :
            oct="4"+oct
        elif rem=="101":
            oct="5"+oct
        elif rem=="110":
            oct="6"+oct
        elif rem=="111" :
            oct="7"+oct
        num=num//1000
    if oct :
        return oct
    else:return"0"
#dicimal to hexadicimal

def dic_hex(num):
    hex =""
    while num >0:
        rem = num %16
        if rem==10:
            hex= "A"+hex
        elif rem == 11:
            hex = "B"+hex
        elif rem == 12:
            hex = "C"+hex
        elif rem == 13:
            hex ="D"+hex
        elif rem == 14:
            hex = "E"+hex
        elif rem ==15:
            hex = "F"+hex
        else:hex = str(rem)+hex
        num = num //16
    if hex:
        return hex
    else: return "0"
#octal to dicimal
def oct_dic(num):
    dic=0
    i=0
    while num>0 :
        digit= num%10
        dic = dic +digit*(8**i)
        i+=1
        num//=10
    if dic :
        return dic
    else:return"0"
# binary to dicimal
def bin_dic(num):
    dic=0
    i=0
    while num >0:
        digit = num %10
        dic = dic +digit*(2**i)
        i+=1
        num = num//10
    if dic :
        return dic
    else:return"0"
#dicimal to binary
def dic_bin (num):
    bin =""
    while num >0 :
        rem = num %2
        bin = str(rem)+ bin
        num = num//2
    if bin :
        return bin
    else:return "0"
# decimal to octal
def dic_oct(num):
    oct=""
    while num >0 :
        rem = num % 8
        oct = str(rem)+oct
        num = num //8
    if oct :
        return oct
    else : return "0"
#binary to hexadicimal
def bin_hex(num):
    res= int(bin_dic(num))
    hex =dic_hex(res)
    if hex:
        return hex
    else:return"0"
#octal to hexadicimal
def oct_hex(num):
    res = int(oct_dic(num))
    hex = dic_hex(res)
    if hex :
        return hex
    else :return"0"
#hexadicimal to dicimal
def hex_dic(num):
    hex=0
    z= len(num)
    i = z - 1
    y=0
    x=0
    digit= num[x]
    for digit in num:
        if digit == "A" or digit=="a" :
            y=10
        elif digit=="B"  or digit=="b" :
            y = 11
        elif digit == "C" or digit=="c":
            y = 12
        elif digit == "D" or digit=="d":
            y=13
        elif digit == "E" or digit=="e" :
            y = 14
        elif digit == "F" or digit =="f":
            y = 15
        else:y = int(digit)
        y = int(y)
        hex = hex + y*(16**i)
        i=i-1
        x=x+1
    if hex :
        return hex
    else:return"0"
#hexadicimal to octal
def hex_oct(num):
    res = hex_dic(num)
    res =int(res)
    hex = int(dic_oct(res))
    if hex:
        return hex
    else:return"0"
first_choice=input("**numbring system cnverter **\nA)Insert a new number \nB)exit program\n please enter your choice \n").upper()
while first_choice=="B":
    print("Exit program")
    first_choice=input("**numbring system cnverter **\nA)Insert a new number \nB)exit program\n please enter your choice \n").upper()
while first_choice not in ["A","B"]:
    first_choice=input("invalid choice piease select A or B\n").upper()

    if first_choice in["A","B"]:

      break
while first_choice=="A":

    num = (input("please inser the number\n"))

    base_from = input(
        "please select the base you want to convert thr number from\nA)Desmal\nB)Binary\nc)Octal\nD)Hexadesmal\nplease enter your choice [a,b,c,d]\n").upper()

    base_to = input(
        "please select the base you want to convert thr number to\n\A)Desmal\nB)Binary\nc)Octal\nD)Hexadesmal\nplease enter your choice [a,b,c,d]\n").upper()
    break
if base_from == "A" and base_to== "B":
   num = int(num)
   print (dic_bin(num))
elif base_from=="A" and base_to=="C":
    num=int(num)
    print(dic_oct(num))
elif base_from=="A"and base_to=="D":
    num=int(num)
    print(dic_hex(num))
elif base_from  =="B" and base_to=="A":
    num=int(num)
    print(bin_dic(num))
elif  base_from=="B" and base_to=="C":
    num=int(num)
    print(bin_oct(num))
elif  base_from =="B" and base_to=="D":
    num=int(num)
    print(bin_hex(num))
elif base_from =="C" and base_to=="A":
    num=int(num)
    print(oct_dic(num))
elif base_from=="C" and base_to =="B":
    print(oct_bin(num))
elif base_from=="C"  and base_to=="D":
    num=int(num)
    print(oct_hex(num))
elif base_from=="D" and base_to =="A":
    num=str(num)
    print(hex_dic(num))
elif  base_from=="D"  and base_to=="B":
    num=str(num)
    print(hex_bin(num))
elif base_from  =="D" and base_to=="C":
    num=str(num)
    print(hex_oct(num))
else:
    print(num)

print("Exit program")




