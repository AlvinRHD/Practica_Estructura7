class ValidadorDeEdad:
    def validar(self, edad):
        try:
            edad_entero = int(edad)
            if edad_entero >= 0:
                return f"edad válida: {edad_entero}"
            else:
                return "Error, la edad no puede ser un número en negativo."
        except ValueError:
            return "Error, la edad ingresada no es un número entero válido."



validador = ValidadorDeEdad()


entrada = input("Ingresar una edad: ")

resultado = validador.validar(entrada)

print(resultado)