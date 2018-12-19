import tkinter as tk

root = tk.Tk()
root.title('Editor Test')

text_widget = tk.Text(root)
text_widget.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
text_widget.grid(column=0, row=1, )

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
