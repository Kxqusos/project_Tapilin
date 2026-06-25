import tkinter as tk
from tkinter import ttk, messagebox

BG, BG_ALT, ACCENT, BORDER = "#ffffff", "#f7f7f7", "#7a9e7a", "#d0d0d0"
FG, FG_MUTED, FG_REQ = "#111111", "#666666", "#c0392b"

F_TITLE = ("Arial", 13, "bold")
F_BOLD  = ("Arial", 9, "bold")
F_BASE  = ("Arial", 9)

ENTRY_KW = dict(bg=BG_ALT, relief="flat", highlightthickness=1,
                highlightbackground=BORDER, highlightcolor=ACCENT,
                font=F_BASE, bd=0)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Workshop Registration")
        self.resizable(False, False)
        self.configure(bg=BG)
        self._ttk_style()
        self._header()
        self._body()
        self._footer()

    def _ttk_style(self):
        s = ttk.Style(self)
        s.theme_use("clam")
        s.configure("TCombobox", fieldbackground=BG, background=BG,
                    foreground=FG, bordercolor=BORDER,
                    lightcolor=BORDER, darkcolor=BORDER, font=F_BASE)
        s.map("TCombobox",
              fieldbackground=[("readonly", BG)],
              selectbackground=[("readonly", BG)],
              selectforeground=[("readonly", FG)])

    def _header(self):
        f = tk.Frame(self, bg=ACCENT, pady=10, padx=16)
        f.pack(fill="x")
        tk.Label(f, text="Workshop Registration", bg=ACCENT,
                 fg="white", font=F_TITLE).pack(side="left")

    def _body(self):
        body = tk.Frame(self, bg=BG, padx=20, pady=16)
        body.pack(fill="both", expand=True)

        tk.Label(body, text="Register while seats are available",
                 bg=BG, fg=FG_MUTED, font=F_BASE
                 ).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 14))

        left = tk.Frame(body, bg=BG)
        left.grid(row=1, column=0, columnspan=2, sticky="nw", padx=(0, 32))

        self._section(left, "Personal Information")
        self.e_first   = self._field(left, "First Name", req=True)
        self.e_last    = self._field(left, "Last Name", req=True)
        self.e_company = self._field(left, "Company / Institution", req=True)

        self._lbl(left, "Address", req=True)
        self.t_address = tk.Text(left, width=34, height=4, **ENTRY_KW)
        self.t_address.grid(row=left.grid_size()[1], column=0, sticky="w")

        self.e_city     = self._field(left, "City")
        self.cb_state   = self._combo(left, "State / Province / Region",
                                      ["-", "NY", "CA", "TX"])
        self.cb_country = self._combo(left, "Country",
                                      ["-", "USA", "India", "UK", "Germany"])
        self._section(left, "Contact")
        self.e_email = self._field(left, "Email", req=True)
        self.e_phone = self._field(left, "Phone Number", req=True)

        right = tk.Frame(body, bg=BG)
        right.grid(row=1, column=2, columnspan=2, sticky="nw")

        self._section(right, "Lunch")
        self._lbl(right, "Meal Preference")
        self.cb_meal = ttk.Combobox(right, state="readonly", width=26,
                                    font=F_BASE,
                                    values=["Vegetarian", "Non-Vegetarian", "Vegan"])
        self.cb_meal.set("Vegetarian")
        self.cb_meal.grid(row=right.grid_size()[1], column=0,
                          sticky="w", ipady=3, pady=(0, 4))

        self._section(right, "Payment")
        self._lbl(right, "Payment Mode")
        chk = tk.Frame(right, bg=BG)
        chk.grid(row=right.grid_size()[1], column=0, sticky="w")
        self.var_cash, self.var_cheque, self.var_dd = (tk.BooleanVar() for _ in range(3))
        for text, var in [("Cash", self.var_cash), ("Cheque", self.var_cheque),
                          ("Demand Draft", self.var_dd)]:
            tk.Checkbutton(chk, text=text, variable=var, bg=BG, fg=FG,
                           font=F_BASE, activebackground=BG,
                           selectcolor=BG, relief="flat", bd=0).pack(anchor="w")
        self.e_ddno  = self._field(right, "DD / Cheque No.")
        self.e_bank  = self._field(right, "Drawn On (Bank Name)")
        self.e_payat = self._field(right, "Payable At")

    def _footer(self):
        tk.Frame(self, bg=BORDER, height=1).pack(fill="x")
        f = tk.Frame(self, bg=BG, pady=12)
        f.pack(fill="x")
        inner = tk.Frame(f, bg=BG)
        inner.pack()
        kw = dict(font=F_BOLD, relief="flat", bd=0, padx=20, pady=6, cursor="hand2")
        tk.Button(inner, text="Submit", command=self._submit,
                  bg=ACCENT, fg="white", activebackground="#5d7f5d",
                  activeforeground="white", **kw).pack(side="left", padx=(0, 8))
        tk.Button(inner, text="Reset", command=self._reset,
                  bg=BG_ALT, fg=FG, activebackground=BORDER,
                  activeforeground=FG, **kw).pack(side="left")

    def _section(self, parent, text):
        f = tk.Frame(parent, bg=BG)
        f.grid(row=parent.grid_size()[1], column=0, sticky="w", pady=(14, 6))
        tk.Frame(f, bg=ACCENT, width=3, height=14).pack(side="left")
        tk.Label(f, text=text, bg=BG, fg=FG, font=F_BOLD, padx=6).pack(side="left")

    def _lbl(self, parent, text, req=False):
        tk.Label(parent, bg=BG, font=F_BASE,
                 text=text + ("  *" if req else ""),
                 fg=FG_REQ if req else FG_MUTED
                 ).grid(row=parent.grid_size()[1], column=0,
                        sticky="w", pady=(6, 2))

    def _field(self, parent, label, req=False):
        self._lbl(parent, label, req)
        e = tk.Entry(parent, width=34, **ENTRY_KW)
        e.grid(row=parent.grid_size()[1], column=0, sticky="w", ipady=4)
        return e

    def _combo(self, parent, label, values):
        self._lbl(parent, label)
        cb = ttk.Combobox(parent, values=values, state="readonly",
                          width=32, font=F_BASE)
        cb.set(values[0])
        cb.grid(row=parent.grid_size()[1], column=0, sticky="w", ipady=3)
        return cb

    def _submit(self):
        messagebox.showinfo("Submitted", "Registration submitted successfully!")

    def _reset(self):
        for w in (self.e_first, self.e_last, self.e_company, self.e_city,
                  self.e_email, self.e_phone, self.e_ddno, self.e_bank, self.e_payat):
            w.delete(0, tk.END)
        self.t_address.delete("1.0", tk.END)
        for cb, val in [(self.cb_state, "-"), (self.cb_country, "-"),
                        (self.cb_meal, "Vegetarian")]:
            cb.set(val)
        for v in (self.var_cash, self.var_cheque, self.var_dd):
            v.set(False)


App().mainloop()