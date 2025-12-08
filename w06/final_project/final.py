#import
import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry

#main
def main():
    root = tk.Tk()
    root.option_add("*Font", "Helvetica 16")
    frame_main = Frame(root)
    frame_main.master.title("Final Project")
    frame_main.pack(padx=3, pady=3, fill=tk.BOTH, expand=True)
    setup_main(frame_main)
    frame_main.mainloop()

def setup_main(frame, query):
    #upper_bounds needs to be updated from "query" and the ver.
    #Labels for addition request
    label_add_quest = Label(frame, text="Enter the first digits for the addtion")
    label_add_quest.grid(row=0, column=0, padx=3, pady=3)
    add_num = IntEntry(frame, width=4, lower_bound=1, upper_bound=upper)
    upper = len(query)
    label_add_quest1 = Label(frame, text="Enter the second didgits for the addition")
    label_add_quest1.grid(row=1, column=1, padx=3, pady= 3)
    add_num1 = IntEntry(frame, width=4, lower_bound=1, upper_bound=upper)
    #button for addition
    label_btn = Button(frame, text="ADDITION!")
    label_btn.grid(row=1, column=2, padx=3, pady=3)

    label_addition = Label(frame, text="")
    label_addition.grid(row=3, column=0, padx=3, pady=3)

    def addition():
        try:
            add_1 = add_num.get()
            add_2 = add_num1.get()
            result = add_1 + add_2

        except ValueError:

    







if __name__ == "__main__":
    main()