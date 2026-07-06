from tkinter import ttk
import tkinter as tk
from CONTROLLER import Car_Controller
controller=Car_Controller()
window=tk.Tk()
color1="#FFE1FF"
window.configure(bg=color1)

style = ttk.Style()
style.theme_use("default")
style.configure(
    "Treeview.Heading",
    background="#D8BFD8",
    foreground="black",
    font=("Segoe UI", 10, "bold")
)

#sart function-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def open_add_window():
    add_win=tk.Toplevel(window)
    add_win.title("Add Car")
    add_win.geometry("300x250")
    add_win.resizable(False ,False )
    color="#8B668B"
    add_win.configure(bg=color)
    tk.Label(add_win, text="Name" , bg=color).pack()
    name_e = tk.Entry(add_win , bd=3)
    name_e.pack()
    tk.Label(add_win, text="Model" , bg=color).pack()
    model_e = tk.Entry(add_win , bd=3)
    model_e.pack()
    tk.Label(add_win, text="Color" , bg=color).pack()
    color_e = tk.Entry(add_win ,bd=3)
    color_e.pack()
    tk.Label(add_win, text="Horse Power" , bg=color).pack()
    horse_power_e = tk.Entry(add_win , bd=3)
    horse_power_e.pack()

    tk.Button(add_win , text="confirmation " , command=lambda:controller.add_cars(name_e.get() , model_e.get() , color_e.get() , horse_power_e.get()) , bd=3).pack(pady=10)



def open_update_window():
    add_win=tk.Toplevel(window)
    add_win.title("update Car")
    add_win.geometry("300x300")
    add_win.resizable(False ,False )
    color="#CDB5CD"
    # "#8B668B"
    add_win.configure(bg=color)
    tk.Label(add_win, text="ID" , bg=color).pack()
    id_e=tk.Entry(add_win ,bd=3)
    id_e.pack()
    tk.Label(add_win, text="Name" , bg=color).pack()
    name_e = tk.Entry(add_win , bd=3)
    name_e.pack()
    tk.Label(add_win, text="Model" , bg=color).pack()
    model_e = tk.Entry(add_win , bd=3)
    model_e.pack()
    tk.Label(add_win, text="Color" , bg=color).pack()
    color_e = tk.Entry(add_win , bd=3)
    color_e.pack()
    tk.Label(add_win, text="Horse Power" , bg=color).pack()
    horse_power_e = tk.Entry(add_win , bd=3)
    horse_power_e.pack()

    tk.Button(add_win , text="confirmation " , command=lambda: controller.update_cars( id_e.get(),name_e.get() , model_e.get() , color_e.get() , horse_power_e.get()) , bd=3).pack(pady=10)
def refresh_treeview():
    treev.delete(*treev.get_children())
    cars=controller.show_all_cars()
    for car in cars:
        treev.insert("" , "end" , values=(car.Id , car.Name , car.Model , car.Color , car.Horse_Power) , tags=("green",))


#end function----------------------------------------------------------------------------------------------------------------------------------------------------------------------
window.title("car database")
window.geometry("1010x400")
window.resizable(False , False)
treev = ttk.Treeview(window , height=5)
treev.place(x=50, y=120, width=900, height=200)

verscrlbar = ttk.Scrollbar(window, orient ="vertical", command = treev.yview)
treev.configure(yscrollcommand = verscrlbar.set)
verscrlbar.place(x=950, y=120, height=200)

horscrlbar = ttk.Scrollbar(window,orient="horizontal",command=treev.xview)
horscrlbar.place(x=50, y=320, width=900)
treev.configure(xscrollcommand=horscrlbar.set)


treev["columns"] = ("1", "2", "3" , "4" , "5")
treev['show'] = 'headings'

treev.heading("1", text ="Id")
treev.heading("2", text ="Name")
treev.heading("3", text ="Model")
treev.heading("4", text ="Color")
treev.heading("5", text ="Horse Power")

treev.column("1" , anchor="center")
treev.column("2" , anchor="center")
treev.column("3" , anchor="center")
treev.column("4" , anchor="center")
treev.column("5" , anchor="center")

treev.tag_configure ( "green" , background="#FFE1FF")
treev.tag_configure( "green",background="#EED2EE")


color2="#F5F5F5"
tk.Button(window , text="Add" , command=open_add_window  ,width=10 , bd=3 ,bg=color2).place(y=50 , x=50)
tk.Button(window , text="update" , command=open_update_window , width=10 , bd=3 , bg=color2).place(y=50  , x=200)
tk.Button(window , text="delete" , command=lambda:controller.delete_cars(id_en1.get()),width=10 ,bd=3 , bg=color2).place(y=50 , x=350)
id_en1=tk.Entry(window)
id_en1.place(y=55 , x=440)
tk.Button(window , text="show all" , command=refresh_treeview , width=10 , bd=3 , bg=color2).place(y=50  , x=600)
window.mainloop()
