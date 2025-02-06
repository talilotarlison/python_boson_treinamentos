salario = float(input("Valor salario"))

def cal_bonus(salario):
	bonus = 0
	if(salario>=2400):
	  bonus=	salario * 0.05
	elif(salario>=1400):
	  bonus = 	salario * 0.10
	else:
	  bonus=	salario * 0.15
	return salario + bonus

novo_salario = cal_bonus(salario)

print("novo salario R$",novo_salario)