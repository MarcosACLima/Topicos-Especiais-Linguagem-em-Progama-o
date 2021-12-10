#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calcularMedia(nota1, nota2):
    media = 0
    media = (nota1 + nota2)/2
    return media

def informarStatus(media):
    status = ''
    if media > 6:
        status = 'Aprovado'
    elif media > 4:
        status = 'Verificação Suplementar'
    else:
        status = 'Reprovado'
    return status


nota1 = float(input('Informe uma nota 1: '))
nota2 = float(input('Informe uma nota 2: '))
print()

media = calcularMedia(nota1, nota2)
status = informarStatus(media)

print('Média do aluno: ', media)
print('Status do aluno: ', status)