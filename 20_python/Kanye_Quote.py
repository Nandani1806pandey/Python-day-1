from tkinter import *
import requests
import os
from PIL import Image, ImageTk 

script_dir = os.path.dirname(os.path.abspath(__file__))
background_path = os.path.join(script_dir, "background.jpg")
kanye_image_path = os.path.join(script_dir, "Kanye_image.jpg")
def get_quote():
    try:
        response = requests.get("https://api.kanye.rest/")
        response.raise_for_status()
        data = response.json()
        quote = data["quote"]
        canvas.itemconfig(quote_text, text=quote)
    except requests.exceptions.RequestException:
        canvas.itemconfig(quote_text, text="Error fetching quote!")


window = Tk()
window.title("Kanye Says....")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
canvas.grid(row=0, column=0)
background_image = Image.open(background_path)
background_img = ImageTk.PhotoImage(file=r"C:/Users/pande/OneDrive/Desktop/nandani/Python/20_python/background.jpg")

canvas.create_image(150, 207,image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial",20, "bold"), fill='white')
canvas.grid(row=0, column=0)

kanye_img = Image.open(kanye_image_path)
Kanye_image = ImageTk.PhotoImage(kanye_img)
kanye_button = Button(image=Kanye_image, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)
window.mainloop()