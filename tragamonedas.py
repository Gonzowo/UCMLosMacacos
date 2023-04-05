#Gonzalo Cerpa - 21.191.139-5 - gonzalo.cerpa@alu.ucm.cl
#Juan Rojas - 21.443.134-3 - juan.rojas.02@alu.ucm.cl
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
    aux=0
    while aux==0:
        monto=int(input("Ingese un Monto Inicial: "))
        if "-" in str(monto):
            print("No existe dinero negativo, ingrese otro monto")
        elif monto<100:
            print("Ingrese un valor superior a los 99")
        else:
            aux=aux+1
            return int(monto)

    
#funcion para ingresar la apuesta
def apuesta():
    aux=0
    apuesta=int(input("Ingrese la cantidad que desea apostar ($100, $500 o $1000): "))
    while aux==0:
        if apuesta==100 or apuesta==500 or apuesta==1000:
            aux=aux+1
        else:
            print("\n")
            print("Por favor, elegir uno de los montos indicados:")
            apuesta=int(input("Ingrese la cantidad que desea apostar ($100, $500 o $1000): "))
    return int(apuesta)


#funcion premios
def premios(prob1,prob2,prob3,apuestas):
    recomp=[]
    #agregar las prob
    recomp.append(prob1)
    recomp.append(prob2)
    recomp.append(prob3)
    #usar count para saber cuando son iguales o distintos
    if recomp.count(7)==3:
        apuestas=apuestas*1000
        #caso de ganar, mutliplica por x cantidad, aplica para los demás casos de abajo
        return apuestas
    elif recomp.count(6)==3:
        apuestas=apuestas*250
        return apuestas
    elif recomp.count(5)==3:
        apuestas=apuestas*150
        return apuestas
    elif recomp.count(4)==3 or recomp.count(3)==3:
        apuestas=apuestas*50
        return apuestas
    elif recomp.count(2)==3 or recomp.count(1)==3:
        apuestas=apuestas*30
        return apuestas
    elif recomp.count(0)==3:
        apuestas=apuestas*20
        return apuestas
    elif recomp.count(6)==2 or recomp.count(5)==2 or recomp.count(7)==2:
        apuestas=apuestas*10
        return apuestas
    elif recomp.count(7)==1:
        apuestas=apuestas*5
        return apuestas
    elif recomp.count(5)==1 or recomp.count(6)==1:
        apuestas=apuestas*2
        return apuestas
    else:
        apuestas=apuestas #caso de perder
        return apuestas

#Codigo principal
if __name__=="__main__":
    montos=monto()
    terminar = 1
    while terminar == 1:
        apuestas=apuesta()
        prob1=probabilidades()
        prob2=probabilidades()
        prob3=probabilidades()
        recompensas=premios(prob1,prob2,prob3,apuestas)
        print("---------")
        print(prob1,"-",prob2,"-",prob3)
        print("---------")
        #condicional para modificar el monto en caso de ganar
        if recompensas > apuestas:
            print("Gana: $",recompensas)
            montos=montos+recompensas
            print("Su nuevo saldo es: $",montos)
        #condicional para modificar el monto en caso de perder
        else:
            print("Pierde: $",recompensas)
            montos=montos-recompensas
            print("Su nuevo saldo es: $",montos)
        print("Continuar? (1=SI, Otro valor=NO):")
        continuar=int(input())
        #Condicional en caso de seguir toma en cuenta tambien si el saldo actual esta en el minimo requerido para apostar
        if continuar==1 and montos>=100:
            pass
        #Condicional en caso de que el saldo sea inferior a una apuesta minima
        elif montos<100:
            print("Saldo insuficiente, la partida terminara.")
            terminar=terminar-1
        #Condicional para terminar la partida
        elif continuar!=1:
            print("Su saldo final fue: $",montos)
            terminar=terminar-1

