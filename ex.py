n1=int(input("請輸入數字一: "))
n2=int(input("請輸入數字二: "))
op=input("請輸入運算: +,-,*,/: ")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援的運算")