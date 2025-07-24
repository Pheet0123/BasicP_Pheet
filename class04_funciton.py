# def hello ():
#     print("Hello")

# hello()

# def hello(name):
#     print(name)
# name = input()
# hello(name)

# def hello(name):
#     print("ค่าที่รับมา",name)
# name = input()
# hello(name)

# def sum(a,b):
#     result = a+b 
#     print(result)

# num1 = int(input("กรอกเลขที่ 1"))
# num2 = int(input("กรอกเลขที่ 2"))

# def sum(a,b):
#     result = a+b 
#     return result

# num1 = int(input("กรอกเลขที่ 1"))
# num2 = int(input("กรอกเลขที่ 2"))

# result = sum(num1,num2)
# print(result)

# def add(num1,num2):
#     result = num1 + num2
#     return result

# def main():
#     num1 = int(input("กรอกเลขตัวที่ 1 "))
#     num2 = int(input("กรอกเลขตัวที่ 2 "))
#     result = add(num1,num2)
#     print("ผลลัพจากการบวกคือ:", result)
# main()


# wordshop

def add(num1,num2):
   result = num1 + num2
   return result

def minus(num1,num2):
    result = num1 - num2
    return result

def mutiple(num1,num2):
    result = num1 * num2
    return result

def divide(num1,num2):
    result = num1 / num2
    return result

def is_even(num1):
    result = num1 % 2
    if(result == 1):
        print("เป็นเลข คี่")
        return result
    elif(result == 0):
        print("เป็นเลข คู่")
    return result



def main():
    num1 = int(input("กรอกเลขตัวที่ 1 :"))
    num2 = int(input("กรอกเลขตัวที่ 2 :"))
    print("+ - * / เลือกเครื่องหมาย")
    print("[1] +")
    print("[2] -")
    print("[3] *")
    print("[4] /")
    operation = input("เลือกสักอัน: ")
    if (operation == "1"):
        result = add(num1,num2)
        print("ผลบวกคือ: " ,result)
    
    elif(operation == "2"):
        result = minus(num1,num2)
        print("ผลลบคือ: " ,result)

    elif(operation == "3"):
        result = mutiple(num1,num2)
        print("ผลคูณคือ: " ,result)

    elif(operation == "4"):
        result = divide(num1,num2)
        print("ผลหารกคือ: " ,result)


    print(is_even(result))
   


main()