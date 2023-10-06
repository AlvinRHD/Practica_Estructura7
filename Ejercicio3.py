class ValidadorContraseña:
    def __init__(self, longitud_minima):
        self.longitud_minima = longitud_minima

    def validar(self, contraseña):
        try:
            if len(contraseña) < self.longitud_minima:
                raise ValueError("La contraseña es muy corta, debe tener por lo menos {} carácteres.".format(self.longitud_minima))
            else:
                print("Contraseña ingresada de forma válida.")
        except ValueError as error:
            print(error)



longitud_minima = 5

validador = ValidadorContraseña(longitud_minima)

contraseña = "Nunca69"

validador.validar(contraseña)  

contraseña = "maquinadefuego"

validador.validar(contraseña)