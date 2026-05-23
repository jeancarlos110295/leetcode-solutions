# https://leetcode.com/problems/add-two-numbers/

# Definición de ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def listToListNode(self, nums):
        """Convierte una lista normal de Python a una lista enlazada"""
        dummy = ListNode()
        actual = dummy
        for num in nums:
            actual.next = ListNode(num)
            actual = actual.next
        return dummy.next

    def revertList(self, lista):
        """Revierte una lista normal"""
        return lista[::-1]
    
    def convertListToInt(self, lista):
        """Convierte una lista de dígitos a un entero"""
        return int("".join(map(str, lista)))
    

    def listNodeToList(self, node):
        """Convierte una lista enlazada a una lista normal de Python"""
        result = []
        while node:
            result.append(node.val)
            node = node.next

        return result


    def addTwoNumbers(self, l1, l2):
        # Convertir las listas enlazadas a listas normales
        list1 = self.listNodeToList(l1)
        list2 = self.listNodeToList(l2)

        # Revertir las listas para obtener el número correcto
        num1 = self.convertListToInt(self.revertList(list1))
        num2 = self.convertListToInt(self.revertList(list2))

        # Sumar los dos números
        suma = num1 + num2

        # Convertir la suma a una lista de dígitos en orden invertido
        suma_revertida = list(map(int, self.revertList(str(suma))))

        # Convertir la lista de dígitos de vuelta a lista enlazada
        return self.listToListNode(suma_revertida)



# Instanciar solución y resolver
sol = Solution()
resultado = sol.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))

print("Resultado:")
print(sol.listNodeToList(resultado))  # Debería imprimir [7, 0, 8] que representa el número 807