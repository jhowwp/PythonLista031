'''
Fazer um programa que pergunte uma temperatura ao usuário, em graus Fahrenheit, e aprewente esta temperatura
convertida em graus Celsius. A formula da conversão é c= (f-32)
'''

f = float(input("informe uma temperatura em Graus Fahrenheit:"))

# c = (f - 32) x 5 : 9
c = (f - 32) * 5 / 9

print(f, "graus Fahrenheit correspondem á ", "graus Celsius")

valor_pi = math.pi
print("valor de pi ", valor_pi)