#Coeficiente y residuo para numeros enteros.
def DivisionN(a,b):
    r=a
    q=0
    while r<=b:
        r=b+r
        q=q-1
        if r==0:
            print("El residuo es: ",r)
            print("El cociente es: ",q)
        elif r>0 and r<b:
            print("El residuo es: ",r)
            print("El cociente es: ",q)
def DivisionG(a,b):
    if a>0:
        r=a
        q=0
        while r>=b:
            r=r-b
            q=q+1
        print("El residuo es: ",r)
        print("El cociente es: ",q)
    elif a<0:
        DivisionN(a,b)
a=int(input("Ingresar el numero 'a': "))
b=int(input("Ingresar el numero 'b': "))
DivisionG(a,b)