import tkinter as tk
import pygame as py
from PIL import Image, ImageTk 
import ControllerHome as ch
import WindowsGame as wg




def init_gui():

  # finestra principale
  windows_root=tk.Tk()
  window_height = 700
  window_width = 900
  windows_root.title("Filetto")
  windows_root.configure(bg='black')
  windows_root.resizable(False,False)
  screen_width = windows_root.winfo_screenwidth()
  screen_height = windows_root.winfo_screenheight()

  x_cordinate = int((screen_width/2) - (window_width/2))
  y_cordinate = int((screen_height/2) - (window_height/2))

  windows_root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

  welcome_text="Welcome on Filetto!"
  welcome=tk.Label(windows_root, text=welcome_text, fg="blue", bg="black", font="Helvetica 30 bold")
  welcome.pack(pady= 20, side=tk.TOP)


  image = ImageTk.PhotoImage(Image.open('prima immagine.jpg'))
  bg_label = tk.Label(windows_root, image = image)
  bg_label.pack(pady= 50, side=tk.TOP)
  bg_label.image = image


  start_button=tk.Button(windows_root, text="Start Game",background="red", fg="white", font="Helvetica 14 bold",  height=2, width=10, command= lambda: wg.init_gui_field_game(windows_root))
  start_button.place(x=30,y=170)
  quit_button=tk.Button(windows_root, text="Quit",background="red", fg="white", font="Helvetica 14 bold", height=2, width=10, command= lambda : ch.exitApplication(windows_root))
  quit_button.place(x=30, y=270)


  
  credits_button=tk.Button(windows_root, text="@Credits", background="blue", fg="white", font="Helvetica 14 bold", height=2, width=10, command=ch.print_credit)
  credits_button.pack(padx=100, pady=70, side=tk.BOTTOM)

  windows_root.mainloop()

if __name__ == "__main__":
    init_gui()
    

  

    










