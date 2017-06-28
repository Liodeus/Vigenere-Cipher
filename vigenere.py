#!/usr/bin/env Python3
# -*- encoding:utf_8 -*-

import Alphabet

keyword = "DEFAULT"
plaintext = "JOLIE"

padding = (Alphabet.alpha[keyword[0]] - 1) + Alphabet.alpha[plaintext[0]]


ciphertext = ""
for nb in range(0, len(plaintext)):
    padding = (Alphabet.alpha[keyword[nb]] - 1) + Alphabet.alpha[plaintext[nb]]
    ciphertext += Alphabet.beta[padding]

print(ciphertext)
