class Mierror(Exception):
    pass
async def funcion(n1:int=0,n2:int=0)->int:
    if n1<0:
        raise Mierror("N1 no puede ser negativo")
    else:
        return n1+n2
def imprimir (n1:int=0,n2:int=0):
    try:
        print(funcion(n1,n2))
    except Mierror as e:
        print(f"Mi error{e.args}")
    except  Exception as e:
        print(f"Exeption{e.args}") 

imprimir(10,15)
imprimir(-10,5)
imprimir("4,5")                       