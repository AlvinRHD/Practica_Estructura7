class Divisor:
    def dividir(self, numerador, denominador):
        try:
            resultado = numerador / denominador
            return resultado
        except ZeroDivisionError:
            return "Error, no se puede dividir entre 0."


divisor = Divisor()

numerador = 10

denominador = 0

resultado = divisor.dividir(numerador, denominador)

print(resultado)