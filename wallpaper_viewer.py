from tkinter import *
from PIL import ImageTk, Image
import os

def rotate_img():
    global counter
    img_label.config(image = img_array[counter%len(img_array)])
    counter += 1
    
counter = 1
root = Tk()

root.title("Wallpaper Viewer")
root.geometry('250x400')
root.configure(background='black')

files = os.listdir('wallpapers')

img_array = []
for file in files:
    img = Image.open(os.path.join('wallpapers',file))
    resized_img = img.resize((200,300))
    img_array.append(ImageTk.PhotoImage(resized_img))
    

img_label = Label(root, image=img_array[0])
img_label.pack(pady=(15,10))

next_button = Button(root, text="Next", background='white', fg='black', width= 28, height= 25, command= rotate_img)
next_button.pack()

root.mainloop()