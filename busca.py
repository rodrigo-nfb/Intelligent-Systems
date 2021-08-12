import numpy as np
from numpy import matrix 

Parede	= 0
Caminho = 1
Inicio 	= 2
Final 	= 3

Labirinto = [[2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
			[0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
			[0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
			[0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
			[0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
			[0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
			[0, 0, 1, 3, 1, 1, 1, 1, 0, 0]]
			
Auxiliar = [[2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
			[0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
			[0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
			[0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
			[0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
			[0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
			[0, 0, 1, 3, 1, 1, 1, 1, 0, 0]]

#------------------------------------------------------------------------------------------#				

class Posicao:
	def __init__(self, x, y):
		self.nome = nome(x, y)
		self.pos_x = x
		self.pos_y = y

		self.v_cima, self.v_baixo, self.v_esquerda, self.v_direita = verifica_Vizinhos(x,y)

		self.visitado = False
		self.pai = None

#------------------------------------------------------------------------------------------#

def encontra_Inicio():
	
	n = len(Labirinto)
	i = 0
	j = 0
	
	while(Labirinto[i][j] != Inicio):
		if(j < n-1):
			j+=1
		else:
			j = 0
			i+=1
	
	return i, j

#------------------------------------------------------------------------------------------#

def verifica_Vizinhos(x,y):

	c = False
	b = False
	e = False	
	d = False
	
	if(x > 0 and Labirinto[x-1][y] != Parede):
		c = True
	if(x < 9 and Labirinto[x+1][y] != Parede):
		b = True
	if(y > 0 and Labirinto[x][y-1] != Parede):
		e = True
	if(y < 9 and Labirinto[x][y+1] != Parede):
		d = True
	
	return c, b, e, d

#------------------------------------------------------------------------------------------#

def buscaEmProfundidade(pos_inicial):

	print("\n   Busca em Profundidade:\n")
	
	imprimir_caminho(Auxiliar)
	
	Lista = []
	caminho = []
	
	Pilha = []
	Pilha.append(pos_inicial)
	
	while len(Pilha) > 0:	
		noh_atual = Pilha.pop()
		
		if noh_atual.visitado == False:
			noh_atual.visitado == True
			
			Lista.append(noh_atual.nome)
			caminho.append(noh_atual)
			
			Auxiliar[noh_atual.pos_x][noh_atual.pos_y] = 5
			imprimir_caminho(Auxiliar)
			
			print(vetor_caminho(caminho))
			
			if teste(noh_atual):
				Auxiliar[noh_atual.pos_x][noh_atual.pos_y] = 3
				Auxiliar[caminho[0].pos_x][caminho[0].pos_y] = 2
				
				imprimir_caminho(Auxiliar)
				
				print("\nCaminho: ")
				Aux = vetor_caminho(caminho)
				print(Aux)
				
				menor_caminho(Aux)
				
				imprimir_caminho(Auxiliar)
				
				print("\n\tCHEGOU NO FINAL!!!!\n")
				print("Custo total = ", len(caminho)-1)
				print("--------------------------------------\n")
				break
				
			else:
				if adicionar(Lista, Pilha, noh_atual) == 0:
					caminho.pop()
					while verifica_caminho(Lista, caminho[-1]) == 0:
						caminho.pop()

#------------------------------------------------------------------------------------------#

def buscaEmLargura(pos_inicial):

	print("\n   Busca em Largura:\n")

	imprimir_caminho(Auxiliar)

	Lista = []
	caminho = []
	
	Fila = []
	Fila.append(pos_inicial)
	
	while len(Fila) > 0:
		noh_atual = Fila.pop(0)
		
		Lista.append(noh_atual.nome)
		print(Lista)
		caminho.append(noh_atual)
		
		Auxiliar[noh_atual.pos_x][noh_atual.pos_y] = 5
		imprimir_caminho(Auxiliar)
		
		if teste(noh_atual):
			Auxiliar[noh_atual.pos_x][noh_atual.pos_y] = 3
			Auxiliar[caminho[0].pos_x][caminho[0].pos_y] = 2
			
			primeiro = caminho[0]
			aux  = caminho[-1]
			Aux = []
			while aux != primeiro:
				Aux.append(aux.nome)
				aux = aux.pai
			Aux.append(aux.nome)
			
			imprimir_caminho(Auxiliar)
			
			print("\nMenor caminho: ")
			print(Aux[::-1])
			
			menor_caminho(Aux)
			
			imprimir_caminho(Auxiliar)
			
			print("\n\tCHEGOU NO FINAL!!!!\n")
			print("Custo total = ", len(Aux)-1)
			print("--------------------------------------\n")
			break

		else:
			if adicionar(Lista, Fila, noh_atual) == 0:
				caminho.pop()

#------------------------------------------------------------------------------------------#

def menor_caminho(Caminho):
	for i in range (0, len(Auxiliar)):
		for j in range (0, len(Auxiliar)):
			if Auxiliar[i][j] == 5 and not procura(Caminho, nome(i,j)):
				Auxiliar[i][j] = 1

#------------------------------------------------------------------------------------------#

def vetor_caminho(caminho):

	Aux = []
	for i in range (0, len(caminho)):
		Aux.append(caminho[i].nome)
		
	return Aux

#------------------------------------------------------------------------------------------#

def verifica_caminho(Lista, noh_atual):
	cont = 0

	if noh_atual.v_cima == True and not procura(Lista, nome(noh_atual.pos_x-1, noh_atual.pos_y)):
		cont +=1

	if noh_atual.v_baixo == True and not procura(Lista, nome(noh_atual.pos_x+1, noh_atual.pos_y)):
		cont +=1

	if noh_atual.v_direita == True and not procura(Lista, nome(noh_atual.pos_x, noh_atual.pos_y+1)):
		cont +=1

	if noh_atual.v_esquerda == True and not procura(Lista, nome(noh_atual.pos_x, noh_atual.pos_y-1)):
		cont +=1
		
	return cont
	
#------------------------------------------------------------------------------------------#

def teste(noh_atual):
	if Labirinto[noh_atual.pos_x][noh_atual.pos_y] == Final:
		return True
	else:
		return False
		
#------------------------------------------------------------------------------------------#

def imprimir_caminho(matriz):
	
	linhas = len(matriz)
	colunas = len(matriz[0])
	
	print(" ____________________ ")
	for i in range(linhas):
		print("|", end="")
		for j in range(colunas):
			if matriz[i][j] == 0:
				print("□ ", end="")
			elif matriz[i][j] == 5:
				print("o ", end="")
			elif matriz[i][j] == 1:
				print("  ", end="")
			elif matriz[i][j] == 2:
				print("# ", end="")
			else:
				print("X ", end="")
		print("|")
	print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
	print()
		
#------------------------------------------------------------------------------------------#

def adicionar(Lista, Estrutura, noh_atual):

	cont = 0

	if noh_atual.v_cima == True and not procura(Lista, nome(noh_atual.pos_x-1, noh_atual.pos_y)):
		pos = Posicao(noh_atual.pos_x-1, noh_atual.pos_y)
		pos.pai = noh_atual
		Estrutura.append(pos)
		cont +=1

	if noh_atual.v_baixo == True and not procura(Lista, nome(noh_atual.pos_x+1, noh_atual.pos_y)):
		pos = Posicao(noh_atual.pos_x+1, noh_atual.pos_y)
		pos.pai = noh_atual
		Estrutura.append(pos)
		cont +=1

	if noh_atual.v_direita == True and not procura(Lista, nome(noh_atual.pos_x, noh_atual.pos_y+1)):
		pos = Posicao(noh_atual.pos_x, noh_atual.pos_y+1)
		pos.pai = noh_atual
		Estrutura.append(pos)
		cont +=1

	if noh_atual.v_esquerda == True and not procura(Lista, nome(noh_atual.pos_x, noh_atual.pos_y-1)):
		pos = Posicao(noh_atual.pos_x, noh_atual.pos_y-1)
		pos.pai = noh_atual
		Estrutura.append(pos)
		cont +=1
		
	return cont

#------------------------------------------------------------------------------------------#

def nome(x, y):
	return x*10 + y

#------------------------------------------------------------------------------------------#

def procura(Lista, dado):
    for i in range(len(Lista)):
        if Lista[i] == dado:
            return True
    return False
    
#------------------------------------------------------------------------------------------#

def ler_labirinto():
	arq = open('labirinto.txt','r')
	v = []

	for line in arq.readlines():
		v.append([int (x) for x in line.split()])
	
	return v

#------------------------------------------------------------------------------------------#

def main():
	global Labirinto, Auxiliar
	 
	Labirinto = ler_labirinto()
	Auxiliar = ler_labirinto()
	
	linha, coluna = encontra_Inicio()
	pos_inicial = Posicao(linha, coluna)
	
	imprimir_caminho(Auxiliar)
	buscaEmProfundidade(pos_inicial)
	
	Auxiliar = ler_labirinto()
	buscaEmLargura(pos_inicial)
	
if __name__ == "__main__":
    main()
