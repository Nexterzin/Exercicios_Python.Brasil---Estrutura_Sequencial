#Faça um Programa que pergunte quanto você ganha por hora e o número 
# de horas trabalhadas no mês. Calcule e mostre o total do seu salário 
# no referido mês, sabendo-se que são descontados 11% para o Imposto 
# de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que 
# nos dê:
# A - salário bruto.
# B - quanto pagou ao INSS.
# C - quanto pagou ao sindicato.
# D - o salário líquido.
# E - calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

print('Bem vindo!!')

gh = float(input('Informe quanto voce ganha por hora trabalhada: ')) 
ht = float(input('Informe as horas trabalhadas neste mês: '))

sb = gh*ht
print('Seu salario bruto é: ',sb)

ir = sb*11/100
print('Voce pagou R$',ir,'de importo de renda')

inss = sb*8/100
print('Voce pagou R$',inss,'de INSS')

sindicato = sb*5/100
print('Voce pagou R$',sindicato,'de sindicato')

salario_liquido = sb-ir-inss-sindicato
print('Seu salario liquido é: R$',salario_liquido)