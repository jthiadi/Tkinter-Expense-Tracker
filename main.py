# Checkpoint 3
# Justin Thiadi 程煒財 112006234

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
#import os
#import sys

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Record:
    """Represent a record."""
    def __init__(self, category, description, amount):
        """Create a record with category, description, and amount."""
        # 1. Define the formal parameters so that a Record can be instantiated # by calling Record('meal', 'breakfast', -50). 
        # 2. Initialize the attributes from the parameters. The attribute # names should start with an underscore (e.g. self._amount)
        self._category = category
        self._description = description
        self._amount = amount

    @property
    def category(self):
        """Return the record's category."""
        return self._category

    @property
    def description(self):
        """Return the record's description."""
        return self._description

    @property
    def amount(self):
        """Return the record's amount."""
        return self._amount


class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""
    def __init__(self, root):
        """Load data from file or ask for initial money."""
        # 1. Read from 'records.txt' or prompt for initial amount of money. 
        # 2. Initialize the attributes (self._records and self._initial_money) from the file or user input.
        self._records = []
        self._initial_money = 0

        try:
            with open("records.txt", "r") as f:
                first = f.readline().strip()
                if not first:
                    raise ValueError

                try:
                    self._initial_money = int(first)
                except ValueError:
                    messagebox.showerror(
                        "Error",
                        "Invalid first line in records.txt.\nStarting from 0.",
                        parent=root,
                    )
                    raise

                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split()
                    if len(parts) != 3:
                        messagebox.showerror(
                            "Error",
                            "Invalid record format in records.txt.\nStarting from 0.",
                            parent=root,
                        )
                        raise ValueError
                    category, description, amount_str = parts
                    try:
                        amount = int(amount_str)
                    except ValueError:
                        messagebox.showerror(
                            "Error",
                            "Invalid amount in records.txt.\nStarting from 0.",
                            parent=root,
                        )
                        raise
                    self._records.append(Record(category, description, amount))

        except (FileNotFoundError, ValueError):
            # Ask initial money via dialog
            value = simpledialog.askinteger(
                "Initial Money",
                "How much money do you have?",
                parent=root,
                minvalue=0,
            )
            self._initial_money = value if value is not None else 0
            self._records = []

    @property
    def initial_money(self):
        """Return the starting amount of money."""
        return self._initial_money

    @property
    def all_records(self):
        """Return a copy of all stored records."""
        return list(self._records)


    def balance(self):
        """Return current balance (initial money + all amounts)."""
        return self._initial_money + sum(r.amount for r in self._records)

    # extra feature
    def summary(self):
        """Return (total_income, total_expense, balance)."""
        incomes = [r.amount for r in self._records if r.amount > 0]
        expenses = [r.amount for r in self._records if r.amount < 0]
        total_income = sum(incomes) if incomes else 0
        total_expense = sum(expenses) if expenses else 0  # negative number
        return total_income, total_expense, self.balance()

    # extra feature (for pie chart)
    def totals_income_expense(self):
        """Return (total_income, total_expense_positive)."""
        incomes = [r.amount for r in self._records if r.amount > 0]
        expenses = [r.amount for r in self._records if r.amount < 0]

        total_income = sum(incomes) if incomes else 0
        # make expense positive for plotting
        total_expense = -sum(expenses) if expenses else 0
        return total_income, total_expense

    # extra feature
    def iter_expenses_above(self, threshold):
        """Yield records that are expenses with abs(amount) >= threshold."""
        for r in self._records:
            if r.amount < 0 and abs(r.amount) >= threshold:
                yield r

    def add(self, category, description, amount, categories_obj):
        """Add a new record after checking category validity."""
        # 1. Define the formal parameter so that a string input by the user representing a record can be passed in. 
        # 2. Convert the string into a Record instance. 
        # 3. Check if the category is valid. For this step, the predefined categories have to be passed in through the parameter. 
        # 4. Add the Record into self._records if the category is valid.

        if not category or not description:
            raise ValueError("Category and description cannot be empty.")

        if not categories_obj.is_category_valid(category):
            raise ValueError(
                'The specified category is not in the category list.\n You can check the category list by command "view categories".\n Fail to add a record.'
        )

        try:
            amount = int(amount)
        except ValueError:
            raise ValueError("Amount must be an integer.")

        self._records.append(Record(category, description, amount))
    
    '''def view(self):
        # 1. Print all the records and report the balance
        header = (
            "No.  Category        Description            Amount\n"
            "==== ============== ==================== ========\n"
        )

        if not self._records:
            print(header + "(No records)\n")
            return

        lines = []
        for i, record in enumerate(self._records, 1):
            lines.append(
                f"{i:<4} {record.category:<14} {record.description:<20} {record.amount:>8}"
            )

        table = "\n".join(lines)
        footer = "\n==== ============== ==================== ========\n"

        total_money = self._initial_money + sum(r.amount for r in self._records)
        total_line = f"Now you have {total_money} dollars.\n"

        print(header + table + footer + total_line)'''

    def delete(self, index):
        """Delete the record at the given index."""
        # 1. Define the formal parameter.
        # 2. Delete the specified record from self._records.
        if 0 <= index < len(self._records):
            self._records.pop(index)

    def find(self, cat_list):
        """Return records whose categories appear in the list."""
        # 1. Define the formal parameter to accept a non-nested list (returned from find_subcategories) 
        # 2. Print the records whose category is in the list passed in # and report the total amount of money of the listed records.
        if not cat_list:
            return []
        return [r for r in self._records if r.category in cat_list]

    def save(self):
        """Save initial money and all records to records.txt."""
        # 1. Write the initial money and all the records to 'records.txt'.
        with open("records.txt", "w") as f:
            f.write(str(self._initial_money) + "\n")
            for r in self._records:
                f.write(f"{r.category} {r.description} {r.amount}\n")

class Categories:
    """Maintain the category list and provide some methods."""

    def __init__(self):
        """Initialize the nested category list."""
        # 1. Initialize self._categories as a nested list.
        self._categories = [
            "expense",
            ["food", ["meal", "snack", "drink"], "transportation", ["bus", "railway"]],
            "income",
            ["salary", "bonus"],
        ]

    def view(self):
        """Return a formatted list of all categories."""
        # 1. Define the formal parameters so that this method can be called recursively. 
        # 2. Recursively print the categories with indentation. 
        # 3. Alternatively, define an inner function to do the recursion.

        lines = []

        def _view(cats, depth=0):
            if isinstance(cats, list):
                i = 0
                while i < len(cats):
                    item = cats[i]
                    if isinstance(item, str):
                        lines.append("  " * depth + f"- {item}")
                        if (
                            i + 1 < len(cats)
                            and isinstance(cats[i + 1], list)
                        ):
                            _view(cats[i + 1], depth + 1)
                            i += 1
                    else:
                        _view(item, depth + 1)
                    i += 1

        _view(self._categories)
        return "\n".join(lines)

    def is_category_valid(self, category, cats=None):
        """Check recursively whether a category exists."""
        # 1. Define the formal parameters so that a category name can be # passed in and the method can be called recursively. 
        # 2. Recursively check if the category name is in self._categories.
        # 3. Alternatively, define an inner function to do the recursion.
        if cats is None:
            cats = self._categories

        if isinstance(cats, list):
            for v in cats:
                if self.is_category_valid(category, v):
                    return True
            return False
        else:
            return cats == category

    def find_subcategories(self, category):
        """Return list of category and all its subcategories using a generator."""

        def find_subcategories_gen(category, cats, found=False):
            # A generator that yields the target category and its subcategories
            if isinstance(cats, list):
                for index, child in enumerate(cats):
                    # continue search
                    yield from find_subcategories_gen(category, child, found)

                    # if we just found the category and it has a subcategory list
                    if (
                        child == category
                        and index + 1 < len(cats)
                        and isinstance(cats[index + 1], list)
                    ):
                        # now go through its subcategories with found=True
                        yield from find_subcategories_gen(
                            category, cats[index + 1], True
                        )
            else:
                if cats == category or found:
                    yield cats

        return list(find_subcategories_gen(category, self._categories))
        # A list generated by find_subcategories_gen(category, self._categories)

# extra feature
class PymoneyApp:
    """Tkinter GUI wrapper around Records and Categories."""

    def __init__(self, root):
        self.root = root
        self.root.title("Pymoney - Tkinter Edition")

        self.categories = Categories()
        self.records = Records(root)

        self._build_widgets()
        self._refresh_table()

    def _build_widgets(self):
        """Create all UI components."""
        # top frame: balance
        top = tk.Frame(self.root)
        top.pack(fill="x", padx=10, pady=5)

        tk.Label(top, text="Now you have").pack(side="left")
        self.balance_var = tk.StringVar()
        tk.Label(top, textvariable=self.balance_var, font=("Arial", 11, "bold")).pack(
            side="left", padx=5
        )

        # middle frame: form
        form = tk.LabelFrame(self.root, text="Add Record")
        form.pack(fill="x", padx=10, pady=5)

        tk.Label(form, text="Category:").grid(row=0, column=0, padx=5, pady=3, sticky="e")
        tk.Label(form, text="Description:").grid(row=0, column=2, padx=5, pady=3, sticky="e")
        tk.Label(form, text="Amount:").grid(row=0, column=4, padx=5, pady=3, sticky="e")

        self.entry_category = tk.Entry(form, width=15)
        self.entry_desc = tk.Entry(form, width=20)
        self.entry_amount = tk.Entry(form, width=10)

        self.entry_category.grid(row=0, column=1, padx=5, pady=3)
        self.entry_desc.grid(row=0, column=3, padx=5, pady=3)
        self.entry_amount.grid(row=0, column=5, padx=5, pady=3)

        tk.Button(form, text="Add", command=self.on_add).grid(
            row=0, column=6, padx=5, pady=3
        )

        # filter frame
        filter_frame = tk.LabelFrame(self.root, text="Find / Filter")
        filter_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(filter_frame, text="Category:").grid(
            row=0, column=0, padx=5, pady=3, sticky="e"
        )
        self.entry_find_cat = tk.Entry(filter_frame, width=15)
        self.entry_find_cat.grid(row=0, column=1, padx=5, pady=3)

        tk.Button(filter_frame, text="Find by Category", command=self.on_find).grid(
            row=0, column=2, padx=5, pady=3
        )
        tk.Button(filter_frame, text="Clear Filter", command=self._refresh_table).grid(
            row=0, column=3, padx=5, pady=3
        )
        tk.Button(
            filter_frame, text="View Categories", command=self.on_view_categories
        ).grid(row=0, column=4, padx=5, pady=3)

        # big expenses (generator-based) filters
        tk.Label(filter_frame, text="Big expense ≥").grid(
            row=1, column=0, padx=5, pady=3, sticky="e"
        )
        self.entry_big_expense = tk.Entry(filter_frame, width=10)
        self.entry_big_expense.grid(row=1, column=1, padx=5, pady=3)

        tk.Button(
            filter_frame, text="Show Big Expenses", command=self.on_big_expenses
        ).grid(row=1, column=2, padx=5, pady=3)

        # table frame
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill="both", expand=True, padx=10, pady=5)
        self.total_var = tk.StringVar(value="")
        tk.Label(self.root, textvariable=self.total_var, font=("Arial", 11, "bold")).pack(pady=3)

        columns = ("category", "description", "amount")
        self.tree = ttk.Treeview(
            table_frame, columns=columns, show="headings", height=10
        )
        self.tree.heading("category", text="Category")
        self.tree.heading("description", text="Description")
        self.tree.heading("amount", text="Amount")

        self.tree.column("category", width=120, anchor="w")
        self.tree.column("description", width=200, anchor="w")
        self.tree.column("amount", width=80, anchor="e")

        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # bottom buttons
        bottom = tk.Frame(self.root)
        bottom.pack(fill="x", padx=10, pady=5)

        tk.Button(bottom, text="Delete Selected", command=self.on_delete).pack(
            side="left", padx=5
        )
        tk.Button(bottom, text="Save", command=self.on_save).pack(side="left", padx=5)

        # summary button
        tk.Button(bottom, text="Summary", command=self.on_summary).pack(
            side="left", padx=5
        )

        # pie chart button
        tk.Button(bottom, text="Pie: Income vs Expense", command=self.on_pie_chart).pack(
            side="left", padx=5
        )

        tk.Button(bottom, text="Exit", command=self.on_exit).pack(side="right", padx=5)

    def _refresh_balance(self):
        """Update the balance label."""
        self.balance_var.set(f"{self.records.balance()} dollars")

    def _refresh_table(self, filtered_records=None):
        """Refresh the table with all or filtered records."""    
        # clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        data = filtered_records if filtered_records is not None else self.records.all_records

        for idx, r in enumerate(data):
            self.tree.insert(
                "", "end", iid=str(idx), values=(r.category, r.description, r.amount)
            )

        self._refresh_balance()

    def on_add(self):
        """Handle adding a new record from user input."""
        cat = self.entry_category.get().strip()
        desc = self.entry_desc.get().strip()
        amt = self.entry_amount.get().strip()

        try:
            self.records.add(cat, desc, amt, self.categories)
        except ValueError as e:
            messagebox.showerror("Add Record Failed", str(e), parent=self.root)
            return

        # clear description and amount (keep category)
        self.entry_desc.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)

        self._refresh_table()

    def on_delete(self):
        """Delete the selected record in the table."""
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Delete", "No record selected.", parent=self.root)
            return

        iid = sel[0]
        idx = int(iid)
        self.records.delete(idx)
        self._refresh_table()

    def on_find(self):
        """Filter records by category and show total."""
        cat = self.entry_find_cat.get().strip()
        if not cat:
            messagebox.showinfo("Find", "Please enter a category.", parent=self.root)
            return

        cat_list = self.categories.find_subcategories(cat)
        if not cat_list:
            messagebox.showinfo(
                "Find",
                f'Category "{cat}" not found in category list.',
                parent=self.root,
            )
            self.total_var.set("")  # clear total
            return

        result = self.records.find(cat_list)

        # compute total for the filtered results
        total = sum(r.amount for r in result)

        # update table
        self._refresh_table(filtered_records=result)

        # show total
        self.total_var.set(f"The total amount above is {total}.")

    def on_view_categories(self):
        """Open a window showing all categories."""
        text = self.categories.view()
        top = tk.Toplevel(self.root)
        top.title("Categories")
        text_widget = tk.Text(top, width=40, height=20)
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget.insert("1.0", text)
        text_widget.config(state="disabled")

    # extra feature
    def on_big_expenses(self):
        """Show expenses greater than or equal to a threshold."""        
        value = self.entry_big_expense.get().strip()
        if not value:
            messagebox.showinfo(
                "Big Expenses", "Please enter a threshold.", parent=self.root
            )
            return
        try:
            threshold = int(value)
        except ValueError:
            messagebox.showerror(
                "Big Expenses", "Threshold must be an integer.", parent=self.root
            )
            return

        gen = self.records.iter_expenses_above(threshold)
        result = list(gen)

        if not result:
            messagebox.showinfo(
                "Big Expenses",
                f"No expenses with absolute amount ≥ {threshold}.",
                parent=self.root,
            )
        self._refresh_table(filtered_records=result)

    # extra feature
    def on_summary(self):
        """Show total income, expense, and balance."""
        inc, exp, bal = self.records.summary()
        message = (
            f"Total income:  {inc}\n"
            f"Total expense: {exp}\n"
            f"Balance:       {bal}"
        )
        messagebox.showinfo("Summary", message, parent=self.root)

    # extra feature 
    def on_pie_chart(self):
        """Display a pie chart of income vs expense."""
        total_income, total_expense = self.records.totals_income_expense()

        if total_income == 0 and total_expense == 0:
            messagebox.showinfo(
                "Pie Chart",
                "No income or expense data to display.",
                parent=self.root,
            )
            return

        labels = []
        sizes = []

        if total_income > 0:
            labels.append("Income")
            sizes.append(total_income)
        if total_expense > 0:
            labels.append("Expense")
            sizes.append(total_expense)

        win = tk.Toplevel(self.root)
        win.title("Income vs Expense")

        fig = Figure(figsize=(4, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")

        canvas = FigureCanvasTkAgg(fig, master=win)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def on_save(self):
        """Save all records to file."""
        self.records.save()
        messagebox.showinfo("Save", "Records saved to records.txt.", parent=self.root)

    def on_exit(self):
        """Ask to save and then close the app."""
        if messagebox.askyesno("exit", "Save before exiting?", parent=self.root):
            self.records.save()
        self.root.destroy()


def main():
    root = tk.Tk()
    app = PymoneyApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
