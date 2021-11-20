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

                self.btn_add1 = ttk.Button(self.tab1, text="Add Camper Van")
                self.btn_add1.place(x=60, y=240, width=300, height=32)

                self.btn_remove1 = ttk.Button(self.tab1, text="Remove Camper Van")
                self.btn_remove1.place(x=358, y=240, width=300, height=32)

                with open('camper_vans.json', 'r') as openfile:
                    # Reading from json file
                    json_object = json.load(openfile)

                self.camper_vans = []

                for each in json_object["camper_vans"]:
                    self.camper_vans.append([each["type"], each["capacity"], each["price"], each["availability"]])

                self.frame = Frame(self.tab1)
                self.frame.place(x=60, y=300)

                self.tree = ttk.Treeview(self.frame, columns=(1, 2, 3, 4), height=10, show="headings")
                self.tree.pack(side='left')

                self.val = ["Type", "Capacity", "Price", "Availability"]

                for i in range(1, len(self.val) + 1):
                    self.tree.heading(i, text=self.val[i - 1])

                for i in range(1, len(self.val) + 1):
                    self.tree.column(i, width=215, anchor='center')

                self.scroll1 = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
                self.scroll1.pack(side='right', fill='y')

                for i in range(len(self.camper_vans)):
                    self.tree.insert('', 'end', values=(
                        str(self.camper_vans[i][0]), str(self.camper_vans[i][1]),
                        str(self.camper_vans[i][2]),
                        str(self.camper_vans[i][3])), tags=('odd',))

                self.btn_add_ok1 = ttk.Button(self.tab1, text="Save Settings")
                self.btn_add_ok1.place(x=60, y=545, width=200, height=35)

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
