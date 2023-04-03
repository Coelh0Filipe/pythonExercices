import math          #part1
def my_sqrt(a):
    x = 1
    while True:
        y = (x + a / x) / 2.0
        if y == x:
            break
        x = y

    return y

def test_sqrt(a):       #part2
    for a in range(25):
        a = a + 1
        formula = my_sqrt(a)
        automatic = math.sqrt(a)
        diff = abs(math.sqrt(a)- my_sqrt(a))               # built-in absolute function returns the absoulte value.
        if abs(math.sqrt(a)- my_sqrt(a))< (1e-14):     #values of my_sqrt and math.sqrt are almost identical with difference less than the value of epsilon. (epsilon=1e-14)
            print('a=', a, '| my_sqrt(a)=',formula, '| math.sqrt(a) =',automatic, '| diff =',diff)

            
test_sqrt(25)
