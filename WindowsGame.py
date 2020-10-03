import tkinter as tk
import pygame as py
from PIL import Image, ImageTk 
import ControllerHome as ch
import tkinter.messagebox
import numpy as ny
import Window_start_game as wsg





def main():
  window_game=tk.Tk()
  matrix_game=[]
  player1_name = tk.StringVar()
  player1_name.set("Input name")
  player2_name = tk.StringVar()
  turn=tk.StringVar()
  turn.set("Press New Game to start")
  player2_name.set("Input name")
  points1_tot = tk.IntVar()
  points1_tot.set(0)
  points2_tot = tk.IntVar()
  points2_tot.set(0)
  matrix_symbol=[]
 
  window_game.geometry("900x785")
  window_game.title("Filetto Game")
  window_game.configure(bg='black')
  window_game.resizable(False,False)

#Player 1
  player1=tk.Label(window_game, text="X  Player1:", fg="red", bg="black", relief="solid", font="Helvetica 14 bold" )
  player1_name_label=tk.Label(window_game, textvariable=player1_name, fg="red", bg="black", relief="solid", font=("Helvetica", 14))
  player1_name_label.place(x=500, y=10)
  player1.place(x=380, y=10)
  punti1_label=tk.Label(window_game, text="Points Player 1:", fg="red", bg="black", relief="solid", font="Helvetica 14 bold")
  punti1_label.place(x=650, y=10)
  punti1_tot=tk.Label(window_game, textvariable=points1_tot, fg="red", bg="black", relief="solid", font=("Helvetica", 14))
  punti1_tot.place(x=830, y=10)

  #Player 2
  player2=tk.Label(window_game, text="O  Player2:", fg="blue", bg="black", relief="solid", font="Helvetica 14 bold")
  player2_name_label=tk.Label(window_game, textvariable=player2_name, fg="blue", bg="black", relief="solid", font=("Helvetica", 14))
  player2_name_label.place(x=500, y=50)
  player2.place(x=380, y=50)
  punti2_label=tk.Label(window_game, text="Points Player 2:", fg="blue", bg="black", relief="solid", font="Helvetica 14 bold")
  punti2_label.place(x=650, y=50)
  punti2_tot=tk.Label(window_game, textvariable=points2_tot, fg="blue", bg="black", relief="solid", font="Helvetica 14")
  punti2_tot.place(x=830, y=50)

  #Turno
  turno_label=tk.Label(window_game, text="Turn:", fg="white", bg="black", relief="solid", font="Helvetica 14 bold")
  turno_label.place(x=20, y=30)
  turno=tk.Label(window_game, textvariable=turn, fg="white", bg="black", relief="solid", font="Helvetica 14 bold")
  turno.place(x=100, y=30)

  #button
  new_game=tk.Button(window_game, text="New Game", bg="grey", fg="black", font='Helvetica 14 bold', height=1, width=9, command= lambda : ch.open_win_init_game(player1_name, player2_name,turn, matrix_game,turno))
  new_game.place(x=680, y=150)
  reset=tk.Button(window_game, text="Reset Game", bg="grey", fg="black", font='Helvetica 14 bold', height=1, width=9, command= lambda : ch.reset_option(matrix_game, matrix_symbol,points1_tot,points2_tot,turn,turno))
  reset.place(x=680, y=210)
  close=tk.Button(window_game, text="Close", bg="grey", fg="black", font='Helvetica 14 bold', height=1, width=9, command=window_game.destroy)
  close.place(x=680, y=270)

  #scacchiera
  label=tk.Label(window_game)
  label.pack(side=tk.LEFT, fill="y", pady=100, padx=20)
  for index1 in range (0,7):
    row_symbol= []
    for index2 in range (0,7):
      symbol=tk.StringVar()
      row_symbol.append(symbol)
    matrix_symbol.append(row_symbol)

  for index1 in range (0,7):
    row = []
    for index2 in range (0,7):
      b = tk.Button(label, textvariable=matrix_symbol[index1][index2], bg="grey", font='Helvetica 14 bold', state=tk.DISABLED, height=3, width=6)
      b.grid(row=index1,column=index2)
      row.append(b)
    matrix_game.append(row)
  for i in range (0,7):
    for j in range (0,7):
      mg=matrix_game[i][j]
      mg.configure(command=lambda i=i, j=j,  button=mg: ch.play_game(button, i, j, turn, matrix_symbol, points1_tot, points2_tot,turno)) 
 
  window_game.mainloop()

  

  


if __name__ == "__main__":
    main()
