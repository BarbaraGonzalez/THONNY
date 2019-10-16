"""Problemas moodle facil"""

"""Realice un programa que lea por teclado tres números
enteros positivos (H, M, S)que contienen hora(s), minuto(s) y
segundo(s) respectivamente, y calcule y muestre el tiempo
en segundos."""

def horas_a_segundo (H):
    res1 = 36000*H
    return res1

def minutos_a_segundo (M):
    res2 = 60*M
    return res2 

def segundos (S):
    res3 = S
    return res3

H= int(input("ingrese H"))
M= int(input("ingrese M"))
S= int(input("ingrese S"))

if (H>0 and M>0 and S>0) :
    suma = horas_a_segundo(H)+minutos_a_segundo(M)+ segundos(S)
    print (suma)
else :
    print("error")