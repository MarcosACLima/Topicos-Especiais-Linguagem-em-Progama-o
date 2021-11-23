#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def quantidadeDigitos(numero):
    return len((str(numero)))


n = str(input('Digite um número: ')).strip()

print('Quantidade de digitos: ', quantidadeDigitos(n))