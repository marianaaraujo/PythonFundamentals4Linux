#!/usr/bin/python3

#Relação de asserts
#https://docs/python/org/3/library/unittest.html#assert-methods

from unittest import TestCase, main

def soma(x,y):
    return x + y

class TestSoma(TestCase):
    def test_soma_equal(self):
        self.assertEqual(soma(2,2),4)

    def test_soma_not_equal(self):
        #self.assertNotEqual(soma(4,2),6)
        self.assertNotEqual(soma(4,2),5)

if __name__ == '__main__':
    main()