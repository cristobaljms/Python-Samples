from unittest import TestCase, main

# EJERCICIO 1: Vuelta en monedas

def monedas(valor):
    listMonedas = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    dictMonedas = dict({2:0, 1:0, 0.5:0, 0.2:0, 0.1:0, 0.05:0, 0.02:0, 0.01:0})

    for moneda in listMonedas:
        while (moneda <= valor):
            valor = valor - moneda
            dictMonedas[moneda] += 1

    result = list()

    for moneda in listMonedas:
        if(dictMonedas[moneda] > 0):
            result.append((dictMonedas[moneda], moneda))
    return tuple(result)


# EJERCICIO 2: Vuelta en monedas
# EJERCICIO 3: Vuelta en monedas
# EJERCICIO 4: Vuelta en monedas
# EJERCICIO 5: Vuelta en monedas
# EJERCICIO 6: Vuelta en monedas
# EJERCICIO 7: Vuelta en monedas
# EJERCICIO 8: Vuelta en monedas
# EJERCICIO 9: Vuelta en monedas
# EJERCICIO 10: Vuelta en monedas

class Test(TestCase):
    def test_monedas(self):
        self.assertEqual(monedas(9.4), ((4, 2), (1, 1), (2, 0.2)))
        self.assertEqual(monedas(1.5), ((1, 1), (1, 0.5)))
        self.assertEqual(monedas(.01), ((1, 0.01),))
        self.assertEqual(monedas(0), tuple())

    # def test_ordenar_indirecto(self):
    #     self.assertEqual(ordenar_indirecto((50, 98, 10, 63, 31, 25, 63, 74)),
    #                      (2, 5, 4, 0, 3, 6, 7, 1))
    #     self.assertEqual(ordenar_indirecto(tuple(range(1,10))), tuple(range(9)))
    #     self.assertEqual(ordenar_indirecto(tuple()), tuple())
    #     self.assertEqual(ordenar_indirecto((1,)), (0,))

    # def test_media(self):
    #     self.assertEqual(media([1,2,4,8,16,32,64,128]), 31.875)
    #     self.assertEqual(media([2]), 2)
    #     self.assertEqual(media([]),0)
    #     self.assertEqual(media([1,5]), 3)

    # def test_subintervalo_mayor(self):
    #     self.assertEqual(subintervalo_mayor(((1,4),(5,6))),(1,4))
    #     self.assertEqual(subintervalo_mayor(((1,5),(4,6))),(1,6))
    #     self.assertEqual(subintervalo_mayor(((5,7),(9,11),(2,5),(1,4),(4,6))),(1,7))
    #     self.assertEqual(subintervalo_mayor(((4,6),)),(4,6))

    # def test_rectangulo_maximo(self):
    #     self.assertEqual(rectangulo_maximo(((1,0,0,1),(1,0,0,1),(0,0,0,1),(1,1,1,1))),
    #                      ((1,0),(3,3)))
    #     self.assertEqual(rectangulo_maximo(((1,0),(1,0))), ((1,0),(2,2)))
    #     self.assertEqual(rectangulo_maximo(((0,),)), ((0,0),(1,1)))
    #     self.assertEqual(rectangulo_maximo(((0,),)), ((0,0),(1,1)))
        
    # def test_particion(self):
    #     def tp(L,k):
    #         a,b,c = particion(L,k)
    #         self.assertEqual(len(a) + len(c), len(L) - 1)
    #         self.assertTrue(all(e < b for e in a))
    #         self.assertTrue(all(e > b for e in c))
    #         self.assertEqual(b, L[k])
    #     tp([32, 17, 41, 18, 52, 98, 24, 65], 2)
    #     tp([52, 98, 24], 2)
    #     tp([52, 1, 98], 2)
    #     tp([52, 5, 1], 2)

    # def test_seleccionar_rapido(self):
    #     self.assertEqual(seleccionar_rapido([5], 0), 5)
    #     from random import shuffle
    #     L = list(range(8))
    #     self.assertEqual(seleccionar_rapido(L, 3), 3)
    #     L = list(range(3,18))
    #     shuffle(L)
    #     self.assertEqual(seleccionar_rapido(L,3), 6)
    #     L = list(range(4,100,2))
    #     shuffle(L)
    #     self.assertEqual(seleccionar_rapido(L,5), 14)

    # def test_max2(self):
    #     self.assertEqual(max2([1,2]), (2,1))
    #     from random import shuffle
    #     L = list(range(8))
    #     self.assertEqual(max2(L), (7,6))
    #     L = list(range(3,18))
    #     shuffle(L)
    #     self.assertEqual(max2(L), (17,16))
    #     L = list(range(4,100,2))
    #     shuffle(L)
    #     self.assertEqual(max2(L), (98,96))

    # def test_mayoritario(self):
    #     self.assertEqual(mayoritario([1,1,2]), 1)
    #     self.assertEqual(mayoritario([1,2,2,1,3,1,1,1]), 1)
    #     self.assertEqual(mayoritario([1]), 1)
    #     self.assertRaises(ValueError, lambda : mayoritario([1,2,3]))

    # def test_buscar_sumandos(self):
    #     def ts(V,x):
    #         i,j = buscar_sumandos(V, x)
    #         self.assertNotEqual(i,j)
    #         self.assertEqual(V[i]+V[j], x)
    #     ts([12, 4, 14, 17, 9], 13)
    #     ts([1, 1], 2)
    #     ts([1, 2, 1], 2)
    #     self.assertRaises(ValueError, lambda : buscar_sumandos([1,2,3], 8))

main()