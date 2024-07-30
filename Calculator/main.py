from tkinter import *
from tkinter import messagebox


class Calculator:

    def __init__(self, root):
        self.root = root
        self.root.title('Calculator')
        self.user_input = StringVar()
        self.root.config(pady=10, padx=10)
        # Display
        display_frame = Frame(self.root, highlightthickness=1, highlightcolor='black', width=50, height=30)
        display_frame.pack()
        entry = Entry(display_frame, textvariable=self.user_input, width=40)
        entry.grid(row=0, column=0, columnspan=2, padx=10)
        Button(display_frame, text='C', width=10, command=lambda b='C': self.on_button_click(b)).grid(
            row=0, column=2, padx=5)

        # Number Button
        number_frame = Frame(self.root, width=50)
        number_frame.pack()
        buttons = ['7', '8', '9',
                   '4', '5', '6',
                   '1', '2', '3',
                   '0', '.', '=']
        row = 1
        col = 0
        for button in buttons:
            Button(number_frame, text=button, width=5, font=("Helvetica", 15), height=3, bd=4,
                   command=lambda b=button: self.on_button_click(b)).grid(
                row=row, column=col, padx=10, pady=5)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # Operators
        operators = ['/', '*', '-', '+']
        op_row = 1
        for oper in operators:
            Button(number_frame, text=oper, width=5, height=3, font=("Helvetica", 15), bd=4,
                   command=lambda b=oper: self.on_button_click(b)).grid(
                row=op_row, column=3, padx=10, pady=5
            )
            op_row += 1

    def on_button_click(self, button):
        if button == 'C':
            self.user_input.set('')
        elif button == "=":
            try:
                result = str(eval(self.user_input.get()))
                self.user_input.set(result)
            except SyntaxError:
                messagebox.showerror('Error', 'Wrong Input')
        else:
            current_input = self.user_input.get()
            new_input = current_input + button
            self.user_input.set(new_input)


if __name__ == '__main__':
    root = Tk()
    app = Calculator(root)
    root.mainloop()
