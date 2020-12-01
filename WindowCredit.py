import tkinter as tk
import pygame as py
from PIL import Image, ImageTk 
import ControllerHome as ch

  # modale credits
def init_gui_credit():
  windows_credit=tk.Toplevel()
  windows_credit.geometry("600x500")
  windows_credit.title("Filetto @Credits")
  windows_credit.resizable(False,False)
  windows_credit.configure(bg="black")
  
  text1="Author: Annalisa Sabatelli"
  text2=" Esame di Interazione Uomo-Macchina a.a. 2020/2021"
  credit_label1=tk.Label(windows_credit, text=text1, fg="white", bg="black", font="Helvetica 14")
  credit_label1.pack( pady=30, side=tk.TOP)
  credit_label2=tk.Label(windows_credit, text=text2, fg="white", bg="black", font="Helvetica 14 bold")
  credit_label2.pack(  side=tk.TOP)

  image = ImageTk.PhotoImage(Image.open('logo_ufficiale_web.jpg'))
  bg_label = tk.Label(windows_credit, image = image)
  bg_label.pack(pady=40,side=tk.TOP)
  bg_label.image = image

  exit_button=tk.Button(windows_credit, text="Close",background="grey", fg="white", font="Helvetica 12 bold", height=1, width=7, command=windows_credit.destroy)
  exit_button.pack(padx=100,pady=20, side=tk.BOTTOM)

  
