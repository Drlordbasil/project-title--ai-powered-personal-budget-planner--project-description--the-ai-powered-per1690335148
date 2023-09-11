import tkinter as tk
from tkinter import messagebox
Optimized Python script:

```python


def generate_budget_plan(income: int, expenses: int, financial_goals: str) -> dict:
    # AI algorithm to generate personalized budget plan
    budget_plan = {}

    # Perform calculations and generate budget plan

    return budget_plan


class BudgetPlannerApp(tk.Tk):
    def __init__(self):
        self.title("AI-Powered Personal Budget Planner")

        # Initialize variables
        self.income_var = tk.IntVar()
        self.expenses_var = tk.IntVar()
        self.financial_goals_var = tk.StringVar()

        # Create user interface
        self.create_widgets()

    def create_widgets(self):
        # Create labels and entry fields for income, expenses, and financial goals
        tk.Label(self, text="Income:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self, textvariable=self.income_var).grid(
            row=0, column=1, padx=10)

        tk.Label(self, text="Expenses:").grid(
            row=1, column=0, padx=10, pady=10)
        tk.Entry(self, textvariable=self.expenses_var).grid(
            row=1, column=1, padx=10)

        tk.Label(self, text="Financial Goals:").grid(
            row=2, column=0, padx=10, pady=10)
        tk.Entry(self, textvariable=self.financial_goals_var).grid(
            row=2, column=1, padx=10)

        # Create submit button
        tk.Button(self, text="Submit", command=self.generate_budget_plan).grid(
            row=3, column=0, columnspan=2, pady=10)

    def generate_budget_plan(self):
        # Get user inputs and validate them
        income = self.income_var.get()
        expenses = self.expenses_var.get()
        financial_goals = self.financial_goals_var.get()

        if income <= 0:
            messagebox.showerror(
                "Error", "Income should be greater than zero.")
            return

        if expenses <= 0:
            messagebox.showerror(
                "Error", "Expenses should be greater than zero.")
            return

        # Generate budget plan
        budget_plan = generate_budget_plan(income, expenses, financial_goals)

        # Display budget plan to the user
        messagebox.showinfo("Budget Plan", str(budget_plan))


if __name__ == "__main__":
    # Create an instance of the budget planner app
    app = BudgetPlannerApp()
    app.mainloop()
```
