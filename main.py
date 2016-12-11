def main () :
	
	rubro_negra = arvore()
	numero_operacoes = int(input())

	for i in range(numero_operacoes):
		O = input().split()
		
		if (O[0] == "1") :
			rubro_negra.insercao(int(O[1]))
		elif (O[0] == "2") :
			rubro_negra.sucessor(int(O[1]))
		elif (O[0] == "3") :
			rubro_negra.predecessor(int(O[1]))
		elif (O == "4") :
			rubro_negra.maximo()
		elif (O == "5") :
			rubro_negra.minimo()
		elif (O == "6") :
			rubro_negra.preordem()
		elif (O == "7") :
			rubro_negra.emordem()
		elif (O == "8") :
			rubro_negra.posordem()
