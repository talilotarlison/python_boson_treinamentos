n1 = float(input("nota 1"))
n2 = float(input("nota 2"))

def cal_media(n1,n2):
	return (n1 +n2)/2

media = cal_media(n1,n2)

if(media >= 7):
	print("aprovado")
elif(media>=5):
	print("recuperacao")
else:
	print("reprovado")