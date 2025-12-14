import sys
import math

# Читаем входные данные
data = sys.stdin.readline().split()
R = int(data[0])
B = int(data[1])

# Перебираем делители B от 1 до sqrt(B)
for d in range(1, int(math.sqrt(B)) + 1):
    if B % d == 0:
        # Пара делителей (a, b) = (B/d, d)
        a = B // d
        b = d
        
        # Проверяем обе ориентации: W=a+2, H=b+2 и W=b+2, H=a+2
        for w_inner, h_inner in [(a, b), (b, a)]:
            W = w_inner + 2
            H = h_inner + 2
            
            # Проверяем условие для красных плиток
            if 2 * W + 2 * H - 4 == R and W >= H:
                print(W, H)
                sys.exit(0)