# -*- coding: utf-8 -*-
"""Coding activity 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gh8pxaVEzgOg2JFvIf0bGAv2_YyhlsV8
"""

import numpy as np

class Game:
  def __init__(self, r, c):
    self.r = r
    self.c = c
    self.boardA = np.random.rand(r,c)
    self.boardL = [['_'] * c for i in range(r)]

  def __str__(self):
    return self(self.boardA)

  def play(self):
    rows = int(input("how many rows? ")) -1
    cols = int(input("how many columns? ")) -1
    if self.boardA[rows][cols] < 0:
      print("Bomb found")
      print(self)
    else: 
      proceed = input("no bomb detected. \nContinue? Y/N")
      if proceed.lower() == 'Y':
        self.play()
      else:
        print("bye")
        print(self)
        
    rows = int(input("how many rows "))
    cols = int(input("how many columns? "))

    x = Game(rows, cols)
    x.play()

def eraser(paper):

  finishes_paper = ""
  get_rid = [["(", ")", ",", ".", "!", "?", "\'", "/", "[", "]","*", "\""]]

  for char in paper:
    if char not in get_rid:
      finishes_paper += char

  return finishes_paper

def isNumber(word):
  for char in word:
    if not char.isdigit():
      return False
  return True

def wordcount(paper):
  words = paper.lower().split(" ")
  sentance = {}
  for word in words:
    if not isNumber(word):
      if word in sentance:
        sentance[word] += 1
      else:
        sentance[word] = 1
  print(sentance)


sent = input("Enter a sentance? ")
print(isNumber("50"))
wordcount(eraser(sent))