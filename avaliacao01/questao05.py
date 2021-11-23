#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def notaValida(nota):
	n=nota
	while (n>10) or (n<0):
		print('Valor da nota inválido')
		n=float(input('Informe uma nota de 0 a 10: '))
	return n

nota = float(input('Informe uma nota de 0 a 10: '))
print('Valor da nota vãlida: ', notaValida(nota))