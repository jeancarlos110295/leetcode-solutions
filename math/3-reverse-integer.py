'''
URL: https://leetcode.com/problems/reverse-integer?envType=problem-list-v2&envId=math

Material de apoyo:

1. Aritmética de módulo y división
    https://oboe.com/learn/algorithmic-digit-manipulation-and-extraction-1comkgs

2. stackoverflow
    https://stackoverflow.com/questions/41474035/can-someone-explain-how-reversing-an-integer-using-10-works?utm_source=chatgpt.com


Ejercicio:
    Given a signed 32-bit integer x, return x with its digits reversed. 
    If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

    Example 1:
        Input: x = 123
        Output: 321
    
    Example 2:
        Input: x = -123
        Output: -321
    
    Example 3:
        Input: x = 120
        Output: 21

    Constraints: -231 <= x <= 231 - 1

    
Analisis:
    1. Validaciones:
        a. Debe ser un numero

    2. Restrición:
        a. [-2^31, 2^31 - 1], representa el rango de un entero signed de 32 bits.

            En enteros signed:
                1 bit indica el signo.
                31 bits representan magnitud.

            ¿Por qué el máximo es 2^31 - 1?

                Con 31 bits puedes representar: 2^31, valores distintos.

                Pero como se empieza desde 0, el máximo es: 2^31 - 1

                Que da: 2147483647

            ¿Y el mínimo?

                El mínimo es: -2^31

                Que da: -2147483648
            
            ¿Por qué el rango es asimétrico?

                | Tipo   | Valor       |
                | ------ | ----------- |
                | Máximo | 2147483647  |
                | Mínimo | -2147483648 |

                Hay un negativo extra. Eso ocurre por cómo funciona: Complemento a dos (Two’s Complement)
                que es la representación binaria de enteros signed.

                Visualmente: -2147483648  ...  -1 0 1 ... 2147483647

                Cantidad total de números: 2^32
'''


class ReverseInteger:
    def __init__(self, x):
        self.x = int(x)

    def resultado(self):
        num_res = 0

        max_int = (2 ** 31) - 1

        # Guardar el signo original del número.
        sign = -1 if self.x < 0 else 1
        self.x = abs(self.x)

        while self.x != 0:
            u_digito = self.x % 10

            # Impedir overflow
            if (
                num_res > max_int // 10 or
                (
                    num_res == max_int // 10 and u_digito > max_int % 10
                )
            ):
                return 0

            num_res = (num_res * 10) + u_digito

            self.x //= 10

        return num_res * sign

init_reverse_integer = ReverseInteger(123)

resultado = init_reverse_integer.resultado()

print( resultado )