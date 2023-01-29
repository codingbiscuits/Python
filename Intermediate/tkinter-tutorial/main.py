import tkinter

window = tkinter.Tk()
window.title("D&D Character Sheet")
window.minsize(width=500, height=300)

character_name = tkinter.Label(
    text="Character 1: IRB", font=("Arial", 24, "bold"))
character_name.pack(side="top")
charactar_stats = tkinter.Label(
    text="Strength: 10\n\nIntelligence: 100\n\nStamina: 10\n\nCharisma: 100\n\nLuck: 10",
    font=("Arial", 15))
charactar_stats.pack(side="right", expand=True)


def change_name():
    character_name["text"] = f"Character 1: {input.get().upper()}"
    input.delete(0, "end")


button = tkinter.Button(text="Change Name", command=change_name)
button.pack(side="bottom")

input = tkinter.Entry(width=10)
input.pack()


window.mainloop()
