import tkinter as tk
import pygame as py
from PIL import Image, ImageTk 
import WindowCredit as wc
import Window_start_game as wsg
import WindowsGame as wg
import ControllerHome as ch
import numpy as ny


def check_points (matrix_symbol, symbol_to_count):
  print("controllo punteggio "+ symbol_to_count)
  tot_points_player=tk.IntVar()
  tot_points_row=check_points_row(matrix_symbol, symbol_to_count).get()
  tot_points_column=check_points_column(matrix_symbol,  symbol_to_count).get()
  tot_points_main_diagonal=check_points_main_diagonal(matrix_symbol,  symbol_to_count).get()
  tot_points_secondary_diagonal=check_points_secondary_diagonal(matrix_symbol, symbol_to_count).get()

  tot_points_player.set(tot_points_row+tot_points_column+tot_points_main_diagonal+tot_points_secondary_diagonal)

  return tot_points_player.get()



def check_points_row(matrix_symbol, symbol_to_count):
  points_player=tk.IntVar()
  points_player.set(0)
  count_symbol_player=0
  for i in range (0,7): # check per righe
    count_symbol_player=0
    for j in range (0,7):
      if(matrix_symbol[i][j].get()==symbol_to_count):
        count_symbol_player=count_symbol_player+1
      else:
        points_player.set(points_player.get()+get_points(count_symbol_player))
        count_symbol_player=0
    if(count_symbol_player>=3):
      points_player.set(points_player.get()+get_points(count_symbol_player))
      count_symbol_player=0
  print("row " +str(points_player.get()))

  return points_player

def check_points_column(matrix_symbol, symbol_to_count):
  points_player=tk.IntVar()
  points_player.set(0)
  count_symbol_player=0
  for i in range (0,7): # check per righe
    count_symbol_player=0
    for j in range (0,7):
      if(matrix_symbol[j][i].get()==symbol_to_count):
        count_symbol_player=count_symbol_player+1
      else:
        points_player.set(points_player.get()+get_points(count_symbol_player))
        count_symbol_player=0
    if(count_symbol_player>=3):
      points_player.set(points_player.get()+get_points(count_symbol_player))
      count_symbol_player=0
  print("column " +str(points_player.get()))
  return points_player

def check_points_secondary_diagonal(matrix_symbol, symbol_to_count):
  points_player=tk.IntVar()
  points_player.set(0)
  count_symbol_player=0

  
  way=2
  while (way>0):
    for j in range (0,7,1):
      if(way==2):
        k=j
        z=0
      if(way==1):
        z=j+1
        k=6
      if(way==1 and z==7):
        continue
      count_symbol_player=0
      while (k>=0 and z>=0 and k<7 and z<7):
        if(matrix_symbol[z][k].get()==symbol_to_count):
          count_symbol_player=count_symbol_player+1
        else:
          points_player.set(points_player.get()+get_points(count_symbol_player))
          count_symbol_player=0
        k=k-1
        z=z+1
      if(count_symbol_player>=3):
        points_player.set(points_player.get()+get_points(count_symbol_player))
        count_symbol_player=0
    way=way-1
  print("secondary " +str(points_player.get()))
  return points_player


def get_points(count_symbol_player):
  if (count_symbol_player==3):
    return 3
  elif (count_symbol_player==4):
    return 4
  elif (count_symbol_player>=5):
    return 50
  else:
    return 0

def check_points_main_diagonal(matrix_symbol, symbol_to_count):
  points_player=tk.IntVar()
  points_player.set(0)
  count_symbol_player=0

  way=2
  while (way>0):
    for j in range (0,7,1):
      if(way==2):
        z=6-j
        k=0
      if(way==1):
        k=j+1
        z=0
      if(way==1 and z==7):
        continue
        
      while (k>=0 and z>=0 and k<7 and z<7):
        if(matrix_symbol[z][k].get()==symbol_to_count):
          count_symbol_player=count_symbol_player+1
        else:
          points_player.set(points_player.get()+get_points(count_symbol_player))
          count_symbol_player=0
        k=k+1
        z=z+1
      if(count_symbol_player>=3):
        points_player.set(points_player.get()+get_points(count_symbol_player))
        count_symbol_player=0
    way=way-1
  print("main " + str(points_player.get()))
  return points_player


def check_full_matrix(matrix_symbol):
  full=False
  count=0
  for i in range (0,7):
    for j in range (0,7):
      if(matrix_symbol[i][j].get()=="X" or matrix_symbol[i][j].get()=="O"):
        count=count+1
  if (count== (len(matrix_symbol)*len(matrix_symbol))):
    full=True
  return full

def check_win (player_points):
  winner=False
  if(player_points.get()>=50):
    winner=True
  return winner
