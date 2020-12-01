import tkinter as tk
import pygame as py
from PIL import Image, ImageTk 
import WindowCredit as wc
import Window_start_game as wsg
import WindowsGame as wg
import Window_start_game as wsg
import Game_logic as gl
import tkinter.messagebox as tm
import Window_winner as ww


#open window credit
def print_credit():
  wc.init_gui_credit()

def close_game():
  quit()

def exitApplication(windows_root):
  MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application?',icon = 'warning')
  if MsgBox == 'yes':
      windows_root.destroy()
  else:
      tk.messagebox.showinfo('Return','You will now return to the application screen')

def open_win_init_game(player1_name, player2_name,turn, matrix_game,turno,matrix_symbol):
     wsg.init_start_game(player1_name, player2_name,turn, matrix_game,turno)
     for i in range (0,7):
      for j in range (0,7):
          matrix_symbol[i][j].set("")
  

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



def play_game(b, i, j, turn, matrix_symbol, points1_tot, points2_tot, turno, window_game,matrix_game):
  if(turn.get()=="Player 1"):
    symbol1="X"

    matrix_symbol[i][j].set("X")

    b.config (disabledforeground="red", state=tk.DISABLED)
    points1_tot.set(gl.check_points(matrix_symbol,symbol1))

    if((gl.check_full_matrix(matrix_symbol) and (points1_tot>points2_tot)) or gl.check_win(points1_tot)):
      #tm.showinfo("Game Over", "Player1 WIN!!")
       ww.init_winner_game(1)
       for i in range (0,7):
        for j in range (0,7):
          matrix_game[i][j].config(state="disabled")
    elif (gl.check_full_matrix(matrix_symbol) and (points1_tot==points2_tot)):
       ww.init_winner_game(3)
    else:  
      turn.set("Player 2")
      turno.configure(fg="blue")
  else: 
    matrix_symbol[i][j].set("O")
    symbol2="O"
    b.config (disabledforeground="blue", state=tk.DISABLED)
    points2_tot.set(gl.check_points(matrix_symbol,symbol2))
    if((gl.check_full_matrix(matrix_symbol) and (points2_tot>points1_tot)) or gl.check_win(points2_tot)):
      #tm.showinfo("Game Over", "Player2 WIN!!" , parent=window_game)
      ww.init_winner_game(2)
      for i in range (0,7):
        for j in range (0,7):
          matrix_game[i][j].config(state="disabled")
    elif (gl.check_full_matrix(matrix_symbol) and (points1_tot==points2_tot)):
       ww.init_winner_game(3)
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









  
      
    
  
  

  

