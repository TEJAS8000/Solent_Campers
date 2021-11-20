import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, Frame
from tkcalendar import DateEntry
from tkinter.filedialog import asksaveasfile
from csv import DictWriter
import json

# sys.stdout = open('BACKUP/output.txt', 'w')
# sys.stderr = open('BACKUP/error.txt', 'w')


def main():
    def user_login():

        class User(tk.Frame):

            def __init__(self, window, *args, **kwargs):
                super().__init__(window, *args, **kwargs)

                self.windows = window

                style = ttk.Style()
                style.configure('TNotebook.Tab', font=('URW Gothic L', '21', 'bold'), padding=[10, 10])

                tab_control = ttk.Notebook(window)

                self.tab1 = ttk.Frame(tab_control, width=1000, height=100)
                self.tab2 = ttk.Frame(tab_control)
                self.tab3 = ttk.Frame(tab_control)

                tab_control.add(self.tab1, text='Van Type')
                tab_control.add(self.tab2, text='Region')
                tab_control.add(self.tab3, text='Details')
                tab_control.pack(expand=500, fill="both")

                with open('camper_vans.json', 'r') as openfile:
                    # Reading from json file
                    json_object = json.load(openfile)

                self.camper_vans = []

                for each in json_object["camper_vans"]:
                    self.camper_vans.append([each["name"], each["type"], each["capacity"], each["price"],
                                             each["availability"]])

                self.lb1_add = tk.Label(self.tab1, text="Name", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb1_add.place(x=60, y=70)

                self.textfield1_add = ttk.Combobox(self.tab1, font=("Helvetica", 10), state='readonly')
                self.textfield1_add.place(x=180, y=70, width=280)

                self.lb2_add = tk.Label(self.tab1, text="Type", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb2_add.place(x=500, y=70)

                self.textfield2_add = ttk.Combobox(self.tab1, font=("Helvetica", 10), state='readonly')
                self.textfield2_add.place(x=620, y=70, width=280)

                self.lb3_add = tk.Label(self.tab1, text="Capacity", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb3_add.place(x=60, y=100)

                self.textfield3_add = ttk.Combobox(self.tab1, font=("Helvetica", 10), state='readonly')
                self.textfield3_add.place(x=180, y=100, width=280)

                self.lb4_add = tk.Label(self.tab1, text="Price", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb4_add.place(x=500, y=100)

                self.textfield4_add = ttk.Combobox(self.tab1, font=("Helvetica", 10), state='readonly')
                self.textfield4_add.place(x=620, y=100, width=280)

                def selectItem(a):

                    cur_item = self.tree.focus()
                    print(self.tree.item(cur_item)["values"][0], a)

                    self.textfield1_add.set(self.tree.item(cur_item)["values"][0])
                    self.textfield2_add.set(self.tree.item(cur_item)["values"][1])
                    self.textfield3_add.set(self.tree.item(cur_item)["values"][2])
                    self.textfield4_add.set(self.tree.item(cur_item)["values"][3])

                self.frame = Frame(self.tab1)
                self.frame.place(x=60, y=180)

                self.tree = ttk.Treeview(self.frame, columns=(1, 2, 3, 4, 5), height=7, show="headings")
                self.tree.pack(side='left')
                self.tree.bind('<ButtonRelease-1>', selectItem)

                self.val = ["Name", "Type", "Capacity", "Price", "Availability"]

                for i in range(1, len(self.val) + 1):
                    self.tree.heading(i, text=self.val[i - 1])

                for i in range(1, len(self.val) + 1):
                    self.tree.column(i, width=165, anchor='center')

                self.scroll1 = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
                self.scroll1.pack(side='right', fill='y')

                for i in range(len(self.camper_vans)):
                    if int(self.camper_vans[i][4]) > 0:
                        self.tree.insert('', 'end', values=(
                            str(self.camper_vans[i][0]), str(self.camper_vans[i][1]),
                            str(self.camper_vans[i][2]), str(self.camper_vans[i][3]),
                            str(self.camper_vans[i][4])), tags=('odd',))

                self.lb7 = tk.Label(self.tab1, text="User Name", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb7.place(x=60, y=400)

                self.textfield7_add = ttk.Entry(self.tab1, font=("Helvetica", 10))
                self.textfield7_add.place(x=180, y=400, width=720)

                self.lb8 = tk.Label(self.tab1, text="Driving Card Id", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb8.place(x=60, y=430)

                self.textfield8_add = ttk.Entry(self.tab1, font=("Helvetica", 10))
                self.textfield8_add.place(x=180, y=430, width=300)

                self.lb9 = tk.Label(self.tab1, text="Travellers", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb9.place(x=500, y=430)

                self.textfield9_add = ttk.Entry(self.tab1, font=("Helvetica", 10))
                self.textfield9_add.place(x=600, y=430, width=300)

                self.lb10 = tk.Label(self.tab1, text="Journey Date", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb10.place(x=60, y=460)

                self.textfield10_add = DateEntry(self.tab1, font=("Helvetica", 10), state='readonly',
                                                 date_pattern='mm/dd/yyyy', anchor='center')
                self.textfield10_add.place(x=180, y=460, width=300)

                self.lb11 = tk.Label(self.tab1, text="Return Date", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb11.place(x=500, y=460)

                self.textfield11_add = DateEntry(self.tab1, font=("Helvetica", 10), state='readonly',
                                                 date_pattern='mm/dd/yyyy', anchor='center')
                self.textfield11_add.place(x=600, y=460, width=300)

                with open('region.json', 'r') as openfile:
                    # Reading from json file
                    json_object = json.load(openfile)

                self.region = json_object["Region"]
                print(self.region)

                self.main_region = {}

                for each in self.region:
                    for key, value in each.items():
                        self.main_region[key] = value

                def callbackFunc(event):
                    print(event)
                    self.textfield13_add.destroy()
                    self.textfield13_add = ttk.Combobox(self.tab1, font=("Helvetica", 10),
                                                        values=self.main_region[str(self.textfield12_add.get())],
                                                        state='readonly')
                    self.textfield13_add.place(x=600, y=490, width=300)

                self.lb12 = tk.Label(self.tab1, text="Region", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb12.place(x=60, y=490)

                self.textfield12_add = ttk.Combobox(self.tab1, font=("Helvetica", 10),
                                                    values=list(self.main_region.keys()), state='readonly')
                self.textfield12_add.place(x=180, y=490, width=300)
                self.textfield12_add.bind("<<ComboboxSelected>>", callbackFunc)

                self.lb13 = tk.Label(self.tab1, text="Sub Region", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb13.place(x=500, y=490)

                self.textfield13_add = ttk.Combobox(self.tab1, font=("Helvetica", 10), state='readonly')
                self.textfield13_add.place(x=600, y=490, width=300)

                self.btn_add_ok1 = ttk.Button(self.tab1, text="Save Booking", command=self.validate)
                self.btn_add_ok1.place(x=60, y=545, width=200, height=35)

            def validate(self):
                messagebox.showinfo("Warning", "Please ensure fields have been filled.")

                if (str(self.textfield1_add.get()) != "") and (str(self.textfield2_add.get()) != "") and (
                        str(self.textfield3_add.get()) != "") and (str(self.textfield4_add.get()) != "") and (
                        str(self.textfield7_add.get()) != "") and (str(self.textfield8_add.get()) != "") and (
                        str(self.textfield9_add.get()) != "") and (str(self.textfield10_add.get()) != "") and (
                        str(self.textfield11_add.get()) != "") and (str(self.textfield12_add.get()) != "") and (
                        str(self.textfield13_add.get()) != ""):

                    json_data = {
                        "van_name": str(self.textfield1_add.get()),
                        "van_type": str(self.textfield2_add.get()),
                        "van_capacity": str(self.textfield3_add.get()),
                        "van_price": str(self.textfield4_add.get()),
                        "user_name": str(self.textfield7_add.get()),
                        "id_card": str(self.textfield8_add.get()),
                        "no_of_travellers": str(self.textfield9_add.get()),
                        "journey_date": str(self.textfield10_add.get()),
                        "return_date": str(self.textfield11_add.get()),
                        "region": str(self.textfield12_add.get()),
                        "sub_region": str(self.textfield13_add.get())
                    }

                    json_object = json.dumps(json_data, indent=4)

                    # Writing to sample.json
                    f = asksaveasfile(initialfile='Untitled.json', defaultextension=".json",
                                      filetypes=[("Json", "*.*")])

                    f.write(json_object)
                    f.close()

                    field_names = ['Van Name', 'Van type', 'Van capacity', 'Van Price',	'User Name', 'Driver ID Number',
                                   'No Of Travellers', 'Journey Date',	'Return Date',	'Region', 'Sub Region']

                    booking = {'Van Name': str(self.textfield1_add.get()), 'Van type': str(self.textfield2_add.get()),
                               'Van capacity': str(self.textfield3_add.get()),
                               'Van Price': str(self.textfield4_add.get()), 'User Name': str(self.textfield7_add.get()),
                               'Driver ID Number': str(self.textfield8_add.get()),
                               'No Of Travellers': str(self.textfield9_add.get()),
                               'Journey Date': str(self.textfield10_add.get()),
                               'Return Date': str(self.textfield11_add.get()),
                               'Region': str(self.textfield12_add.get()), 'Sub Region': str(self.textfield13_add.get())}

                    # Open your CSV file in append mode
                    # Create a file object for this file
                    with open('bookings.csv', 'a') as f_object:

                        # Pass the file object and a list
                        # of column names to DictWriter()
                        # You will get a object of DictWriter
                        dictwriter_object = DictWriter(f_object, fieldnames=field_names)

                        # Pass the dictionary as an argument to the Writerow()
                        dictwriter_object.writerow(booking)

                        # Close the file object
                        f_object.close()

                    messagebox.showinfo("Successfully", "The data saved into Json Data successfully")
                    window_user_login.destroy()
                    user_login()
                else:
                    messagebox.showerror("Operation failed", "The data cannot be saved. Enter data invalid")

        def exits():

            msgobj_close = messagebox.askquestion('Warning', 'Your changes have not been saved. would you '
                                                             'like to Exit ?',
                                                  icon='warning')
            if msgobj_close == "yes":
                exit(0)
            else:
                pass

        window_user_login = tk.Tk()
        window_user_login.config(background='#EFEFEF')
        # window_user_login_2.attributes('-alpha', 0.97)
        User(window_user_login)
        # user_login_window.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)
        window_user_login.title('Solent Campers')
        window_user_login.geometry("1000x680")
        window_user_login.resizable(False, False)
        window_user_login.protocol('WM_DELETE_WINDOW', exits)
        window_user_login.mainloop()

    user_login()


if __name__ == '__main__':
    main()
