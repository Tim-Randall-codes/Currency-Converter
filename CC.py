import tkinter as tk

window1 = tk.Tk()

def convert():
    num = input1.get()
    currency = str(cused.curselection())
    letpass = True
    while True:
        try:
            num = float(num)
            error1['text'] = " "
            letpass = True
            break
        except ValueError:
            error1['text'] = "Please input only numbers"
            input1.delete(0, tk.END)
            letpass = False
            break
    if letpass == True:
        if currency == "(0,)":
            audo['text'] = str(round(num * 1, 2))
            cado['text'] = str(round(num * 0.98, 2))
            cnho['text'] = str(round(num * 4.99, 2))
            euro['text'] = str(round(num * 0.64, 2))
            hkdo['text'] = str(round(num * 5.98, 2))
            jpyo['text'] = str(round(num * 82.13, 2))
            nzdo['text'] = str(round(num * 1.07, 2))
            gbpo['text'] = str(round(num * 0.55, 2))
            chfo['text'] = str(round(num * 0.70, 2))
            usdo['text'] = str(round(num * 0.77, 2))
        elif currency == "(1,)":
            audo['text'] = str(round(num * 1.02, 2))
            cado['text'] = str(round(num * 1, 2))
            cnho['text'] = str(round(num * 5.09, 2))
            euro['text'] = str(round(num * 0.65, 2))
            hkdo['text'] = str(round(num * 6.09, 2))
            jpyo['text'] = str(round(num * 83.69, 2))
            nzdo['text'] = str(round(num * 1.09, 2))
            gbpo['text'] = str(round(num * 0.56, 2))
            chfo['text'] = str(round(num * 0.71, 2))
            usdo['text'] = str(round(num * 0.79, 2))
        elif currency == "(2,)":
            audo['text'] = str(round(num * 0.2, 2))
            cado['text'] = str(round(num * 0.2, 2))
            cnho['text'] = str(round(num * 1, 2))
            euro['text'] = str(round(num * 0.13, 2))
            hkdo['text'] = str(round(num * 1.2, 2))
            jpyo['text'] = str(round(num * 16.44, 2))
            nzdo['text'] = str(round(num * 0.21, 2))
            gbpo['text'] = str(round(num * 0.11, 2))
            chfo['text'] = str(round(num * 0.14, 2))
            usdo['text'] = str(round(num * 0.15, 2))
        elif currency == "(3,)":
            audo['text'] = str(round(num * 1.57, 2))
            cado['text'] = str(round(num * 1.54, 2))
            cnho['text'] = str(round(num * 7.83, 2))
            euro['text'] = str(round(num * 1, 2))
            hkdo['text'] = str(round(num * 9.37, 2))
            jpyo['text'] = str(round(num * 128.68, 2))
            nzdo['text'] = str(round(num * 1.67, 2))
            gbpo['text'] = str(round(num * 0.87, 2))
            chfo['text'] = str(round(num * 1.1, 2))
            usdo['text'] = str(round(num * 1.21, 2))
        elif currency == "(4,)":
            audo['text'] = str(round(num * 0.17, 2))
            cado['text'] = str(round(num * 0.16, 2))
            cnho['text'] = str(round(num * 0.84, 2))
            euro['text'] = str(round(num * 0.11, 2))
            hkdo['text'] = str(round(num * 1, 2))
            jpyo['text'] = str(round(num * 13.74, 2))
            nzdo['text'] = str(round(num * 0.18, 2))
            gbpo['text'] = str(round(num * 0.093, 2))
            chfo['text'] = str(round(num * 0.12, 2))
            usdo['text'] = str(round(num * 0.13, 2))
        elif currency == "(5,)":
            audo['text'] = str(round(num * 0.012, 2))
            cado['text'] = str(round(num * 0.012, 2))
            cnho['text'] = str(round(num * 0.061, 2))
            euro['text'] = str(round(num * 0.0078, 2))
            hkdo['text'] = str(round(num * 0.073, 2))
            jpyo['text'] = str(round(num * 1, 2))
            nzdo['text'] = str(round(num * 0.013, 2))
            gbpo['text'] = str(round(num * 0.0067, 2))
            chfo['text'] = str(round(num * 0.0085, 2))
            usdo['text'] = str(round(num * 0.0094, 2))
        elif currency == "(6.)":
            audo['text'] = str(round(num * 0.94, 2))
            cado['text'] = str(round(num * 0.92, 2))
            cnho['text'] = str(round(num * 4.69, 2))
            euro['text'] = str(round(num * 0.6, 2))
            hkdo['text'] = str(round(num * 5.61, 2))
            jpyo['text'] = str(round(num * 77.11, 2))
            nzdo['text'] = str(round(num * 1, 2))
            gbpo['text'] = str(round(num * 0.52, 2))
            chfo['text'] = str(round(num * 0.66, 2))
            usdo['text'] = str(round(num * 0.72, 2))
        elif currency == "(7.)":
            audo['text'] = str(round(num * 1.81, 2))
            cado['text'] = str(round(num * 1.92, 2))
            cnho['text'] = str(round(num * 9.03, 2))
            euro['text'] = str(round(num * 1.13, 2))
            hkdo['text'] = str(round(num * 10.8, 2))
            jpyo['text'] = str(round(num * 148.44, 2))
            nzdo['text'] = str(round(num * 1.92, 2))
            gbpo['text'] = str(round(num * 1, 2))
            chfo['text'] = str(round(num * 1.26, 2))
            usdo['text'] = str(round(num * 1.39, 2))
        elif currency == "(8,)":
            audo['text'] = str(round(num * 1.43, 2))
            cado['text'] = str(round(num * 1.4, 2))
            cnho['text'] = str(round(num * 7.14, 2))
            euro['text'] = str(round(num * 0.91, 2))
            hkdo['text'] = str(round(num * 8.54, 2))
            jpyo['text'] = str(round(num * 117.6, 2))
            nzdo['text'] = str(round(num * 1.52, 2))
            gbpo['text'] = str(round(num * 0.79, 2))
            chfo['text'] = str(round(num * 1, 2))
            usdo['text'] = str(round(num * 1.1, 2))
        else:
            audo['text'] = str(round(num * 1.3, 2))
            cado['text'] = str(round(num * 1.27, 2))
            cnho['text'] = str(round(num * 6.48, 2))
            euro['text'] = str(round(num * 0.83, 2))
            hkdo['text'] = str(round(num * 7.76, 2))
            jpyo['text'] = str(round(num * 106.60, 2))
            nzdo['text'] = str(round(num * 1.38, 2))
            gbpo['text'] = str(round(num * 0.72, 2))
            chfo['text'] = str(round(num * 0.91, 2))
            usdo['text'] = str(round(num * 1, 2))
    else:
        pass

input1 = tk.Entry(window1, bg="light gray", bd=5)
input1.grid(column=1, row=2)

cused = tk.Listbox(window1)
cused.insert(1, "Australian Dollar (AUD)")
cused.insert(2, "Canadian Dollar (CAD)")
cused.insert(3, "Chinese Renminbi (CNH)")
cused.insert(4, "Euro (EUR)")
cused.insert(5, "Hong Kong Dollar (HKD)")
cused.insert(6, "Japanese Yen (JPY)")
cused.insert(7, "New Zealand Dollar (NZD)")
cused.insert(8, "Pound Sterling (GBP)")
cused.insert(9, "Swiss Franc (CHF)")
cused.insert(10, "US Dollars (USD)")
cused.grid(column=2, row=2)

convertb = tk.Button(window1, text="Convert!", command=convert)
convertb.grid(column=3, row=2)

audl = tk.Label(window1, text="Australian Dollars")
audl.grid(column=2, row=3)

audo = tk.Label(window1, text=" ")
audo.grid(column=3, row=3)

cadl = tk.Label(window1, text="Canadian Dollars")
cadl.grid(column=2, row=4)

cado = tk.Label(window1, text=" ")
cado.grid(column=3, row=4)

cnhl = tk.Label(window1, text="Chinese Renminbi")
cnhl.grid(column=2, row=5)

cnho = tk.Label(window1, text=" ")
cnho.grid(column=3, row=5)

eurl = tk.Label(window1, text="Euros")
eurl.grid(column=2, row=6)

euro = tk.Label(window1, text=" ")
euro.grid(column=3, row=6)

hkdl = tk.Label(window1, text="Hong Kong Dollars")
hkdl.grid(column=2, row=7)

hkdo = tk.Label(window1, text=" ")
hkdo.grid(column=3, row=7)

jpyl = tk.Label(window1, text="Japanese Yen")
jpyl.grid(column=2, row=8)

jpyo = tk.Label(window1, text=" ")
jpyo.grid(column=3, row=8)

nzdl = tk.Label(window1, text="New Zealand Dollars")
nzdl.grid(column=2, row=9)

nzdo = tk.Label(window1, text=" ")
nzdo.grid(column=3, row=9)

gbpl = tk.Label(window1, text="Great Britain Pounds")
gbpl.grid(column=2, row=10)

gbpo = tk.Label(window1, text=" ")
gbpo.grid(column=3, row=10)

chfl = tk.Label(window1, text="Swiss Francs")
chfl.grid(column=2, row=11)

chfo = tk.Label(window1, text=" ")
chfo.grid(column=3, row=11)

usdl = tk.Label(window1, text="US Dollars")
usdl.grid(column=2, row=12)

usdo = tk.Label(window1, text=" ")
usdo.grid(column=3, row=12)

error1 = tk.Label(window1, text=" ")
error1.grid(column=0, row=5)

explain = tk.Label(window1, text="Type your amount into the box")
explain.grid(column=0, row=0)

explain2 = tk.Label(window1, text="Select which currency you have and press convert")
explain2.grid(column=0, row=1)

explain3 = tk.Label(window1, text="This is the ten major currencies on 27 Feb 2021")
explain3.grid(column=0, row=3)

window1.title("Currency Converter")
window1.mainloop()
