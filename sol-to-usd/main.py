import tkinter
import requests
from bs4 import BeautifulSoup

LINK = "https://coinmarketcap.com/currencies/solana/"


def get_total_sol():
    total_sol = float(input_field.get())
    usd_label["text"] = f"${total_sol * sol_price} USD"
    print(sol_price)


response = requests.get(LINK)
page_parse = BeautifulSoup(response.text, 'html.parser')
sol_price = page_parse.find("div", {"class": "priceValue"}).find("span").text
sol_price = float(sol_price[1:])

window = tkinter.Tk()
window.title("Solana to USD Converter")


input_field = tkinter.Entry()
input_field.insert("end", string="0")
input_field.config(width=10)
input_field.focus()
input_field.grid(column=1, row=0)

solana_label = tkinter.Label(text="Solana")
solana_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

convert_button = tkinter.Button(text="Convert", command=get_total_sol)
convert_button.grid(column=1, row=1)

usd_label = tkinter.Label(text="$0.00 USD")
usd_label.grid(column=2, row=1)


window.mainloop()
