import json
import os
import sys
import argparse
from datetime import datetime
from typing import List, Dict, Any, Optional

EXPENSE_FILE = 'expenses.json'

class ExpenseTracker:
    def __init__(self):
        self.expenses: List[Dict[str, Any]] = self.load_expenses()

    def load_expenses(self) -> List[Dict[str, Any]]:
        if not os.path.exists(EXPENSE_FILE):
            return []
        try:
            with open(EXPENSE_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []

    def save_expenses(self):
        with open(EXPENSE_FILE, 'w') as f:
            json.dump(self.expenses, f, indent=4)

    def add_expense(self, description: str, amount: float):
        if amount < 0:
            print("Error: Amount cannot be negative.")
            return

        expense_id = 1
        if self.expenses:
            expense_id = max(e['id'] for e in self.expenses) + 1
        
        expense = {
            'id': expense_id,
            'date': datetime.now().strftime("%Y-%m-%d"),
            'description': description,
            'amount': amount
        }
        self.expenses.append(expense)
        self.save_expenses()
        print(f"Expense added successfully (ID: {expense_id})")

    def update_expense(self, expense_id: int, description: str = None, amount: float = None):
        for expense in self.expenses:
            if expense['id'] == expense_id:
                if description:
                    expense['description'] = description
                if amount is not None:
                    if amount < 0:
                         print("Error: Amount cannot be negative.")
                         return
                    expense['amount'] = amount
                self.save_expenses()
                print(f"Expense updated successfully (ID: {expense_id})")
                return
        print(f"Error: Expense with ID {expense_id} not found.")

    def delete_expense(self, expense_id: int):
        for i, expense in enumerate(self.expenses):
            if expense['id'] == expense_id:
                del self.expenses[i]
                self.save_expenses()
                print("Expense deleted successfully")
                return
        print(f"Error: Expense with ID {expense_id} not found.")

    def list_expenses(self):
        print(f"{'ID':<5} {'Date':<12} {'Description':<20} {'Amount':<10}")
        for expense in self.expenses:
            print(f"{expense['id']:<5} {expense['date']:<12} {expense['description']:<20} ${expense['amount']:<10}")

    def summary(self, month: int = None):
        total = 0
        filtered_expenses = []
        
        if month:
            current_year = datetime.now().year
            for expense in self.expenses:
                try:
                    expense_date = datetime.strptime(expense['date'], "%Y-%m-%d")
                    if expense_date.month == month and expense_date.year == current_year:
                        filtered_expenses.append(expense)
                except ValueError:
                    continue 
            
            total = sum(e['amount'] for e in filtered_expenses)
            month_name = datetime(current_year, month, 1).strftime("%B")
            print(f"Total expenses for {month_name}: ${total}")
        else:
            total = sum(e['amount'] for e in self.expenses)
            print(f"Total expenses: ${total}")
def print_usage():
    print("Usage: expense_tracker.py [command] [options]\n\n\n")
    print("Available commands:")
    print("  add - Add a new expense")
    print("  update - Update an existing expense")
    print("  delete - Delete an expense")
    print("  list - List all expenses")
    print("  summary - Show summary of expenses")

    print("\n\n\n===================Example===================")
    print("[ADD]  expense_tracker.py add --description 'Groceries' --amount 100")
    print("[UPDATE]  expense_tracker.py update --id 1 --description 'Groceries' --amount 150")
    print("[DELETE]  expense_tracker.py delete --id 1")
    print("[LIST]  expense_tracker.py list")
    print("[SUMMARY]  expense_tracker.py summary --month 1")

def main():
    # parser = argparse.parse_args()
    
    # We will use argparse subcommands manually or reconstruct logic because standard argparse requires defining arguments upfront.
    # Actually, let's use proper argparse subcommands.
    
    main_parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = main_parser.add_subparsers(dest='command', help='Available commands')

    # Add
    parser_add = subparsers.add_parser('add', help='Add a new expense')
    parser_add.add_argument('--description', required=True, help='Description of the expense')
    parser_add.add_argument('--amount', type=float, required=True, help='Amount of the expense')

    # Update
    parser_update = subparsers.add_parser('update', help='Update an existing expense')
    parser_update.add_argument('--id', type=int, required=True, help='ID of the expense to update')
    parser_update.add_argument('--description', help='New description')
    parser_update.add_argument('--amount', type=float, help='New amount')

    # Delete
    parser_delete = subparsers.add_parser('delete', help='Delete an expense')
    parser_delete.add_argument('--id', type=int, required=True, help='ID of the expense to delete')

    # List
    parser_list = subparsers.add_parser('list', help='List all expenses')

    # Summary
    parser_summary = subparsers.add_parser('summary', help='Show summary of expenses')
    parser_summary.add_argument('--month', type=int, help='Month number (1-12) for summary')

    args = main_parser.parse_args()
    tracker = ExpenseTracker()

    if args.command == 'add':
        tracker.add_expense(args.description, args.amount)
    elif args.command == 'update':
        tracker.update_expense(args.id, args.description, args.amount)
    elif args.command == 'delete':
        tracker.delete_expense(args.id)
    elif args.command == 'list':
        tracker.list_expenses()
    elif args.command == 'summary':
        tracker.summary(args.month)
    else:
        print_usage()

if __name__ == "__main__":
    main()
