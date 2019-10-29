def suma(x,y):
    return(x+y)

def mul(x,y):
    return(x*y)

def principal():
    x = (int(input("ingrese un número\n")))
    y =(int(input("ingrese otro número\n")))
    print("la suma de los dos números es:", suma(x,y))
    print("la multiplicacion es:", mul(x,y))
    return
principal()