#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def receberNotas(aluno):
    listaDeNotas = []
    for nota in range(4):
        valor = float(input(print('Informe a ', nota+1, '° nota do aluno ', aluno+1, ': ')))
        listaDeNotas.append(valor)
    print('\nNotas: ', listaDeNotas, '\n')
    return listaDeNotas

def calcularMedia(listaDeNotas):
    media = 0
    soma = 0
    for nota in listaDeNotas:
        soma += nota
    media = soma / len(listaDeNotas)
    return media

def imprimirLista(lista):
    contador = 1
    for valor in lista:
        print('Média do Aluno', contador, ": %.1f" % valor)
        contador += 1

def receberNotasDosAlunos():
    listaDeMedias = []
    for aluno in range(2):
        media = calcularMedia(receberNotas(aluno))
        print('Média: %.1f' % media)
        print('\n_____________________________________\n')
        listaDeMedias.append(media)
    return listaDeMedias


def quantidadeAlunosAprovados(listaDeNotas):
    quantidadeAprovados = 0
    for nota in listaDeNotas:
        if(nota >= 7):
            quantidadeAprovados += 1
    return quantidadeAprovados


listaDeMedias = receberNotasDosAlunos()
quantidadeAprovados = quantidadeAlunosAprovados(listaDeMedias)
print('----- Resultado dos Alunos -----\n\nLista de médias:\n')
imprimirLista(listaDeMedias)
print('\nQuantidade de alunos que obtiveram média maior ou igual a 7: ', quantidadeAprovados)
