from tkinter import *
import random


class RPSGame:

    def __init__(self, root):
        self.root = root
        self.root.title('Rock-Paper-Scissors Game')
        self.root.config(pady=10)
        self.rock_img = PhotoImage(file='rock.png')
        self.paper_img = PhotoImage(file='paper.png')
        self.scissor_img = PhotoImage(file='scissors.png')
        self.options = [self.rock_img, self.paper_img, self.scissor_img]
        self.win = 0
        self.loss = 0
        self.draw = 0
        self.game()

    def game(self):
        self.root.minsize(width=900, height=450)

        self.score_label = Label(text=f'Win = {self.win} | Draw = {self.draw} | Loss = {self.loss}',
                            font=("Courier", 30, 'bold'))
        self.score_label.pack()
        # First Frame
        self.frame1 = Frame(self.root)
        self.frame1.pack()
        # Label
        choose_label = Label(self.frame1, text='Choose:\n', font=("Courier", 50, 'bold'))
        choose_label.grid(row=0, column=1)
        # Buttons
        col = 0
        for button in self.options:
            Button(self.frame1, image=button, highlightthickness=0,
                   command=lambda user_choice=button: self.on_button_click(user_choice)).grid(
                row=1, column=col, padx=10, pady=5)
            col += 1

    def on_button_click(self, user_choice):
        self.frame1.destroy()
        canvas_frame = Frame(self.root)
        computer_choice = random.choice(self.options)
        computer_canvas = Canvas(canvas_frame)
        user_canvas = Canvas(canvas_frame)
        user_canvas.create_image(150, 150, image=user_choice)
        computer_canvas.create_image(150, 150, image=computer_choice)
        canvas_frame.pack(pady=50)
        user_canvas.grid(row=0, column=0)
        computer_canvas.grid(row=0, column=1)

        # determine the winner
        if user_choice == computer_choice:
            result = "It's a tie!"
            self.draw += 1
        elif (user_choice == self.rock_img and computer_choice == self.scissor_img) or \
                (user_choice == self.paper_img and computer_choice == self.rock_img) or \
                (user_choice == self.scissor_img and computer_choice == self.paper_img):
            result = "You win!"
            self.win += 1
        else:
            result = "Computer wins!"
            self.loss += 1
        self.score_label.config(text=f'Win = {self.win} | Draw = {self.draw} | Loss = {self.loss}')

        result_label = Label(self.root, text=result, font=("Courier", 30))
        result_label.pack()

        play_again_button = Button(self.root, text="Play Again", command=self.play_again)
        play_again_button.pack()

    def play_again(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.game()


if __name__ == '__main__':
    root = Tk()
    app = RPSGame(root)
    root.mainloop()
