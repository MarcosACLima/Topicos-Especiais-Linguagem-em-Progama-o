#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def somaImposto(taxaImposto, custoItem):
    calculaImposto = custoItem + (custoItem*(taxaImposto/100))
    return calculaImposto


taxa = float(input('Informe a taxa do imposto: '))
custo = float(input('Informe o custo do item: '))

print('Valor do produto com imposto: ', somaImposto(taxa, custo))