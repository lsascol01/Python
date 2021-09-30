def f1():
    mensaje = "hola"
    def f2(mensaje):
        mensaje += " mundo"
        return print(mensaje)
    f2(mensaje)


f1()