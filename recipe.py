from tkinter import *
from PIL import ImageTk, Image
import requests


class Recipe:

    def __init__(self, dish_pic, inst, dish_name):
        self.window = Tk()
        self.window.geometry("600x780+350+5")
        self.window.title("Recipe")
        self.window.config(padx=20, pady=20, bg="#375362")
        self.window.attributes('-topmost', True)

        response = requests.get(dish_pic)
        open("picture.jpg", "wb").write(response.content)
        img = Image.open("picture.jpg")
        resized_image = img.resize((400, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(resized_image)
        Label(image=photo).place(x=75, y=10)

        Label(text=dish_name, fg="white", highlightthickness=2, bg="#375362", font=("Comic Sans MS", 15, "bold")) \
            .place(x=25, y=325)
        self.canvas = Canvas(bg="#608da6")
        self.canvas.create_text(
            250, 190, width=480,
            text=inst, fill="white",
            font=("Comic Sans MS", 9, "italic")
        )
        self.canvas.grid(pady=370, padx=25)
        self.canvas.config(width=500, height=380)

        self.window.mainloop()
