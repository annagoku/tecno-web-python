import tkinter as tk
import pygame as py
from PIL import Image, ImageTk 
import WindowCredit as wc
import WindowsGame as wg
import ControllerHome as ch



def init_start_game(p1, p2,turn, matrix_game, turno):
  windows_set_players=tk.Tk()
  window_height = 200
  window_width = 400
  windows_set_players.title("Filetto Game - Set Players")
  windows_set_players.resizable(False,False)
  windows_set_players.configure(bg='black')

  screen_width = windows_set_players.winfo_screenwidth()
  screen_height = windows_set_players.winfo_screenheight()

  x_cordinate = int((screen_width/2) - (window_width/2))
  y_cordinate = int((screen_height/2) - (window_height/2))

  windows_set_players.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


  player1=tk.Label(windows_set_players, text="X  Player1:", fg="red", bg="black", font="Helvetica 14 bold" )
  player1.grid(row=1, column=1, padx=10, pady=20)
  player1_textField=tk.Entry(windows_set_players, textvariable=p1, bd=5)
  player1_textField.grid(row=1, column=2, pady=20)

  player2=tk.Label(windows_set_players, text="O  Player2:", fg="blue",bg="black", font="Helvetica 14 bold" )
  player2.grid(row=2, column=1, padx=10)
  player2_textField=tk.Entry(windows_set_players, textvariable=p2, bd=5)
  player2_textField.grid(row=2, column=2)

  

  start_button=tk.Button(windows_set_players, text="Start", bg="grey", fg="black", font='Helvetica 14 bold', height=1, width=8, command=lambda : ch.set_new_game(p1,p2,player1_textField, player2_textField, matrix_game, windows_set_players,turn,turno) )
  start_button.grid(row=3, column=2, padx=75, pady=30)

  

