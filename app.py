import tkinter as tk
window = tk.Tk()
window.attributes('-fullscreen', True)
window.configure(
    highlightthickness=0,
    bd=0, relief='flat',
    bg='white', cursor='none',
)
window.title('White full screen window')
window.bind("<Button-1>", lambda e: window.destroy())
window.mainloop()
