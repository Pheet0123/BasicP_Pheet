# i = 0 
# while i < 5:
#     print("..ds")
#     i = i + 1
#     if i == 4:
#         break


# start = True
# while start:
#     print("เลือกข้อความที่ต้องการเล่น")
#     print("ข้อความที่ [1] โจทย์แรก")
#     print("ข้อความที่ [2] โจทย์สอง")
#     x = int(input("กรุณากรอกเลข: "))
#     if (x == 1):
#         print("โจทย์ที่ 1 ")
#     elif (x == 2):
#         print("ทำโจทย์ที่ 2")
#     start = False

mon = 100
weapon1 = 50 
weapon2 = 40
weapon3 = 20

start = True
while start:
    print("เลือกที่จะ สู้ [1]")
    print("เลือกที่จะ หนี [2] ")
    op = input("อยากจะสู้หรือหนี ")
    if (op == "1"):
        print("เดินไปสู้กับบอส ")
        hit = int(input("จะเลือกว่าจะโจมตีกี่รอบ "))
        for i in range(hit):
            if (hit):
                print("เลือกอาวุธที่ 1 ดามเมจ 50 [1] ")
                print("เลือกอาวุธที่ 2 ดามเมจ 40 [2] ")
                print("เลือกอาวุธที่ 3 ดามเมจ 20 [3] ")
                weapon = int(input("เลือกอาวุธ "))
                if (weapon == 1):
                    print("mon hp " ,mon =- (weapon1*hit))
                elif(weapon == 2):
                    print("mon hp " ,mon =- (weapon2*hit))
                elif(weapon == 3):
                    print("mon hp " ,mon =- (weapon3*hit))

                
    elif (op == "2"):
        print("วิ่งหนี้ออกมาแล้ว เกมจบแล้ว")
        start = False
    

   
    # print("เลือกใช้อาวุธที่ 1")
    # print("เลือกใช้อาวุธที่ 2")
    # x = int(input("กรุณากรอกเลข: "))
    # if (x == 1):
    #     print("โจทย์ที่ 1 ")
    # elif (x == 2):
    #     print("ทำโจทย์ที่ 2")
    # start = False