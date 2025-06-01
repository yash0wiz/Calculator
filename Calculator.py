import tkinter as tk
from tkinter import font as tkFont

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.configure(bg="#1e1e1e")
        self.root.geometry("480x580")
        self.root.resizable(False, False)

        self.expression = ""
        self.font = tkFont.Font(family="Helvetica", size=18, weight="bold")

        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self.root, bg="#1e1e1e")
        input_frame.pack(pady=20)

        input_box = tk.Entry(
            input_frame, textvariable=self.input_text,
            font=("Helvetica", 24, "bold"), 
            width=22,                       
            bd=0, bg="#292929", fg="white",
            justify="right"
            )
        input_box.grid(row=0, column=0, ipady=20, ipadx=10)  


        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+']
        ]

        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack()

        for row_index, row in enumerate(buttons):
            for col_index, char in enumerate(row):
                button = tk.Button(button_frame, text=char, font=self.font, width=5, height=2,
                                   bg="#333", fg="white", bd=0, activebackground="#444", activeforeground="cyan",
                                   command=lambda ch=char: self.on_button_click(ch))
                button.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")
                
        equal_button = tk.Button(button_frame, text="=", font=self.font, height=2,
                         bg="#00a86b", fg="white", bd=0, activebackground="#00cc88", activeforeground="white",
                         command=lambda: self.on_button_click('='))
        equal_button.grid(row=4, column=0, columnspan=4, padx=5, pady=10, sticky="nsew")

  
    def on_button_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        elif char == "C":
            self.expression = ""
            self.input_text.set("")
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
