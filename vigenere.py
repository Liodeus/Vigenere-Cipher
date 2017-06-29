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
    plaintextDecode = ""
    i = 0
    for nb in range(0, len(plaintext)):
        if i < len(keyword):
            padding = Alphabet.alpha[plaintext[nb]] - \
                (Alphabet.alpha[keyword[i]] - 1)
            if padding < 0:
                padding += 26

            plaintextDecode += Alphabet.beta[padding % 26]
            i += 1

        if i >= len(keyword):
            i = 0

    return plaintextDecode


if __name__ == "__main__":
    print("[Vigenere, Thibault Galbourdin (github.com/Liodeus)]")
    print("1- Encode")
    print("2- Decode \n")

    choice = input("Choice : ")

    if choice == "1":
        message = input("Plaintext : ")
        keyword = input("Keyword :")
        print(encode(message.upper(), keyword.upper()))
    elif choice == "2":
        message = input("Plaintext : ")
        keyword = input("Keyword :")
        print(decode(message.upper(), keyword.upper()))
    else:
        print("Error")
