from calculator import Calculator

class Prueba():

    problemas = Calculator
    list_Operaciones = []
    num_fila = 0

    with open ('numeros.txt', 'r') as ArchivoTexto:
        for s in ArchivoTexto:
            operaciones = s.split(' ')
            list_Operaciones.append(operaciones)

    # def pruebas(list_Operaciones,operaciones,problemas):
        for e in list_Operaciones:
            num_fila += 1
            if  e[1] == "+":
                operaciones = problemas.suma(e[0],e[2])
                if operaciones == float(e[3]):
                    print (f"Fila {num_fila} | {e[0]} + {e[2]} = {e[3]} =====> Prueba superada!! {operaciones}")
                else:
                    print (f"Fila {num_fila} | {e[0]} + {e[2]} = {e[3]} =====> No supero la prueba :( {operaciones}")

            elif e[1] == "-":
                operaciones = problemas.resta(e[0],e[2])
                if operaciones == float(e[3]):
                    print (f"Fila {num_fila} | {e[0]} - {e[2]} = {e[3]} =====> Prueba superada!! {operaciones}")
                else:
                    print (f"Fila {num_fila} | {e[0]} - {e[2]} = {e[3]} =====> No supero la prueba :( {operaciones}")


            elif e[1] == "-":
                operaciones = problemas.resta2(e[0],e[2])
                if operaciones == float(e[3]):
                    print (f"Fila {num_fila} | {e[0]} - {e[2]} = {e[3]} =====> Prueba superada!! {operaciones}")
                else:
                    print (f"Fila {num_fila} | {e[0]} - {e[2]} = {e[3]} =====> No supero la prueba :( {operaciones}")


            elif e[1] == "/":
                operaciones = problemas.dividir(e[0],e[2])
                if operaciones == float(e[3]):
                    print (f"Fila {num_fila} | {e[0]} / {e[2]} = {e[3]} =====> Prueba superada!! {operaciones}")
                else:
                    print (f"Fila {num_fila} | {e[0]} / {e[2]} = {e[3]} =====> No supero la prueba :( {operaciones}")


            elif e[1] == "*":
                operaciones = problemas.multiplicar(e[0],e[2])
                if operaciones == float(e[3]):
                    print (f"Fila {num_fila} | {e[0]} * {e[2]} = {e[3]} =====> Prueba superada!! {operaciones}")
                else:
                    print (f"Fila {num_fila} | {e[0]} * {e[2]} = {e[3]} =====> No supero la prueba :( {operaciones}")

            elif e[1] == "^":
                operaciones = problemas.potencia(e[0],e[2])
                try: 
                    if operaciones == float(e[3]):
                        print (f"Fila {num_fila} | {e[0]} ^ {e[2]} = {e[3]} =====> Prueba superada!! {operaciones}")
                    else:
                        print (f"Fila {num_fila} | {e[0]} ^ {e[2]} = {e[3]} =====> No supero la prueba :( {operaciones}")

                except:
                    print( "Operacion no valida")

    # print(pruebas(list_Operaciones,operaciones,problemas))