#Gonzalo Cerpa - 
#Juan Rojas - 21.443.134-3
#Sección 3

#Proyecto Tragamonedas
import random

#funcion para generar la probabilidad de los numeros
def probabilidades():
    #variable que genera al numero
    variable=random.randint(1,100)
    #probabilidades de que salga cada numero
    if variable in range(1,2):
        variable=7
    elif variable in range(3,5):
        variable=6
    elif variable in range(6,10):
        variable=5
    elif variable in range(11,20):
        variable=4
    elif variable in range(21,30):
        variable=3
    elif variable in range(31,50):
        variable=2
    elif variable in range(51,70):
        variable=1
    else:
        variable=0
    return variable

#funcion monto ingresado
def monto():
    monto=int(input("Ingese un Monto Inicial: "))
    if "-" in str(monto):
        print("No existe dinero negativo, ingrese otro monto")
    else:
        return int(monto)

#funcion para ingresar la apuesta
def apuesta():
    apuesta=int(input("Ingrese la cantidad que desea apostar ($100, $500 o $1000): "))
    #if apuesta es distinto de los 3 valores, que lance error
    if apuesta!= int(100):
        print("Solamente puede seleccionar los valores en los parentesis, ingrese otro valor")
    elif apuesta!=int(500):
        print("Solamente puede seleccionar los valores en los parentesis, ingrese otro valor")
    elif apuesta!=int(1000):
        print("Solamente puede seleccionar los valores en los parentesis, ingrese otro valor")
    else:
        return int(apuesta)

#funcion para crear el bucle
def principal():
    
    monto()
    apuesta()
    
    pass

#funcion premios
def premios(prob1,prob2,prob3):

            
    pass


#funcion monto-apuesta

def monto_apuesta():
    total_fallo=monto()-apuesta()
    return total_fallo

if __name__=="__main__":
    prob1=probabilidades()
    prob2=probabilidades()
    prob3=probabilidades()
    monto_apuesta()
    