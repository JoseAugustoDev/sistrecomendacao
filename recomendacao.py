avaliacoesUsuario = {'Ana': 
		{'Freddy x Jason': 2.5, 
		 'O Ultimato Bourne': 3.5,
		 'Star Trek': 3.0, 
		 'Exterminador do Futuro': 3.5, 
		 'Norbit': 2.5, 
		 'Star Wars': 3.0},
	 
	  'Marcos': 
		{'Freddy x Jason': 3.0, 
		 'O Ultimato Bourne': 3.5, 
		 'Star Trek': 1.5, 
		 'Exterminador do Futuro': 5.0, 
		 'Star Wars': 3.0, 
		 'Norbit': 3.5}, 

	  'Pedro': 
	    {'Freddy x Jason': 2.5, 
		 'O Ultimato Bourne': 3.0,
		 'Exterminador do Futuro': 3.5, 
		 'Star Wars': 4.0},
			 
	  'Claudia': 
		{'O Ultimato Bourne': 3.5, 
		 'Star Trek': 3.0,
		 'Star Wars': 4.5, 
		 'Exterminador do Futuro': 4.0, 
		 'Norbit': 2.5},
				 
	  'Adriano': 
		{'Freddy x Jason': 3.0, 
		 'O Ultimato Bourne': 4.0, 
		 'Star Trek': 2.0, 
		 'Exterminador do Futuro': 3.0, 
		 'Star Wars': 3.0,
		 'Norbit': 2.0}, 

	  'Janaina': 
	     {'Freddy x Jason': 3.0, 
	      'O Ultimato Bourne': 4.0,
	      'Star Wars': 3.0, 
	      'Exterminador do Futuro': 5.0, 
	      'Norbit': 3.5},
			  
	  'Leonardo': 
	    {'O Ultimato Bourne':4.5,
             'Norbit':1.0,
	     'Exterminador do Futuro':4.0}
}

avaliacoesFilme = {'Freddy x Jason': 
		{'Ana': 2.5, 
		 'Marcos:': 3.0 ,
		 'Pedro': 2.5, 
		 'Adriano': 3.0, 
		 'Janaina': 3.0 },
	 
	 'O Ultimato Bourne': 
		{'Ana': 3.5, 
		 'Marcos': 3.5,
		 'Pedro': 3.0, 
		 'Claudia': 3.5, 
		 'Adriano': 4.0, 
		 'Janaina': 4.0,
		 'Leonardo': 4.5 },
				 
	 'Star Trek': 
		{'Ana': 3.0, 
		 'Marcos:': 1.5,
		 'Claudia': 3.0, 
		 'Adriano': 2.0 },
	
	 'Exterminador do Futuro': 
		{'Ana': 3.5, 
		 'Marcos:': 5.0 ,
		 'Pedro': 3.5, 
		 'Claudia': 4.0, 
		 'Adriano': 3.0, 
		 'Janaina': 5.0,
		 'Leonardo': 4.0},
				 
	 'Norbit': 
		{'Ana': 2.5, 
		 'Marcos:': 3.0 ,
		 'Claudia': 2.5, 
		 'Adriano': 2.0, 
		 'Janaina': 3.5,
		 'Leonardo': 1.0},
				 
	 'Star Wars': 
		{'Ana': 3.0, 
		 'Marcos:': 3.5,
		 'Pedro': 4.0, 
		 'Claudia': 4.5, 
		 'Adriano': 3.0, 
		 'Janaina': 3.0}
}

from math import sqrt

def euclidiana(base, usuario1, usuario2):
	si = {}
	for item in base[usuario1]:
		if item in base[usuario2]: si[item] = 1

	if len(si) == 0: return 0

	soma = sum([pow(base[usuario1][item] - base[usuario2][item], 2)
		for item in base[usuario1] if item in base[usuario2]])
	return 1/(1 + sqrt(soma))

# print(euclidiana(avaliacoesFilme, 'Star Wars', 'Star Trek'))

def getSimilares(base, usuario):
	similaridade = [(euclidiana(base, usuario, outro), outro)
		for outro in base if outro != usuario]
	similaridade.sort()
	similaridade.reverse()
	return similaridade[0:30]

# print(getSimilares(avaliacoesFilme, 'Star Wars'))

def getRecomendacoesUsuario(base, usuario):
	totais = {}
	somarSimilaridade = {}
	for outro in base:
		if outro == usuario: continue
		similaridade = euclidiana(base, usuario, outro)

		if similaridade <= 0: continue

		for item in base[outro]:
			if item not in base[usuario]:
				totais.setdefault(item, 0)
				totais[item] += base[outro][item] * similaridade
				somarSimilaridade.setdefault(item, 0)
				somarSimilaridade[item] += similaridade
	rankings = [(total / somarSimilaridade[item], item) for item, total in totais.items()]
	rankings.sort()
	rankings.reverse()
	return rankings[0:30]

# print(getRecomendacoesUsuario(avaliacoesFilme, 'Star Wars'))

def carregarMovieLens(path='C:/ml-100k'):
	filmes = {}
	for linha in open(path + '/u.item'):
		(id, titulo) = linha.split('|')[0 : 2]
		filmes[id] = titulo
	# print(filmes)

	base = {}
	for linha in open(path + '/u.data'):
		(usuario, idFilme, nota, tempo) = linha.split('\t')
		base.setdefault(usuario, {})
		base[usuario][filmes[idFilme]] = float(nota)

	return base

baseDados = carregarMovieLens()

# print(getSimilares(baseDados, '69'))
# [(1.0, '369'), (1.0, '273'), (1.0, '147'), (0.5, '98'), (0.5, '914'), (0.5, '855'), (0.5, '822'), (0.5, '613'), (0.5, '558'),
#  (0.5, '51'), (0.5, '212'), (0.4142135623730951, '849'), (0.4142135623730951, '769'), (0.4142135623730951, '713'), (0.4142135623730951, '571'),
#  (0.4142135623730951, '522'), (0.4142135623730951, '516'), (0.4142135623730951, '419'), (0.4142135623730951, '341'), (0.36602540378443865, '754'),
#  (0.36602540378443865, '720'), (0.36602540378443865, '656'), (0.36602540378443865, '375'), (0.36602540378443865, '37'), (0.36602540378443865, '266'),
#  (0.36602540378443865, '237'), (0.36602540378443865, '195'), (0.36602540378443865, '131'), (0.36602540378443865, '111'), (0.3333333333333333, '797')]


# print(getRecomendacoesUsuario(baseDados, '123'))
# [(5.0, 'They Made Me a Criminal (1939)'), (5.0, 'Star Kid (1997)'), (5.0, "Someone Else's America (1995)"), (5.0, 'Santa with Muscles (1996)'),
#  (5.0, 'Saint of Fort Washington, The (1993)'), (5.0, 'Marlene Dietrich: Shadow and Light (1996) '), (5.0, 'Great Day in Harlem, A (1994)'),
#  (5.0, 'Entertaining Angels: The Dorothy Day Story (1996)'), (5.0, 'Aiqing wansui (1994)'), (4.999999999999999, 'Prefontaine (1997)'),
#  (4.711343314961116, 'Pather Panchali (1955)'), (4.624591660602442, 'Maya Lin: A Strong Clear Vision (1994)'), (4.615785936667204, 'Cosi (1996)'),
#  (4.570484630206703, 'Letter From Death Row, A (1998)'), (4.5550514374428, 'Anna (1996)'), (4.54046043898935, "Some Mother's Son (1996)"),
#  (4.5050650574670446, 'Close Shave, A (1995)'), (4.481624190895886, 'Stonewall (1995)'), (4.462545651611139, "Schindler's List (1993)"),
#  (4.448556642828158, 'Wrong Trousers, The (1993)'), (4.447048913217506, 'Faust (1994)'), (4.430140531410556, 'Wallace & Gromit: The Best of Aardman Animation (1996)'),
#  (4.423466435631001, 'Innocents, The (1961)'), (4.413249446731089, 'Third Man, The (1949)'), (4.3868173051739925, 'Rear Window (1954)'), (4.376004286089687, 'Everest (1998)'),
#  (4.374196329748927, 'Usual Suspects, The (1995)'), (4.355420220228099, '12 Angry Men (1957)'), (4.333823801893741, 'Bitter Sugar (Azucar Amargo) (1996)'),
#  (4.303580887528068, 'Shall We Dance? (1996)')]

def calculaItensSimilares(base):
	result = {}
	for item in base:
		notas = getSimilares(base, item)
		result[item] = notas
	return result

itensSimilares = calculaItensSimilares(avaliacoesFilme)

# print(itensSimilares)

def getRecomendacoesItens(baseUsuario, similaridadeItens, usuario):
	notasUsuario = baseUsuario[usuario]
	notas = {}
	totalSimilaridade = {}
	for (item, nota) in notasUsuario.items():
		for (similaridade, item2) in similaridadeItens[item]:
			if item2 in notasUsuario: continue
			notas.setdefault(item2, 0)
			notas[item2] += similaridade * nota
			totalSimilaridade.setdefault(item2, 0)
			totalSimilaridade[item2] += similaridade
	rankings = [(score/totalSimilaridade[item], item) for item, score in notas.items()]
	rankings.sort()
	rankings.reverse()
	return rankings

listaItens = calculaItensSimilares(avaliacoesFilme)

# print(getRecomendacoesItens(avaliacoesUsuario, listaItens, 'Pedro'))
