#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import nltk.data

def main():
    tokenizer = nltk.data.load('tokenizers/punkt/PY3/portuguese.pickle')
    para = "Olá, esta é uma sentença em português. Este é apenas mais um teste. Olá! Como você está? Eu vou bem."
    print(tokenizer.tokenize(para))

if __name__ == '__main__':
    main()
