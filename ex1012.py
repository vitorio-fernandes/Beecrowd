from abc import ABC,abstractmethod

A = float(input())
B = float(input())
C = float(input())

triangulo = A*C/2
circulo = 3.14159*(C**2)
trapezio = ((A+B)*C)/2
quadraado = B**2
retângulo = A*B

print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % 
      (triangulo, circulo, trapezio, quadraado, retângulo))




