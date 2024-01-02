import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        # Create listbox to display tasks
        self.listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, height=15, width=50)
        self.listbox.pack(pady=10)

        # Create entry for new tasks
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        # Create entry for task priority
        self.priority_entry = tk.Entry(self.root, width=50)
        self.priority_entry.pack(pady=10)

        # Create "Add Task" button
        add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        # Create "Delete Task" button
        delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        delete_button.pack(pady=5)

        # Create "Mark as Completed" button
        complete_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_as_completed)
        complete_button.pack(pady=5)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        priority = self.priority_entry.get().strip()
        if task_text:
            if not priority:
                priority = "Normal"
            task_text_with_priority = f"{priority}: {task_text}"
            self.tasks.append(task_text_with_priority)
            self.listbox.insert(tk.END, task_text_with_priority)
            self.task_entry.delete(0, tk.END)
            self.priority_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            index_to_delete = selected_task_index[0]
            if 0 <= index_to_delete < len(self.tasks):
                self.listbox.delete(selected_task_index)
                del self.tasks[index_to_delete]
            else:
                messagebox.showwarning("Warning", "Invalid task index to delete!")

    def mark_as_completed(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            completed_task = self.tasks[selected_task_index[0]]
            self.tasks.remove(completed_task)
            self.listbox.delete(selected_task_index)
            completed_task += " (Completed)"
            self.listbox.insert(tk.END, completed_task)

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()
