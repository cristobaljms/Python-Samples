def cuartiles(L):
    L = list(L)
    L.sort()
    Q1 = 0
    posQ1 = (len(L)+1)/float(4) 
    decimal = posQ1 - int(posQ1)
    if decimal > 0:
        Q1 = L[int(posQ1)-1] + decimal*(L[int(posQ1)]-L[int(posQ1)-1])
    else:
        Q1 = L[int(posQ1)-1]

    Q2 = 0
    posQ2 = 2*(len(L)+1)/float(4) 
    decimal = posQ2 - int(posQ2)
    if decimal > 0:
        Q2 = L[int(posQ2)-1] + decimal*(L[int(posQ2)]-L[int(posQ2)-1])
    else:
        Q2 = L[int(posQ2)-1]

    Q3 = 0
    posQ3 = 3*(len(L)+1)/float(4)
    decimal = posQ3 - int(posQ3)
    if decimal > 0:
        Q3 = L[int(posQ3)-1] + decimal*(L[int(posQ3)]-L[int(posQ3)-1])
    else:
        Q3 = L[int(posQ3)-1]

    Q4 = L[-1]

    return (Q1, Q2, Q3, Q4)


L = ((1,1,1))

print (cuartiles(L))

    # def test_cuartiles(self):
    #     self.assertEqual(cuartiles((63,34,60,30,45,32,56,40,21,37,54,33,28,53,19,45,28,52,24,29)),
    #                      (28.25, 35.5, 52.75, 63))
    #     self.assertEqual(cuartiles(range(10)), (1.75, 4.5, 7.25, 9))
    #     self.assertEqual(cuartiles((1,2,3)), (1,2,3,3))
    #     self.assertEqual(cuartiles((1,1,1)), (1,1,1,1))