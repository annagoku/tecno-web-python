import tkinter as tk
import pygame as py
from PIL import Image, ImageTk 
import ControllerHome as ch

  # modale credits
def init_gui_credit():
  windows_credit=tk.Tk()
  windows_credit.geometry("450x300")
  windows_credit.title("Filetto @Credits")
  windows_credit.resizable(False,False)
  windows_credit.configure(bg="grey")
  
  text1="Author: Annalisa Sabatelli"
  text2=" Esame di Tecnologie Web a.a. 2020/2021"
  credit_label1=tk.Label(windows_credit, text=text1, fg="black", font=("Helvetica", 14))
  credit_label1.pack( pady=30, side=tk.TOP)
  credit_label2=tk.Label(windows_credit, text=text2, fg="black", font=("Helvetica", 14))
  credit_label2.pack( pady=35, side=tk.TOP)

  exit_button=tk.Button(windows_credit, text="Close",background="grey", fg="black", font=("Helvetica", 12), height=1, width=7, command=windows_credit.destroy)
  exit_button.pack(padx=100,pady=20, side=tk.BOTTOM)

  
