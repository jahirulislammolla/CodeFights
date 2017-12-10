/* Checked the sequence: 
 * a      = 20, 52, 116, 180, 308, 372, 564, 692, 884, 1012, 1332, 1460, ...
 * Found on OEIS (oeis.org/A209982) but there is no formula.
 * Next, checked the diff of neighbours (it seems good):
 * d      =   32, 64,  64,  128, 64,  192, 128, 192, 128,  320,  128, ...
 * It's not found on oeis, so tried: d / 32
 * d / 32 =    1,  2,   2,    4,  2,    6,   4,   6,   4,   10,    4
 * Found Euler totient function phi(n) (oeis.org/A000010)
 * Calculating phi(n) with this formula: 
 * phi(n) = n * (1 - 1 / p_1) * (1 - 1 / p_2) * ... * (1 - 1 / p_n)
 * where p_1..n the distinct prime divisors of n.
 * (Found here: en.wikipedia.org/wiki/Euler%27s_totient_function)
 * 
 * Finally: return sum(phi([1..n]) * 32) // initial value = 20 for n = 1 and phi(1) = 0
 */
def determinantOne(n):
    b = 20
    n += 1
    a = range(n)
    for i in range(2, n):
        if a[i] == i:
            for j in xrange(i, n, i):
                a[j] *= 1 - 1.0 / i
        b += int(a[i]) * 32
        print(b)
    return b % (1e9 + 7)
#second way.....
def determinantOne(n):
    s = 0
    n+=1
    p=[0 for i in range(n)]
    p[1] = 1
    i = 2
    while i < n:
        if p[i] == 0:
            p[i] = i - 1
            j = 2
            while j * i <n:
                if p[j] != 0:
                    q = j
                    f = i - 1
                    while q % i == 0:
                        f *= i
                        q //= i
                    p[i * j] = f * p[q]
                    #print(i*j,f,p[q],f * p[q])
                j += 1
        s += p[i]
        i += 1
    return ((s*32)%(10**9+7)+20)
