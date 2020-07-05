#!/usr/bin/python3

#Relação de asserts
#https://docs/python/org/3/library/unittest.html#assert-methods

from unittest import TestCase, main

def e_impar(num):
    try:
        if int(num) % 2 != 0:
            return True
        else:
            return False
    except Exception as e:
        return None

class TestImpar(TestCase):
    def test_impar(self):
        self.assertEqual(e_impar(3), True)
        self.assertEqual(e_impar(12313), True)
        self.assertEqual(e_impar(3212), False)

    def test_impar_string(self):
        self.assertEqual(e_impar('21321'), True)
        self.assertEqual(e_impar('3212'), False)
        self.assertEqual(e_impar('texto'), None)

if __name__ == '__main__':
    main()