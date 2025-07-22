distance = int(input("โปรดกรอกระยะทาง "))
if distance <= 50 :
    print("10 บาท")
elif distance >= 51 and distance <= 100 :
    print("15 บาท")
elif distance >= 101 and distance <= 300 :
    print("25 บาท")
elif distance >= 301 and distance <= 500 :
    print("35 บาท")
else :
    print("45 บาท")