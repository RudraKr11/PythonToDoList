# Creating A To-Do List
import tkinter as tk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("300x400")
        self.root.configure(bg="#1A1A1A")

        self.tasks = []

        self.task_frame = tk.Frame(self.root, bg="#1A1A1A")
        self.task_frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.task_frame, width=40, height=15, font=("Arial Black", 10), bd=0, bg="#1A1A1A", fg="cyan")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry_frame = tk.Frame(self.root, bg="#1A1A1A")
        self.entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.entry_frame, width=30, font=("Arial Black", 10), bd=2, relief=tk.GROOVE)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.add_task_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task,
                                          font=("Arial Black", 10), bg="#00BCD4", fg="white")
        self.add_task_button.pack(side=tk.LEFT)

        self.remove_task_button = tk.Button(self.root, text="Remove Task", command=self.remove_task,
                                             font=("Arial Black", 10), bg="#F44336", fg="white")
        self.remove_task_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append((task, False))
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task, completed in self.tasks:
            display_text = f"[{'✔' if completed else ' '}] {task}"
            if completed:
                display_text = f"~~{task}~~"
            self.task_listbox.insert(tk.END, display_text)

    def toggle_task(self, event):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task, completed = self.tasks[selected_task_index[0]]
            self.tasks[selected_task_index[0]] = (task, not completed)
            self.update_task_list()

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.bind("<Double-1>", todo_app.toggle_task)
    root.mainloop()
