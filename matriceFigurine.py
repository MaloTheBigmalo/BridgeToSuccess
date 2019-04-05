# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 10:36:25 2019

@author: edjo
"""

from random import randint
import numpy as np


def numbers_to_strings(argument):
    switcher = {
            0:"Figurine Absente",
            1:"Lloris",
            2:"Parvar",
            3:"Umtiti",
            4:"Hernandez",
            5:"Varane",
            6:"Kanté",
            7:"Griezman",
            8:"Pogba",
            9:"Girou",
            10:"Mbappé",
            11:"Matuidi"
            }
    return switcher.get(argument, "nothing")

def factoriel(n):
    if n == 0:
        return 1
    else:
        return n*factoriel(n-1)

def zeros(a,b):
    A = np.array([0*x for x in range(a,b)])
    return A

def afficher(A):
    for i in range(np.size(A)):
        print("Figurine n° {:2d} --> {}".format(i,numbers_to_strings(A[i])))

def prod(A):
    resultat = 1
    for i in range(np.size(A)):
        resultat *= A[i]
    return resultat

n = 0
M = zeros(0,11)
afficher(M)
while prod(M) < factoriel(np.size(M)): # J'ai changé cette ligne en utilisant factoriel de 11 (voir c'est que c'est factoriel)
   fig = randint(1,11)
   pos = fig - 1
   if M[pos] == 0:
       M[pos] = fig
   n = n + 1
   print("pour n = ",n)
   afficher(M) # J'ai changé aussi afficher pour qu'il tienne compte du nom de jouer par rapport à leur numéro de figurine


