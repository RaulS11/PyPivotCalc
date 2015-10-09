# coding=utf-8
#Punto más alto = H, Punto más bajo = L, Precio de cierre = C
H=float(raw_input('Escriba el punto más alto: '))
L=float(raw_input('Escriba el punto más bajo: '))
C=float(raw_input('Escriba el precio de cierre: '))
#Punto Pivote (P) = (H + L + C) / 3
#Los niveles de soporte y resistencia se calculan  en base al PP:
PP=(H+L+C)/3
#Primer nivel de soporte y resistencia:
#Primer nivel de soporte (S1)
S1=2*PP-H
#Primer nivel de resistencia (R1)
R1=2*PP-L
#Segundo nivel de soporte y resistencia
#Segundo nivel de soporte (S2)
S2=PP-(R1-S1)
#Segundo nivel de resistencia (R2)
R2=PP+(R1-S1)