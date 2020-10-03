import tkinter as tk
import pygame as py
from PIL import Image, ImageTk 
import WindowCredit as wc
import Window_start_game as wsg
import WindowsGame as wg
import Window_start_game as wsg
import Game_logic as gl
import tkinter.messagebox as tm


#open window credit
def print_credit():
  wc.init_gui_credit()

def close_game():
  quit()

def open_win_init_game(player1_name, player2_name,turn, matrix_game,turno):
  wsg.init_start_game(player1_name, player2_name,turn, matrix_game,turno)

def set_new_game (p1,p2, p1_textField, p2_textField, matrix_game, windows_set_players,turn, turno):
  p1.set(p1_textField.get())
  p2.set(p2_textField.get())
  
  for i in range (0,7):
    for j in range (0,7):
      matrix_game[i][j].config(state="normal")
      

  turn.set("Player 1")
  turno.configure(fg="red")
  windows_set_players.destroy()
  return



def play_game(b, i, j, turn, matrix_symbol, points1_tot, points2_tot, turno):
  if(turn.get()=="Player 1"):
    symbol1="X"

    matrix_symbol[i][j].set("X")

    b.config (disabledforeground="red", state=tk.DISABLED)
    points1_tot.set(gl.check_points(matrix_symbol,symbol1))

    if(gl.check_full_matrix(matrix_symbol) or gl.check_win(points1_tot)):
      tm.showinfo("Game Over", "Player1 WIN!!")
    else:  
      turn.set("Player 2")
      turno.configure(fg="blue")
  else: 
    matrix_symbol[i][j].set("O")
    symbol2="O"
    b.config (disabledforeground="blue", state=tk.DISABLED)
    points2_tot.set(gl.check_points(matrix_symbol,symbol2))
    if(gl.check_full_matrix(matrix_symbol) or gl.check_win(points2_tot)):
      tm.showinfo("Game Over", "Player2 WIN!!")
    else:
      turn.set("Player 1")
      turno.configure(fg="red")
  return

def reset_option(matrix_game, matrix_symbol,points1_tot,points2_tot,turn,turno):
  for i in range (0,7):
    for j in range (0,7):
      matrix_symbol[i][j].set("")
      matrix_game[i][j].configure(state="normal")
  points1_tot.set(0)
  points2_tot.set(0)
  turn.set("Player 1")
  turno.configure(fg="red")









  
      
    
  
  

  

