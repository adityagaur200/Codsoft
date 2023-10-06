import tkinter as tk
from tkinter import messagebox
import json
import os

# Load tasks from a file
def load_tasks():
    global tasks
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)

# Save tasks to a file
def save_tasks():
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        listbox_tasks.delete(selected_task_index)
        save_tasks()

def edit_task():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        selected_task = listbox_tasks.get(selected_task_index)
        edited_task = entry_task.get()
        if edited_task:
            tasks[selected_task_index[0]] = edited_task
            listbox_tasks.delete(selected_task_index)
            listbox_tasks.insert(selected_task_index, edited_task)
            entry_task.delete(0, tk.END)
            save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task to edit.")

# Set up the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# Load tasks from file (if available)
tasks = []
load_tasks()

# Create GUI components
frame_tasks = tk.Frame(root)
frame_tasks.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=30, font=("Arial", 14), bd=0, highlightthickness=0)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_tasks = tk.Scrollbar(frame_tasks, orient=tk.VERTICAL, command=listbox_tasks.yview)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)

entry_task = tk.Entry(root, width=30, font=("Arial", 14))
entry_task.pack(padx=10, pady=5)

button_add_task = tk.Button(root, text="Add Task", command=add_task, font=("Arial", 12))
button_add_task.pack(pady=5, ipadx=10)

button_remove_task = tk.Button(root, text="Remove Task", command=remove_task, font=("Arial", 12))
button_remove_task.pack(pady=5, ipadx=2)

button_edit_task = tk.Button(root, text="Edit Task", command=edit_task, font=("Arial", 12))
button_edit_task.pack(pady=5, ipadx=10)

button_quit = tk.Button(root, text="Quit", command=root.quit, font=("Arial", 12))
button_quit.pack(pady=5, ipadx=10)

# Update the listbox with the tasks
for task in tasks:
    listbox_tasks.insert(tk.END, task)

root.mainloop()
