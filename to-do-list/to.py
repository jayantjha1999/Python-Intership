import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []
        self.load_tasks()

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(master, textvariable=self.task_var, width=50)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.load_tasks_to_listbox()

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.save_button = tk.Button(master, text="Save Tasks", command=self.save_tasks)
        self.save_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

    def load_tasks(self):
        try:
            with open('tasks.txt', 'r') as file:
                self.tasks = [task.strip() for task in file.readlines()]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open('tasks.txt', 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')
        messagebox.showinfo("Tasks Saved", "Your to-do list has been saved.")

    def load_tasks_to_listbox(self):
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        new_task = self.task_var.get()
        if new_task:
            self.tasks.append(new_task)
            self.task_listbox.insert(tk.END, new_task)
            self.task_var.set("")
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(index)
            self.task_listbox.delete(index)
            self.tasks.remove(task)
        except IndexError:
            messagebox.showwarning("No Task Selected", "Please select a task to remove.")

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
