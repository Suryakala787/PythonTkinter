import tkinter as tk
from tkinter import messagebox, simpledialog
import os

FILE_NAME = "tasks.txt"
# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Add a new task
def add_task():
    task = task_entry.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return
    tasks_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)
    save_tasks(list(tasks_listbox.get(0, tk.END)))

# Delete selected task
def delete_task():
    try:
        selected_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_index)
        save_tasks(list(tasks_listbox.get(0, tk.END)))
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Edit selected task
def edit_task():
    try:
        selected_index = tasks_listbox.curselection()[0]
        current_task = tasks_listbox.get(selected_index)
        new_task = simpledialog.askstring("Edit Task", "Edit your task:", initialvalue=current_task)
        if new_task:
            tasks_listbox.delete(selected_index)
            tasks_listbox.insert(selected_index, new_task)
            save_tasks(list(tasks_listbox.get(0, tk.END)))
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit!")

# Mark task as completed
def complete_task():
    try:
        selected_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_index)
        if not task.startswith("✔️ "):
            tasks_listbox.delete(selected_index)
            tasks_listbox.insert(selected_index, f"✔️ {task}")
            save_tasks(list(tasks_listbox.get(0, tk.END)))
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to complete!")

# GUI setup
root = tk.Tk()
root.title("To-Do List / Task Manager")
root.geometry("400x400")

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

edit_button = tk.Button(root, text="Edit Task", width=15, command=edit_task)
edit_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="Complete Task", width=15, command=complete_task)
complete_button.pack(pady=5)

tasks_listbox = tk.Listbox(root, width=50, height=15)
tasks_listbox.pack(pady=10)

# Load tasks initially
for task in load_tasks():
    tasks_listbox.insert(tk.END, task)

root.mainloop()
