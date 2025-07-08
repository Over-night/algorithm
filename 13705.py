from math import sin, cos

a, b, c = map(int, input().split())

fx = lambda x: a * x + b * sin(x) - c  
d_fx = lambda x: a + b * cos(x)      
    
x_n = c//a
tolerance = 1.0e-25                       # 오차
    
while True:
    fx_n = fx(x_n)            
    d_fx_n = d_fx(x_n)      
    
    x_nP1 = x_n - fx_n / d_fx_n
    if abs(x_nP1 - x_n) < tolerance:
        print(round(x_nP1, 6))
        break
    x_n = x_nP1
