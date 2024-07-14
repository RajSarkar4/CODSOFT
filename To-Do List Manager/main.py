import tkinter as tk
from tkinter import messagebox
import json

index = 0


class ToDo:

    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List')
        self.root.config(padx=50, pady=30)

        self.canva_frame = tk.Frame(self.root)
        self.canva_frame.pack()

        self.canvas = tk.Canvas(self.canva_frame, width=200, height=200)
        self.photo = tk.PhotoImage(file='TODO.png')
        self.canvas.create_image(100, 100, image=self.photo)
        self.canvas.grid(row=1, column=1)

        self.button_frame = tk.Frame(self.root)

        self.create_button = tk.Button(self.button_frame, text='Add Task', width=15, command=self.add_task)
        self.view_button = tk.Button(self.button_frame, text='View Task', width=15, command=self.view_task)
        self.exit_button = tk.Button(self.button_frame, text='Exit', width=15, command=self.exit)

        self.button_frame.pack()

        self.create_button.grid(row=2, column=0, pady=20, padx=20)
        self.view_button.grid(row=2, column=1, pady=20, padx=20)
        self.exit_button.grid(row=2, column=2, pady=20, padx=20)

    def add_task(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        add_frame = tk.Frame(self.root)
        add_frame.pack()

        label1 = tk.Label(add_frame, text="TODO List Title:")
        self.title_entry = tk.Entry(add_frame, width=53)
        label1.grid(row=2, column=0, pady=10)
        self.title_entry.grid(row=2, column=1, pady=10, columnspan=3)
        label2 = tk.Label(add_frame, text="Write you're To-Do line-by-line:")
        label2.grid(row=3, column=0)
        self.task_entry_box = tk.Text(add_frame, width=40, height=10)
        self.task_entry_box.grid(row=3, column=1, columnspan=2)
        save = tk.Button(add_frame, text='Add', width=15, command=self.save)
        save.grid(row=4, column=1, pady=20, padx=20)
        back_butt = tk.Button(add_frame, text='Back', width=15, command=self.back)
        exit_button = tk.Button(add_frame, text='Exit', width=15, command=self.exit)
        back_butt.grid(row=4, column=0, pady=20, padx=20)
        exit_button.grid(row=4, column=2, pady=20, padx=20)

    def view_task(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        try:
            with open("data.json") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(title='File not exist', message="You don't have any to-do list.\n"
                                                                 "Click on Add button to create one.")
        else:
            global index

            def next_todo():
                global index
                index += 1
                if index > len(data):
                    messagebox.showinfo(title='Out of Index',
                                        message='It is the Last to-do list')
                    index -= 1
                listbox.delete(0, tk.END)
                label.config(text=titles[index])
                for item in data[titles[index]]:
                    index = 1
                    listbox.insert(index, item)

            def prev_todo():
                global index
                index -= 1
                if index < 0:
                    messagebox.showinfo(title='Out of Index',
                                        message='It is the first to-do list')
                    index = 0
                listbox.delete(0, tk.END)
                label.config(text=titles[index])
                for item in data[titles[index]]:
                    listbox.insert(index, item)

            titles = [title for title in data]
            add_frame = tk.Frame(self.root)
            add_frame.pack()
            label = tk.Label(add_frame, text=titles[index])
            listbox = tk.Listbox(add_frame)
            for item in data[titles[index]]:
                index = 0
                listbox.insert(index, item)
            label.grid(row=2, column=1, pady=5)
            listbox.grid(row=3, column=1)
            prev_button = tk.Button(add_frame, text='←', command=prev_todo)
            next_button = tk.Button(add_frame, text='→', command=next_todo)
            prev_button.grid(row=3, column=0, padx=10)
            next_button.grid(row=3, column=2, padx=10)

        finally:
            bottom_frame = tk.Frame(self.root)
            back_butt = tk.Button(bottom_frame, text='Back', width=15, command=self.back)
            exit_button = tk.Button(bottom_frame, text='Exit', width=15, command=self.exit)
            back_butt.grid(row=4, column=0, padx=55, pady=20)
            exit_button.grid(row=4, column=2, padx=55, pady=20)
            bottom_frame.pack()

    def exit(self):
        global viewer
        self.root.destroy()
        viewer = False

    def back(self):
        self.root.destroy()

    def save(self):
        title = self.title_entry.get().title()
        todo_list = self.task_entry_box.get("1.0", 'end-1c').split('\n')
        new_data = {
            title: todo_list
        }
        if title and todo_list:
            try:
                file = open("data.json", "r")
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data = json.load(file)
                data.update(new_data)
                file.close()
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                self.title_entry.delete(0, tk.END)
                self.task_entry_box.delete("1.0", 'end-1c')


if __name__ == '__main__':
    viewer = True
    while viewer:
        root = tk.Tk()
        app = ToDo(root)
        root.mainloop()
