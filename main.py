# función para ejemplificar una divisiion por cero
def zero_err():
    try:
        num1, num2 = 2, 0
        result = num1 / num2
        return result
    except ZeroDivisionError as error:
        print("No es posible dividir por cero")
        print(error)


# función para dar un ejemplo donde una variable es usada pero no es definida
def name_err():
    try:
        num1, num2 = 2, 0
        result = num1 / num3
        return result
    except NameError as error:
        print("Hay un nombre de variable no definida")
        print(error)


# funcion donde se pasa un indice fuera del rango declarado y que genera un IndexError
def ind_err():
    try:
        num1 = [1, 2, 3, 4, 5]
        result = num1[0] / num1[10]
        return result
    except IndexError as error:
        print("No se puede usar un indice que sup[ere el total de longitud de unba lista ")
        print(error)


if __name__ == '__main__':
    # MAnejo de errores mas comunes
    zero_err()
    name_err()
    ind_err()
