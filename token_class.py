# -*- coding: utf-8 -*-
__author__ = 'ElenaSidorova'

class Token:
    def __init__(self, word):
        self.word = word
        self.old_word = u''
        self.type = None