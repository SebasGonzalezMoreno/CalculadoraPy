import math

class Calculator():

    # def __init__ (self, num1, num2):
    #     self.num1 = float(num1)
    #     self.num2 = float(num2)

    def suma(num1, num2):
        suma = float(num1) + float(num2)
        return(suma)

    def resta(num1, num2):
        resta = float(num1) + float(num2)
        return(resta) 

    def resta2(num1, num2):
        resta2 = float(num1) - float(num2)
        return(resta2) 

    def multiplicar(num1, num2):
        multiplicar = float(num1) * float(num2)
        return(multiplicar) 

    def dividir(num1, num2):
        if (float(num2) == 0):
            mensaje= "No se puede dividir entre cero"
        else:
            dividir2 = float(num1) / float(num2)
            mensaje=(dividir2)
        return mensaje
    
    def potencia(num1, num2):
        potencia = float(num1) ** float(num2)
        return(potencia) 