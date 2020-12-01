import tkinter as tk
import pygame as py
from PIL import Image, ImageTk 
import WindowCredit as wc
import WindowsGame as wg
import ControllerHome as ch



def init_winner_game(num):
  windows_winner=tk.Tk()
  windows_winner.geometry("400x200")
  windows_winner.title("Game Over")
  windows_winner.resizable(False,False)
  windows_winner.configure(bg='black')

  if(num==1):
    winner=tk.Label(windows_winner, text="PLAYER 1 WIN!!", fg="red", bg="black", font="Helvetica 16 bold" )
    winner.grid(row=1, column=3, padx=120, pady=30)
  elif (num==2):
    winner=tk.Label(windows_winner, text="PLAYER 2 WIN!!", fg="blue", bg="black", font="Helvetica 16 bold" )
    winner.grid(row=1, column=3, padx=120, pady=30)
  else:
    winner=tk.Label(windows_winner, text="Game ended in a draw! Try again!", fg="blue", bg="black", font="Helvetica 16 bold" )
    winner.grid(row=1, column=3, padx=120, pady=30)
    
 
  

  close_button=tk.Button(windows_winner, text="Close", bg="grey", fg="black", font='Helvetica 14 bold', height=1, width=8, command=windows_winner.destroy )
  close_button.grid(row=3, column=3, padx=120, pady=30)