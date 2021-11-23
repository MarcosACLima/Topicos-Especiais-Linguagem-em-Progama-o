def somaImposto(taxaImposto, custoItem):
    calculaImposto = custoItem + (custoItem*(taxaImposto/100))
    return calculaImposto


print(somaImposto(100, 35.50))


