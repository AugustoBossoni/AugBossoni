print("===============  CAIXA ELETRONICO  ======================")
op = input("tecle [1] para saque.    [2] para pagamento de divida. ")
if(op == "1"):
	sald = float(input("saldo da conta: "))
	sqs = float(input("valor que deseja sacar: "))
	sq = sqs	
	if(sq <= sald):
		print("saque aprovado")
		cem = sq // 100
		sq = sq %100
		dez = sq // 10
		um = sq % 10
		um1 = um // 2
		dez1 = dez // 2  
		if(sqs % 2 == 0):
			print(f"notas de $100: {cem:.0f}")
			if(dez % 2 == 0):
				print(f"notas de $20: {dez1:.0f}")
				print(f"notas de $2: { um1:.0f}")
			else:
				print(f"notas de $20: {dez1:.0f}")
				print(f"notas de $10: {dez % 2:.0f}")
			print(f"notas de $2: {um1:.0f}") 
			print(f"notas de $1: { um % 2:.0f}")
				 	
		else:
			print(f"notas de $100: {cem:.0f}")
			if(dez % 2 == 0):
				print(f"notas de $20: {dez1:.0f}")
				print(f"notas de $2: { um1:.0f}")
			else:
				print(f"notas de $20: {dez1:.0f}")
				print(f"notas de $10: {dez % 2:.0f}")
			print(f"notas de $2: {um1:.0f}") 
			print(f"notas de $1: { um % 2:.0f}")
		
	else:
		print("saldo insuficiente")
	
elif(op == "2"):
	div = float(input("Valor em divida: "))
	pag = float(input("Valor que deseja pagar:"))
	rest = pag - div 
	if (rest >= 0):
		print(f"Sua divida de ${div:.2f} foi quitada. Saldo atual de {rest:.2f} ")
	elif (rest < 0):
		print(f"seu saldo atual e igual a ${rest:.2f}")	
print("=========================================================")		
print("muito obrigado pela preferencia. Banco Boss agradece.")		
		