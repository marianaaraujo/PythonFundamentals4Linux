#!/usr/bin/python3

par = []

for n in range(20):
    if n % 2 != 0:
        continue
    
    par.append(n)

print(par)