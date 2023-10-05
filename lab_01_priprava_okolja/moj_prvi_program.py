#vaja 2
"""
print("helo")
b=10
print(b)
b=False
print(b)
print(type(b))
#++++++++++++++
x=8
x=int(x)
#++++++++++++++
starost=input("Vtipkaj starost: ")
print(starost)
"-------------"
x=input()
y=input()

if(x>y):
    print(x, "je večji od ", y)
else:
    print(x, "je manjsi od", y)

"---------------"
"""
dolzinaPiramide=input("Vpisi dolzino piramide: ")

for x in range(int(dolzinaPiramide)):
    for y in range(x):
        print("*",end='')
    print()
         
