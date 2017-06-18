"""Le arquivo de gramatica no padrao especificado e constroi
estrutura de dados para representa-la no algoritmo de Earley"""

import os.path

class Grammar:
	"Armazena terminais, variaveis e regras"
	terminals = []
	vars = []
	initial = ""

	class Rule:
		"Define formato das regras"
		var = ""
		production = []

	rules = []

	def ruleindex(self, var):
		"Retorna index tal que rules[index].var == var. Caso nao se possa satisfazer a condicao, retorna -1"
		for index, item in enumerate(self.rules):
			if item.var == var:
				return index
		return -1

	def print(self):
		"Imprime valores da gramatica"
		print("Terminals:")
		print(self.terminals)
		print("")
		print("Variables:")
		print(self.vars)
		print("")
		print("Initial:")
		print(self.initial)
		print("")
		print("Rules:")
		for rule in self.rules:
			print("")
			print(rule.var)
			for prod in rule.production:
				print(prod)


def readfile(file):
	"Le conteudo de file e retorna o conteudo ou false, caso o arquivo nao exista"
	if not os.path.isfile(file):
		return False
	with open(file, encoding='utf-8') as f:
		return f.read().split('\n')

def parse(content):
	"Converte o conteudo do arquivo em Grammar e retorna o objeto"
	if not content: #readfile retornou falso
		return False
	grammar = Grammar()
	for i in range(0, len(content)):
		line = content[i]
		line = line.split("#")[0].strip() #desconsidera tudo que vem apos o caractere indicativo de comentario
		if line != "": #linha vazia ou totalmente comentada
			if line.lower() == "terminais":
				i += 1
				while i < len(content) and content[i][:9].lower() != "variaveis": #le todos os terminais
					if content[i][0] == '[':
						grammar.terminals.append(content[i].split(']')[0][2:-1]) #adiciona a lista de terminais, cortando os colchetes e espacos conforme padrao do arquivo de gramatica
					i += 1
				i -= 1
			elif line.lower() == "variaveis":
				i += 1
				while i < len(content) and content[i][:7].lower() != "inicial": #le todas as variaveis
					if content[i][0] == '[':
						grammar.vars.append(content[i].split(']')[0][2:-1]) #adiciona a lista de variaveis, cortando os colchetes e espacos conforme padrao do arquivo de gramatica
					i += 1
				i -= 1
			elif line.lower() == "inicial":
				i += 1
				while i < len(content) and content[i][:6].lower() != "regras": #le variavel inicial
					if content[i][0] == '[':
						grammar.initial = content[i].split(']')[0][2:-1] #atribui valor, cortando os colchetes e espacos conforme padrao do arquivo de gramatica
					i += 1
				i -= 1
			elif line.lower() == "regras":
				i += 1
				while i < len(content): #le todas as regras
					if content[i][0] == '[':
						rule = content[i].split('#')[0].strip()[2:-1] #remove comentarios e espacos desnecessarios no fim

						rule = rule.replace("[", "").replace("]", "").replace("  ", "") #padroniza formato das regras para posterior insercao na lista

						index = grammar.ruleindex(rule.split('>')[0])

						if index != -1: #se ja existe regra partindo da mesma variavel
							grammar.rules[index].production.append(list(filter(None, rule.split('>')[1].split(' ')))) #adiciona regra a lista de regras saindo da variavel

						else: #se nao existe regra partindo da variavel
							x = Grammar.Rule() #cria nova lista de regras
							x.var = rule.split('>')[0] #atribui a variavel a lista de regras
							x.production = [list(filter(None, rule.split('>')[1].split(' ')))] #atribui valor inicial a lista de producoes

							grammar.rules.append(x) #salva nova regra

					i += 1
				i -= 1

	grammar.print()

parse(readfile('grammar/harmony.txt'))
