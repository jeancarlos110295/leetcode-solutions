"""
========================================================
LEETCODE: 9. Palindrome Number

https://leetcode.com/problems/palindrome-number?envType=problem-list-v2&envId=math
========================================================

Problema:
Determinar si un número entero es palíndromo.

Un palíndromo se lee igual de izquierda a derecha
y de derecha a izquierda.

Ejemplos:
121     -> True
1221    -> True
10      -> False
-121    -> False

Restricciones: -2^31 <= x <= 2^31 - 1

--------------------------------------------------------
Conceptos matemáticos utilizados
--------------------------------------------------------

1. Operador módulo (%)
Permite obtener el último dígito de un número.

Ejemplo:
123 % 10 = 3

2. División entera (//)
Permite eliminar el último dígito.

Ejemplo:
123 // 10 = 12

3. Construcción de número invertido

Formula:
invertido = invertido * 10 + ultimo_digito

Ejemplo:
123 -> 321

Proceso:
0 * 10 + 3 = 3
3 * 10 + 2 = 32
32 * 10 + 1 = 321

--------------------------------------------------------
Casos especiales analizados
--------------------------------------------------------

1. Números negativos
Los números negativos no pueden ser palíndromos.

Ejemplo:
-121 != 121-

2. Números terminados en 0
Si el número termina en 0 y no es 0,
no puede ser palíndromo.

Ejemplo:
10 -> 01

--------------------------------------------------------
Material de apoyo
--------------------------------------------------------

AlgoMaster:
https://algomaster.io/learn/dsa/palindrome-number

========================================================
"""

class PalindromeNumber:
    def __init__(self, x):
        self.x = x

    def resultado(self) -> bool:
        if self.x < 0:
            return False
        
        x_o = self.x
        num_res = 0

        max_int = (2 ** 31) - 1

        while self.x != 0:
            u_digito = self.x % 10

            # Impedir overflow
            if (
                num_res > max_int // 10 or
                (
                    num_res == max_int // 10 and u_digito > max_int % 10
                )
            ):
                return False

            num_res = (num_res * 10) + u_digito

            self.x //= 10

        if num_res == x_o:
            return True

        return False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = PalindromeNumber(x)
        return i.resultado()
    

i = Solution()

print( i.isPalindrome(121) )