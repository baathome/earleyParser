"Gera sentencas aleatorias com base nas regras da gramatica lida"

from random import randint
from file_parser import parse

#parse('grammar/harmony.txt')
def generate(grammar, rule):
	"Gera uma sentenca aleatoria"

	i = grammar.ruleindex(rule)
	prodlen = len(grammar.rules[i].production)
	if i == -1 or prodlen == 0:
		print("Erro na gramatica")
		return False
	prod = grammar.rules[i].production[randint(0, prodlen-1)]
	for part in prod:
		if grammar.isterminal(part):
			print(part)
		else:
			generate(grammar, part)


gramm = parse('grammar/test.txt')
generate(gramm, gramm.initial)
