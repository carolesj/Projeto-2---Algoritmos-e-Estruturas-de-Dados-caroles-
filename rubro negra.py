class no:
	def __init__ (self, valor, cor = "vermelho", esquerda = None, direita = None, pai = None) :
		self.cor = cor
		self.valor = valor
		self.esquerda = esquerda
		self.direita = direita
		self.pai = pai
		
sentinela = no(None, "preto")





class arvore:
	
	
	
	def __init__ (self) :
		self.raiz = None

	
	
	def insercao (self, valor) :
		if (self.raiz == None) :
			self.raiz = no(valor, "preto", sentinela, sentinela)
		else: 
			atual = self.raiz
			while (True):
				if (valor < atual.valor) :
					if (atual.esquerda == sentinela) : 
						novo_no = no(valor, "vermelho", sentinela, sentinela, atual)
						atual.esquerda = novo_no
						break
					else:
						atual = atual.esquerda
				elif (valor > atual.valor) :
					if (atual.direita == sentinela) :
						novo_no = no(valor, "vermelho", sentinela, sentinela, atual)
						atual.direita = novo_no
						break
					else: 
						atual = atual.direita
				else:
					break
		try: 
			arruma_rn(atual)
		except:
			pass
	
	


	def rotacao_esquerda (self, atual) :
		aux = atual.direita
		atual.direita = aux.esquerda
		if (aux.esquerda != sentinela) :
			aux.esquerda.pai = atual
		aux.pai = atual.pai
		if (atual.pai == sentinela) :
			self.raiz = aux
		elif (atual == atual.pai.esquerda) :
			atual.pai.esquerda = aux
		else:
			atual.pai.direita = aux
		aux.esquerda = atual
		atual.pai = aux
		
		
	
	
	def rotacao_direita (self, atual) :
		aux = atual.esquerda
		atual.esquerda = aux.direita
		if (aux.direita != sentinela) :
			aux.direita.pai = atual
		aux.pai = atual.pai
		if (atual.pai == sentinela) :
			self.raiz = aux
		elif (atual == atual.pai.direita) :
			atual.pai.direita = aux
		else:
			atual.pai.esquerda = aux
		aux.direita = atual
		atual.pai = aux
		
					
	
	
	def arruma_rn (self, novo_no) : 
		while (novo_no.pai.cor == "vermelho") :
			if (novo_no.pai == novo_no.pai.pai.esquerda):
				tio = novo_no.pai.pai.direita
				if (tio.cor = "vermelho") :
					novo_no.pai.cor = "preto"
					tio.cor = "preto"
					novo_no.pai.pai.cor = "vermelho"
					novo_no = novo_no.pai.pai
				else:
					if (novo_no == novo_no.pai.direita):
						novo_no = novo_no.pai
						self.rotacao_esquerda(novo_no)
					novo_no.pai.cor = "preto"
					novo_no.pai.pai.cor = "vermelho"
					self.rotacao_direita(novo_no.pai.pai)
			else:
				tio = novo_no.pai.pai.esquerda
				if (tio.cor == "vermelho") :
					novo_no.pai.cor = "preto"
					tio.cor = "preto"
					novo_no.pai.pai = "vermelho"
					novo_no = novo_no.pai.pai
				else:
					if (novo_no == novo_no.pai.esquerda) :
						novo_no = novo_no.pai
						self.rotacao_direita(novo_no)
					novo_no.pai.cor = "preto"
					novo_no.pai.pai.cor = "vermelho"
					self.rotacao_esquerda(novo_no.pai.pai)
		self.raiz.cor = "preto"
	
	
	
	def maximo (self):
		iterador = self.raiz
		while (iterador.direita != sentinela):
			iterador = iterador.direita
		 return iterador.valor
		 
	def minimo (self):
		iterador = self.raiz
		while (iterador.esquerda != sentinela):
			iterador = iterador.esquerda
		return iterador.valor
