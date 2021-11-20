import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, Frame
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

                self.textfield1_add = ttk.Combobox(self.tab1, font=("Helvetica", 10))
                self.textfield1_add.place(x=180, y=70, width=280)

                self.lb2_add = tk.Label(self.tab1, text="Type", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb2_add.place(x=500, y=70)

                self.textfield2_add = ttk.Combobox(self.tab1, font=("Helvetica", 10))
                self.textfield2_add.place(x=620, y=70, width=280)

                self.lb3_add = tk.Label(self.tab1, text="Capacity", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb3_add.place(x=60, y=100)

                self.textfield3_add = ttk.Combobox(self.tab1, font=("Helvetica", 10))
                self.textfield3_add.place(x=180, y=100, width=280)

                self.lb4_add = tk.Label(self.tab1, text="Price", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb4_add.place(x=500, y=100)

                self.textfield4_add = ttk.Combobox(self.tab1, font=("Helvetica", 10))
                self.textfield4_add.place(x=620, y=100, width=280)

                self.lb5_add = tk.Label(self.tab1, text="Availability", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb5_add.place(x=60, y=130)

                self.textfield5_add = ttk.Combobox(self.tab1, font=("Helvetica", 10))
                self.textfield5_add.place(x=180, y=130, width=280)

                self.btn_add2 = ttk.Button(self.tab1, text="Add Van Type", command=self.add_van)
                self.btn_add2.place(x=60, y=180, width=300, height=32)

                self.btn_remove2 = ttk.Button(self.tab1, text="Remove Van Type", command=self.remove_van)
                self.btn_remove2.place(x=359, y=180, width=300, height=32)

                def selectItem(a):

                    cur_item = self.tree.focus()
                    print(self.tree.item(cur_item)["values"][0], a)

                    self.textfield1_add.set(self.tree.item(cur_item)["values"][0])
                    self.textfield2_add.set(self.tree.item(cur_item)["values"][1])
                    self.textfield3_add.set(self.tree.item(cur_item)["values"][2])
                    self.textfield4_add.set(self.tree.item(cur_item)["values"][3])

                self.frame = Frame(self.tab1)
                self.frame.place(x=60, y=245)

                self.tree = ttk.Treeview(self.frame, columns=(1, 2, 3, 4, 5), height=12, show="headings")
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

                self.btn_add_ok1 = ttk.Button(self.tab1, text="Save Van Details")
                self.btn_add_ok1.place(x=60, y=545, width=200, height=35)

                with open('region.json', 'r') as openfile:
                    # Reading from json file
                    json_object = json.load(openfile)

                self.region = json_object["Region"][0]
                print(self.region)

                self.main_region = []

                for each in self.region.keys():
                    self.main_region.append(each)

                self.lb12 = tk.Label(self.tab2, text="Region", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb12.place(x=60, y=100)

                self.textfield12_add = ttk.Combobox(self.tab2, font=("Helvetica", 10))
                self.textfield12_add.place(x=180, y=100, width=300)

                self.lb13 = tk.Label(self.tab2, text="Sub Region", font=("Helvetica", 10), bg='#EFEFEF')
                self.lb13.place(x=500, y=100)

                self.textfield13_add = ttk.Combobox(self.tab2, font=("Helvetica", 10))
                self.textfield13_add.place(x=600, y=100, width=300)

                self.frame2 = Frame(self.tab2)
                self.frame2.place(x=60, y=180)

                self.tree2 = ttk.Treeview(self.frame2, columns=(1, 2), height=14, show="headings")
                self.tree2.pack(side='left')

                self.val2 = ["Region", "Sub Region"]

                for i in range(1, len(self.val2) + 1):
                    self.tree2.heading(i, text=self.val2[i - 1])

                for i in range(1, len(self.val2) + 1):
                    self.tree2.column(i, width=415, anchor='center')

                self.scroll2 = ttk.Scrollbar(self.frame2, orient="vertical", command=self.tree2.yview)
                self.scroll2.pack(side='right', fill='y')

                for key, value in self.region.items():
                    for each in value:
                        self.tree2.insert('', 'end', values=(str(key), str(each)), tags=('odd',))

            def add_van(self):

                self.camper_vans.append([str(self.textfield1_add.get()), str(self.textfield2_add.get()),
                                         str(self.textfield3_add.get()),
                                         str(self.textfield4_add.get()),
                                         str(self.textfield5_add.get())])

                self.frame.destroy()

                self.frame = Frame(self.tab1)
                self.frame.place(x=60, y=245)

                self.tree = ttk.Treeview(self.frame, columns=(1, 2, 3, 4, 5), height=12, show="headings")
                self.tree.pack(side='left')

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

                messagebox.showinfo("Added", "Camera settings added successfully")

            def remove_van(self):

                if messagebox.askquestion('Warning', 'Are you sure you remove the selected van data ?',
                                          icon='warning') == 'yes':

                    print(self.tree.focus())

                    del self.camper_vans[int(self.tree.focus()[-1])-1]

                    self.frame.destroy()

                    self.frame = Frame(self.tab1)
                    self.frame.place(x=60, y=245)

                    self.tree = ttk.Treeview(self.frame, columns=(1, 2, 3, 4, 5), height=12, show="headings")
                    self.tree.pack(side='left')

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

                    messagebox.showinfo("Added", "Van details removed successfully")

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
