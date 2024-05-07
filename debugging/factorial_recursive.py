#!/usr/bin/python3
import sys  # Importation du module sys pour accéder aux arguments de la ligne de command

# Définition de la fonction factorial pour calculer le factoriel d'un nombr
def factorial(n):
    if n == 0: # Cas de base : si n est égal à 0, retourne
        return 1
    else:
        return n * factorial(n-1)  # Récursion : multiplie n par le factoriel de n-

# Appel de la fonction factorial avec l'argument passé en ligne de commande, converti en entie
f = factorial(int(sys.argv[1]))
print(f)
