import time
#from time import sleep
a = 54
b= 82
a + b

print("Sestvek je"+str(a+b))

if a>b:
    print("a je vecji od b")
elif a<b:
    print("b je vecji od a")
else:
    print("noben pogoj ni izplonjen")

while True:
    a += 1
    print("a je:" + str(a))
    time.sleep(0.1)
    if a>b:
        break

vhod = input("Vnesi najljubso stevilko: ")
print("vasa stevilka: " +str(vhod))