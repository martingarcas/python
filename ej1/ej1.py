a = 10
if a > 5:
    b=1+2j
    c=0+6j
    print(b+c)

def saluda(nombre="silverio", edad=50, idioma="español"):
    return f"Hola {nombre} hablas {idioma} y tienes {edad} años"

print(saluda(edad=51))

def sumar(a,b):
    return a + b

print(sumar(2, 5))

def suma(*valores):
    total = 0

    for num in valores:
        total += num

    return total

print(suma(1, 2, 3, 4, 5, 60))

def sumares(valores):
    total = 0

    for num in valores:
        total += num

    return total

print(sumares([1, 2, 3, 4, 5, 60]))

def esDni(dni):
    letra   = (dni[-1:]).upper()
    numero  = dni[:-1]
    letras  = "TRWAGMYFPDXBNJZSQVHLCKE" 
    respuesta = False

    if (letra in letras) and numero.isnumeric():
        numero = int(numero)

        if letras[numero%23] == letra:
            """
            letras.index(letra)
            """
            respuesta = True

    return respuesta


print(esDni("77383320g"))
