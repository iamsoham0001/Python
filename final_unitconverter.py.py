from tkinter import *


# Conversion factors
unit_dict = {
    "cm" : 0.01,
    "m" : 1.0,
    "km": 1000.0,
    "feet": 0.3048,

 

 
    "miles": 1609.344,
    "inches": 0.0254,
    "grams" : 1.0,
    "kg" : 1000.0,
    "quintals": 100000.0,
    "tonnes" : 1000000.0,
    "pounds" : 453.592,
    "sq. m" : 1.0,
    "sq. km": 1000000.0,
    "are" : 100.0,
    "hectare" : 10000.0,
    "acre": 4046.856,
    "sq. mile" : 2590000.0,
    "sq. foot" : 0.0929,
    "cu. cm" : 0.001,
    "Litre" : 1.0,
    "ml" : 0.001,
    "gallon": 3.785
}

lengths = ["cm", "m", "km", "feet", "miles", "inches",]
weights = ["kg", "grams", "quintals", "tonnes", "pounds",]
temps = ["Celsius", "Fahrenheit"]
areas = ["sq. m", "sq. km", "are", "hectare", "acre", "sq. mile", "sq. foot"]
volumes = ["cu. cm", "Litre", "ml", "gallon"]



OPTIONS = ["select units","cm","m","km","feet","miles","inches",
            "kg","grams","quintals","tonnes","pounds",
            "Celsius","Fahrenheit",
            "sq. m","sq. km","are","hectare","acre","sq. mile","sq. foot","cu. cm",
            "Litre","ml","gallon"]


root=Tk()
root.geometry("450x400")
root.title("")
root['bg'] = '#90CAF9'
header = Label(root,text="Unit Converter",font ="Cambria 20",bg = '#90CAF9').place(x=100,y=10)

def convert():
    input = float(input_entry.get())
    inp_unit = input_options.get()
    out_unit = output_options.get()
 
    cons = [inp_unit in lengths and out_unit in lengths,
    inp_unit in weights and out_unit in weights,
    inp_unit in temps and out_unit in temps,
    inp_unit in areas and out_unit in areas,
    inp_unit in volumes and out_unit in volumes]
 
    if any(cons): # If both the units are of same type, do the conversion
        if inp_unit == "Celsius" and out_unit == "Fahrenheit":
            output_entry.delete(0, END)
            output_entry.insert(0, (inp * 1.8) + 32)
        elif inp_unit == "Fahrenheit" and out_unit == "Celsius":
            output_entry.delete(0, END)
            output_entry.insert(0, (inp - 32) * (5/9))
        else:
            output_entry.delete(0, END)
            output_entry.insert(0, round(input * unit_dict[inp_unit]/unit_dict[out_unit], 5))
 
    else: # Display error if units are of different types
         output_entry.delete(0, END)
         output_entry.insert(0, "ERROR")

input_options = StringVar()
input_options.set(OPTIONS[0])

output_options = StringVar()
output_options.set(OPTIONS[0])

input_label = Label(root,text = "From :",font ="georgia",bg = '#90CAF9')               #.place(x=10,y=60)
input_label.grid(row=1,column=0,padx=5,pady=50)

input_entry = Entry(root,justify="center",font = "bold",bg='#FAE5D3')               #.place(x=80,y=60)
input_entry.grid(row=1,column=1)


input_menu = OptionMenu(root,input_options,*OPTIONS)                   #.place(x=350,y=60)
input_menu.grid(row=1,column=2)
input_menu.config(bg='#F9E79F',font='Arial 10')

output_label = Label(root,text = "To :",font ="georgia",bg = '#90CAF9')               #.place(x=10,y=120)
output_label.grid(row=2,column=0)

output_entry = Entry(root,justify="center",font = "bold",bg='#FAE5D3')               #.place(x=80,y=120)
output_entry.grid(row=2,column=1)

output_menu = OptionMenu(root,output_options, *OPTIONS)                #.place(x=350,y=120)
output_menu.grid(row=2,column=2)
output_menu.config(bg='#F9E79F',font='Arial 10')

convert_button = Button(root,text = "Convert",font = 'georgia',bg='#EEFF41',border = 3,command = convert).place(x=200,y=200)


root.mainloop()