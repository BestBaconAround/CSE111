import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, Dict, Tuple


def validate_amount(text: str) -> Tuple[bool, float]:
    try:
        amount = float(text)
    except ValueError:
        return False, 0.0
    if amount <= 0:
        return False, 0.0
    return True, amount


def add_expense(expenses: List[Dict], amount: float, category: str) -> List[Dict]:
    if category:
        clean_category = category.strip()
    else:
        clean_category = "Uncategorized"
    new_expense = {
        "amount": amount,
        "category": clean_category
    }
    new_list = expenses.copy()
    new_list.append(new_expense)
    return new_list


def calculate_total(expenses: List[Dict]) -> float:
    total = 0.0
    for expense in expenses:
        total += expense.get("amount", 0.0)
    return total


def calculate_remaining_budget(budget: float, total_spent: float) -> float:
    return budget - total_spent


class BudgetApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Smart Budget Tracker")
        self.expenses: List[Dict] = []
        self.budget_amount: float = 0.0
        self._build_widgets()

    def _build_widgets(self) -> None:
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.grid(row=0, column=0, sticky="NSEW")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        budget_label = ttk.Label(main_frame, text="Total Budget:")
        budget_label.grid(row=0, column=0, sticky="W", padx=5, pady=5)

        self.budget_entry = ttk.Entry(main_frame, width=15)
        self.budget_entry.grid(row=0, column=1, sticky="EW", padx=5, pady=5)

        set_budget_button = ttk.Button(
            main_frame,
            text="Set Budget",
            command=self.on_set_budget
        )
        set_budget_button.grid(row=0, column=2, sticky="EW", padx=5, pady=5)

        amount_label = ttk.Label(main_frame, text="Expense Amount:")
        amount_label.grid(row=1, column=0, sticky="W", padx=5, pady=5)

        self.amount_entry = ttk.Entry(main_frame, width=15)
        self.amount_entry.grid(row=1, column=1, sticky="EW", padx=5, pady=5)

        category_label = ttk.Label(main_frame, text="Category:")
        category_label.grid(row=2, column=0, sticky="W", padx=5, pady=5)

        self.category_entry = ttk.Entry(main_frame, width=20)
        self.category_entry.grid(row=2, column=1, sticky="EW", padx=5, pady=5)

        add_button = ttk.Button(
            main_frame,
            text="Add Expense",
            command=self.on_add_expense
        )
        add_button.grid(row=2, column=2, sticky="EW", padx=5, pady=5)

        self.total_label_var = tk.StringVar(value="Total Spent: $0.00")
        total_label = ttk.Label(main_frame, textvariable=self.total_label_var)
        total_label.grid(row=3, column=0, columnspan=3, sticky="W", padx=5, pady=5)

        self.remaining_label_var = tk.StringVar(value="Remaining Budget: $0.00")
        remaining_label = ttk.Label(main_frame, textvariable=self.remaining_label_var)
        remaining_label.grid(row=4, column=0, columnspan=3, sticky="W", padx=5, pady=5)

        expenses_label = ttk.Label(main_frame, text="Expenses:")
        expenses_label.grid(row=5, column=0, sticky="W", padx=5, pady=5)

        self.expenses_listbox = tk.Listbox(main_frame, height=10)
        self.expenses_listbox.grid(
            row=6,
            column=0,
            columnspan=3,
            sticky="NSEW",
            padx=5,
            pady=5
        )

        scrollbar = ttk.Scrollbar(
            main_frame,
            orient=tk.VERTICAL,
            command=self.expenses_listbox.yview
        )
        scrollbar.grid(row=6, column=3, sticky="NS")
        self.expenses_listbox.configure(yscrollcommand=scrollbar.set)

        clear_button = ttk.Button(
            main_frame,
            text="Clear Inputs",
            command=self.clear_inputs
        )
        clear_button.grid(row=7, column=0, columnspan=3, sticky="EW", padx=5, pady=5)

        main_frame.rowconfigure(6, weight=1)

    def on_set_budget(self) -> None:
        text = self.budget_entry.get().strip()
        is_valid, value = validate_amount(text)
        if not is_valid:
            messagebox.showerror(
                "Invalid Budget",
                "Please enter a positive number for the budget."
            )
            return
        self.budget_amount = value
        self.update_summary_labels()

    def on_add_expense(self) -> None:
        amount_text = self.amount_entry.get().strip()
        category_text = self.category_entry.get().strip()
        is_valid, amount_value = validate_amount(amount_text)
        if not is_valid:
            messagebox.showerror(
                "Invalid Amount",
                "Please enter a positive number for the expense amount."
            )
            return
        self.expenses = add_expense(
            self.expenses,
            amount_value,
            category_text
        )
        self.update_expenses_listbox()
        self.update_summary_labels()
        self.clear_expense_fields()

    def update_expenses_listbox(self) -> None:
        self.expenses_listbox.delete(0, tk.END)
        for index, expense in enumerate(self.expenses, start=1):
            amount = expense["amount"]
            category = expense["category"]
            line = f"{index}. ${amount:.2f} - {category}"
            self.expenses_listbox.insert(tk.END, line)

    def update_summary_labels(self) -> None:
        total_spent = calculate_total(self.expenses)
        remaining = calculate_remaining_budget(
            self.budget_amount,
            total_spent
        )
        self.total_label_var.set(f"Total Spent: ${total_spent:.2f}")
        self.remaining_label_var.set(f"Remaining Budget: ${remaining:.2f}")

    def clear_inputs(self) -> None:
        self.budget_entry.delete(0, tk.END)
        self.clear_expense_fields()

    def clear_expense_fields(self) -> None:
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)


def main() -> None:
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
