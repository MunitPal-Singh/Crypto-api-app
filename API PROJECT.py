# IMPORTING IMPORTANT LIBRARIES AND PACKAGES

from tkinter import *
from tkinter import messagebox                                      #used to show message box
import requests                                                     #These lines import the necessary Python modules requests and json.
import json                                                          #These lines import the necessary Python modules requests and json.
import sqlite3



#INITIATING TKINTER MODULE
pf = Tk()
pf.title("First Project")                                             #using title method




#INITIATING SQLITE
obj1 = sqlite3.connect("Coin Market Data")
obj2 = obj1.cursor()

# obj2.execute("CREATE TABLE  IF NOT EXISTS coin_data(id INTEGER PRIMARY KEY, symbol TEXT, coin owned INTEGER, at_price REAL)")
# obj1.commit()

# obj2.execute("INSERT INTO coin_data values(1,'BTC',2,20000)")
# obj1.commit()
#
# obj2.execute("INSERT INTO coin_data values(2,'ETH',4,1000)")
# obj1.commit()
#
# obj2.execute("INSERT INTO coin_data values(3,'DOT',100,5)")
# obj1.commit()
#
# obj2.execute("INSERT INTO coin_data values(4,'LEO',500,3)")
# obj1.commit()

def reset():
    for cell in pf.winfo_children():               #this function used to destroy window and update the db
            cell.destroy()                           #this function used to destroy window and update the db


    app_header()
    my_Portfolio()


def my_Portfolio():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=100&convert=USD&CMC_PRO_API_KEY=4e41ec18-400c-4a8c-816d-253bb4184735")
    api = json.loads(api_request.content)                                                                                    # These lines send a GET request to the CoinMarketCap API to retrieve the latest market data

    obj2.execute("SELECT * FROM coin_data")
    coins = obj2.fetchall()

    print(coins)

    def color(colors):
        if colors > 0:
            return "green"
        else:
            return "red"




     #MAKING A FUNCTION TO INSERT COINS IN DATABASE
    def INSERT():
        obj2.execute("INSERT INTO coin_data(symbol,coin,at) VALUES(?,?,?)", (symbolname.get(),boughtprice.get(), coinsbought.get()))
        obj1.commit()

        messagebox.showinfo("Portfolio Notification","New Coin Added Successfully")                 #this will show message dialogue box, 1 parameter is for tittle and 2 is for content
        reset()



    # MAKING A FUNCTION TO DELETE COINS IN DATABASE
    def DELETE():
        obj2.execute("DELETE FROM coin_data WHERE id=?", (symbolnameD.get(),))
        obj1.commit()

        messagebox.showinfo("Portfolio Notification", "Coin Deleted Successfully")                   #this will show message dialogue box, 1 parameter is for tittle and 2 is for content
        reset()




    # coins = [                                                                                                          #This creates a list called coins containing two dictionaries
    #     {
    #         "symbol": "BTC",
    #         "coin_owned": 2,
    #         "at_price": 20000
    #     },
    #     {
    #         "symbol": "ETH",
    #         "coin_owned": 4,
    #         "at_price": 1000
    #     },
    #     {
    #         "symbol": "DOT",
    #         "coin_owned": 100,
    #         "at_price": 5
    #     },
    #     {
    #         "symbol": "LEO",
    #         "coin_owned": 500,
    #         "at_price": 3
    #     },
    #     {
    #         "symbol": "ETC",
    #         "coin_owned": 50,
    #         "at_price": 16
    #     }
    # ]




    total_pl = 0                                                        #This initializes a variable total_pl to zero
    roww = 1
    total_current_value = 0
    total_amount_value = 0
    for i in range(0, 100):
        for port in coins:
            if (api["data"][i]["symbol"]) == port[1]:
                total_amount = port[3] * port[2]                                                        # 1-total money spent on buying the coins
                current_value = port[2] * api["data"][i]["quote"]["USD"]["price"]                                # 2 -printing the current value of total shares with latest price
                pro_los = api["data"][i]["quote"]["USD"]["price"] - port[3]                                        # 3-printing profit and loss in shares
                pro_loss = pro_los * port[2]
                total_pl = total_pl + pro_loss                                                                              # 4-total profit and loss of portfolio
                total_current_value = total_current_value + current_value
                total_amount_value = total_amount_value + total_amount



                # print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
                # print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
                # print("Number Of Coin:", port[2])
                # print("Total Amount Paid:", "${0:.2f}".format(total_amount))
                # print("Current Value:", "${0:.2f}".format(current_value))
                # print("P/L Per Coin:", "${0:.2f}".format(pro_los))
                # print("Total P/L With Coins:", "${0:.2f}".format(pro_loss))
                # print("----------------")
                # print("----------------")
                # print("Total P/L For Portfolio:", "${0:.2f}".format(total_pl))

                pf_id = Label(pf, text= port[0], bg="white", fg="black", font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3)
                pf_id.grid(row=roww, column=0)

                name = Label(pf, text=api["data"][i]["symbol"],bg="white", fg="black", font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3 )
                name.grid(row=roww , column=1)

                price = Label(pf, text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="white", fg="black", font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3)
                price.grid(row=roww, column=2)


                co = Label(pf, text=port[2], bg="white", fg="black", font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3)
                co.grid(row=roww, column=3)

                tap = Label(pf, text="${0:.2f}".format(total_amount), bg="white", fg="black", font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3)
                tap.grid(row=roww, column=4)

                cv = Label(pf, text="${0:.2f}".format(current_value), bg="white", fg="black", font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3)
                cv.grid(row=roww, column=5)

                pl = Label(pf, text="${0:.2f}".format(pro_los), bg="white", fg=color(float("{0:.2f}".format(pro_los))), font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3)
                pl.grid(row=roww, column=6)

                tpl = Label(pf, text="${0:.2f}".format(pro_loss), bg="white", fg=color(float("{0:.2f}".format(pro_loss))), font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3)
                tpl.grid(row=roww, column=7)


                roww = roww + 1


                totalpl = Label(pf, text="${0:.2f}".format(total_pl), bg="white", fg=color(float("{0:.2f}".format(total_pl))), font=("Comic Sans MS", 12),padx=2, pady=2, borderwidth=3)
                totalpl.grid(row=6, column=7)

                totalcv = Label(pf, text="${0:.2f}".format(total_current_value), bg="white", fg="black", font=("Comic Sans MS", 12),padx=2, pady=2, borderwidth=3)
                totalcv.grid(row=6, column=5)

                totalamo = Label(pf, text="${0:.2f}".format(total_amount_value), bg="white", fg="black",font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3)
                totalamo.grid(row=6, column=4)

    api = ""

    # CODE TO ADD COINS IN DATABASE
    symbolname = Entry(pf,borderwidth=3)                                    #entry in a method to get input frm user in tkinter
    symbolname.grid(row = roww+2, column=1)

    boughtprice = Entry(pf, borderwidth=3)
    boughtprice.grid(row=roww + 2, column=2)

    coinsbought = Entry(pf, borderwidth=3)
    coinsbought.grid(row=roww + 2, column=3)

    add_coin = Button(pf, text="ADD COIN", bg="black", fg="white", command=INSERT, font=("Comic Sans MS", 12),padx=2, pady=2, borderwidth=3)
    add_coin.grid(row=roww + 2, column=4)


    #DELETING DATA FROM DATABASE

    symbolnameD = Entry(pf, borderwidth=3)  # entry in a method to get input frm user in tkinter
    symbolnameD.grid(row=roww + 3, column=0)


    delete_coin = Button(pf, text="DELETE", bg="black", fg="white", command=DELETE, font=("Comic Sans MS", 12), padx=2,pady=2, borderwidth=3)
    delete_coin.grid(row=roww + 3, column=4)



    Refresh = Button(pf, text="Refresh", bg="black", fg="white", command=reset, font=("Comic Sans MS", 12), padx=2, pady=2, borderwidth=3) #in command we are calling reset functio because it will call destroy method and after that my portfolio function
    Refresh.grid(row=7, column=7)


def app_header():
    coin_id = Label(pf, text="ID", bg="dark blue", fg="white", font=("Comic Sans MS", 12, "bold"), padx=2, pady=2, borderwidth=3, relief="groove")
    coin_id.grid(row=0, column=0)

    name = Label(pf, text="Name", bg="dark blue", fg="white", font=("Comic Sans MS", 12, "bold"), padx=2, pady=2, borderwidth=3, relief="groove")
    name.grid(row=0, column=1)


    price = Label(pf, text="current\nPrice", bg="dark blue", fg="white", font=("Comic Sans MS", 12, "bold"), padx=2, pady=2, borderwidth=3, relief="groove")                                                                              # creates a new instance of the Label class, and specifies pf as its parent or master widget, the label will be placed inside the GUI window created by pf
    price.grid(row=0, column=2)                                                                                             #grid method to position the label
                                                                                                                            #  The row and column parameters of the grid method specify the position of the widget in the grid

    co = Label(pf, text="Coins Owned", bg="dark blue", fg="white", font=("Comic Sans MS", 12, "bold"), padx=2, pady=2, borderwidth=3, relief="groove")
    co.grid(row=0, column=3)



    tap = Label(pf, text="Total amount paid", bg="dark blue", fg="white", font=("Comic Sans MS", 12, "bold"), padx=2, pady=2, borderwidth=3, relief="groove")
    tap.grid(row=0, column=4)


    cv = Label(pf, text="Current Value", bg="dark blue", fg="white", font=("Comic Sans MS", 12, "bold"), padx=2, pady=2, borderwidth=3, relief="groove")
    cv.grid(row=0, column=5)


    pl = Label(pf, text="P/l per coin", bg="dark blue", fg="white", font=("Comic Sans MS", 12, "bold"), padx=2, pady=2, borderwidth=3, relief="groove")
    pl.grid(row=0, column=6)


    tpl = Label(pf, text="Total p/l", bg="dark blue", fg="white", font=("Comic Sans MS", 12, "bold"), padx=2, pady=2, borderwidth=3, relief="groove")
    tpl.grid(row=0, column=7)




my_Portfolio()
app_header()

pf.mainloop()

obj2.close()
obj1.close()












