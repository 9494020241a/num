import tkinter as tk
import random
import string

PAUSE_MS = 4000  # 4 seconds

def main():
    root = tk.Tk()
    root.title("Random A–Z")
    root.configure(bg="white")
    root.geometry("800x500")

    lbl = tk.Label(root, text="", font=("Segoe UI", 180, "bold"), bg="white", fg="#222")
    lbl.pack(expand=True, fill="both")

    def tick():
        ch = random.choice(string.ascii_uppercase)  # pick A–Z
        lbl.config(text=ch)
        root.after(PAUSE_MS, tick)  # schedule next update in 4 sec

    tick()
    root.mainloop()

if __name__ == "__main__":
    main()
