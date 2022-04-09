#-*- coding: utf-8 -*-
nome = "Daniel"
sobrenome = "Gusmao"
string_dgp = "A maior honra do homem é conhecer a Deus"
lista_dgp = string_dgp.split()
lista_dgp2 = string_dgp.split("h")
busca = string_dgp.find("Deus")
string_dgp = string_dgp.replace("a Deus","ao Senhor")

concatenar = (nome+" "+sobrenome+ "\n")

tamanho = len(concatenar)

print(tamanho)

#Imprime em minúsculo

print(concatenar.lower())

#Imprime em maiusculo

print(concatenar.upper())

#Remove quebra de linha

print(concatenar.strip())

#Converte string em lista

print(lista_dgp)

#Separa sem a letra em parênteses

print(lista_dgp2)

#Em que posição aparece a palavra "Deus"

print(busca)

#Imprimir da busca em diante

print(string_dgp[busca:])

#Substitui as palavras

print(string_dgp)