# JOGO DA FORCA #
'''
Nesse exercício você deverá programar o jogo da FORCA, apra isso necessariamente você deverá ter:
	1) Uma lista 'forca' de strings com os vários desenhos em formato texto 
	(esqueça bibliotecas gráficas, foque no desenvolvimento do código)
	Dependendo do número de desenhos a pessoa terá mais ou menos chances para 	
	acertar. Use aspas triplas e sua criatividade para os desenhos.
	Dica: boneco do lado esquerdo da forca.

	2) Duas strings que chamaremos de certas e erradas que irão acumulando os chutes
	certos e errados sem repetição.
	Não utilize listas para armazenar os chutes, mas strings.
	Sua única lista será a que guarda os desenhos.

	3) Função sorteia(). Retorna uma palavra sorteada do dicionário em português. 		Poderá ser acessado em www.ime.usp.br/~pf/algoritmos/dicios/br.
	Você deve fazer uma leitura de todas as palavras na primeira vez e não deverá
	mais acessar o site nas próximas jogadas. 
	Para ler as palavras do site utilize decode('iso8859').

	4) Função desenha(). Imprime o desenho da FORCA correspondente ao número
	 de letras erradas e corretas até o momento. Exemplo:

	+-------+
	|	|
	O	|
       /|\	|
       / 	|
		|
      ============

	e _ e m p _ o
	
	Chute uma letra:

	5) Função chute(letras). Recebe como parâmetro uma string com todas as letras
	já tentadas (certas + erradas). Devolve uma letra minúscula que não foi tentada
	antes. 
	Faz consistência se a pessoa digitou uma letra e não um número.

	6) Função again(). Pergunta se a pessoa quer jogar de novo. Você deverá aceitar
	maiúsculas ou minúsculas na resposta.

	7) Função win(). Retorna True caso todas as letras da palavra sorteada estejam
	na string certas.
	
