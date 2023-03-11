from tkinter import *
import requests                                                                                           #These lines import the necessary Python modules requests and json.
import json                                                                                                  #These lines import the necessary Python modules requests and json.

pf = Tk()
pf.title("First Project")                                                                                            #using title method


def color(colors):                                                                                                   #colors function
    if colors > 0 
        return "green"
    else:
        return "red"

def my_Portfolio():                                                                                                  #function
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=100&convert=USD&CMC_PRO_API_KEY=4e41ec18-400c-4a8c-816d-253bb4184735")
    api = json.loads(api_request.content)                                                                             # These lines send a GET request to the CoinMarketCap API to retrieve the latest market data

    coins = [                                                                                                          #This creates a list called coins containing two dictionaries
        {
            "symbol": "BTC",
            "coin_owned": 2,
            "at_price": 20000
        },
        {
            "symbol": "ETH",
            "coin_owned": 4,
            "at_price": 1000
        },
        {
            "symbol": "DOT",
            "coin_owned": 100,
            "at_price": 5
        },
        {
            "symbol": "LEO",
            "coin_owned": 500,
            "at_price": 3
        },
        {
            "symbol": "ETC",
            "coin_owned": 50,
            "at_price": 16
        }
    ]

    total_pl = 0                                                                                                             #This initializes a variable total_pl to zero
    roww = 1
    total_current_value = 0
    total_amount_value = 0
    for i in range(0, 100):
        for port in coins:
            if (api["data"][i]["symbol"]) == port["symbol"]:
                total_amount = port["at_price"] * port["coin_owned"]                                                        # 1-total money spent on buying the coins
                current_value = port["coin_owned"] * api["data"][i]["quote"]["USD"]["price"]                                # 2 -printing the current value of total shares with latest price
                pro_los = api["data"][i]["quote"]["USD"]["price"] - port["at_price"]                                        # 3-printing profit and loss in shares
                pro_loss = pro_los * port["coin_owned"]
                total_pl = total_pl + pro_loss                                                                              # 4-total profit and loss of portfolio
                total_current_value = total_current_value + current_value
                total_amount_value = total_amount_value + total_amount



                # print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
                # print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
                # print("Number Of Coin:", port["coin_owned"])
                # print("Total Amount Paid:", "${0:.2f}".format(total_amount))
                # print("Current Value:", "${0:.2f}".format(current_value))
                # print("P/L Per Coin:", "${0:.2f}".format(pro_los))
                # print("Total P/L With Coins:", "${0:.2f}".format(pro_loss))
                # print("----------------")
                # print("----------------")
                # print("Total P/L For Portfolio:", "${0:.2f}".format(total_pl))

                name = Label(pf, text=api["data"][i]["symbol"],bg="white", fg="black", font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3 )
                name.grid(row=roww , column=0)

                price = Label(pf, text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="white", fg="black", font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3)
                price.grid(row=roww, column=1)


                co = Label(pf, text=port["coin_owned"], bg="white", fg="black", font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3)
                co.grid(row=roww, column=2)

                tap = Label(pf, text="${0:.2f}".format(total_amount), bg="white", fg="black", font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3)
                tap.grid(row=roww, column=3)

                cv = Label(pf, text="${0:.2f}".format(current_value), bg="white", fg="black", font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3)
                cv.grid(row=roww, column=4)

                pl = Label(pf, text="${0:.2f}".format(pro_los), bg="white", fg=color(float("{0:.2f}".format(pro_los))), font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3)
                pl.grid(row=roww, column=5)

                tpl = Label(pf, text="${0:.2f}".format(pro_loss), bg="white", fg=color(float("{0:.2f}".format(pro_loss))), font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3)
                tpl.grid(row=roww, column=6)


                roww = roww + 1


                totalpl = Label(pf, text="${0:.2f}".format(total_pl), bg="white", fg=color(float("{0:.2f}".format(total_pl))), font=("Comic Sans MS", 12),padx=2, pady=2, borderwidth=3)
                totalpl.grid(row=6, column=6)

                totalcv = Label(pf, text="${0:.2f}".format(total_current_value), bg="white", fg="black", font=("Comic Sans MS", 12),padx=2, pady=2, borderwidth=3)
                totalcv.grid(row=6, column=4)

                totalamo = Label(pf, text="${0:.2f}".format(total_amount_value), bg="white", fg="black",font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3)
                totalamo.grid(row=6, column=3)

    api = ""


    buttonn = Button(pf, text="Update", bg="black", fg="white", command=my_Portfolio, font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3)
    buttonn.grid(row=7, column=6)



    name = Label(pf, text="Name", bg="dark blue", fg="white", font=("Comic Sans MS", 12, "bold"), padx=2, pady=2, borderwidth=3, relief="groove")
    name.grid(row=0, column=0)


    price = Label(pf, text="current\nPrice", bg="dark blue", fg="white", font=("Comic Sans MS", 12, "bold"), padx=2, pady=2, borderwidth=3, relief="groove")                                                                              # creates a new instance of the Label class, and specifies pf as its parent or master widget, the label will be placed inside the GUI window created by pf
    price.grid(row=0, column=1)                                                                                             #grid method to position the label
                                                                                                                            #  The row and column parameters of the grid method specify the position of the widget in the grid

    co = Label(pf, text="Coins Owned", bg="dark blue", fg="white", font=("Comic Sans MS", 12, "bold"), padx=2, pady=2, borderwidth=3, relief="groove")
    co.grid(row=0, column=2)



    tap = Label(pf, text="Total amount paid", bg="dark blue", fg="white", font=("Comic Sans MS", 12, "bold"), padx=2, pady=2, borderwidth=3, relief="groove")
    tap.grid(row=0, column=3)


    cv = Label(pf, text="Current Value", bg="dark blue", fg="white", font=("Comic Sans MS", 12, "bold"), padx=2, pady=2, borderwidth=3, relief="groove")
    cv.grid(row=0, column=4)


    pl = Label(pf, text="P/l per coin", bg="dark blue", fg="white", font=("Comic Sans MS", 12, "bold"), padx=2, pady=2, borderwidth=3, relief="groove")
    pl.grid(row=0, column=5)


    tpl = Label(pf, text="Total p/l", bg="dark blue", fg="white", font=("Comic Sans MS", 12, "bold"), padx=2, pady=2, borderwidth=3, relief="groove")
    tpl.grid(row=0, column=6)


my_Portfolio()

pf.mainloop()













