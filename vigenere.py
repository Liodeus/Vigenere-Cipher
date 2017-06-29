#!/usr/bin/env Python3
# -*- encoding:utf_8 -*-

import Alphabet


def encode(plaintext, keyword):
    plaintextEncode = ""
    i = 0
    for nb in range(0, len(plaintext)):
        if i < len(keyword):
            padding = (Alphabet.alpha[keyword[i]] - 1) + \
                Alphabet.alpha[plaintext[nb]]
            plaintextEncode += Alphabet.beta[padding % 26]
            i += 1

        if i >= len(keyword):
            i = 0

    return plaintextEncode


def decode(plaintext, keyword):
    plaintextEncode = ""
    i = 0
    for nb in range(0, len(plaintext)):
        if i < len(keyword):
            padding = Alphabet.alpha[plaintext[nb]] - (Alphabet.alpha[keyword[i]] - 1)
            if padding < 0:
                padding += 26
            
            plaintextEncode += Alphabet.beta[padding % 26]
            i += 1

        if i >= len(keyword):
            i = 0

    return plaintextEncode


print(encode("THIBAULT", "DEFAULT"))
print(decode("WLNBUFEW", "DEFAULT"))