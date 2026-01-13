# Expense Tracker CLI

A simple command-line expense tracker application built with Python.

## Features

- **Add expenses** with description, amount, and automatic date tracking
- **Update existing expenses** (description and/or amount)
- **Delete expenses** by ID
- **List all expenses** in a formatted table
- **View summary** of expenses (total or monthly breakdown)
- **Persistent storage** using JSON file

## Installation

1. Ensure you have Python 3.6 or higher installed:
   ```bash
   python3 --version
   ```

2. Clone or download the project files.

3. The application has no external dependencies beyond Python's standard library.

## Usage

### Basic Commands

```bash
# Add a new expense
python3 expense_tracker.py add --description "Groceries" --amount 50.25

# Add another expense
python3 expense_tracker.py add --description "Dinner" --amount 30.75

# List all expenses
python3 expense_tracker.py list

# Update an expense (change description)
python3 expense_tracker.py update --id 1 --description "Supermarket Groceries"

# Update an expense (change amount)
python3 expense_tracker.py update --id 1 --amount 45.50

# Update both description and amount
python3 expense_tracker.py update --id 1 --description "Weekly Groceries" --amount 55.00

# Delete an expense
python3 expense_tracker.py delete --id 2

# View total summary of all expenses
python3 expense_tracker.py summary

# View monthly summary (January = month 1)
python3 expense_tracker.py summary --month 1
```

### Command Reference

| Command | Description | Required Arguments | Optional Arguments |
|---------|-------------|-------------------|-------------------|
| `add` | Add a new expense | `--description`, `--amount` | None |
| `update` | Update an existing expense | `--id` | `--description`, `--amount` |
| `delete` | Delete an expense | `--id` | None |
| `list` | List all expenses | None | None |
| `summary` | Show expense summary | None | `--month` (1-12) |

## Data Storage

- Expenses are stored in a file named `expenses.json` in the same directory as the script.
- The file uses JSON format for easy readability and manual editing if needed.
- Each expense has the following structure:
  ```json
  {
      "id": 1,
      "date": "2024-01-15",
      "description": "Groceries",
      "amount": 50.25
  }
  ```

## Examples

### Adding Expenses
```bash
python3 expense_tracker.py add --description "Coffee" --amount 4.50
python3 expense_tracker.py add --description "Bus ticket" --amount 2.75
python3 expense_tracker.py add --description "Movie tickets" --amount 25.00
```

### Listing Expenses
```
$ python3 expense_tracker.py list
ID    Date         Description          Amount    
--------------------------------------------------
1     2024-01-15   Groceries            $50.25    
2     2024-01-15   Coffee               $4.50     
3     2024-01-15   Movie tickets        $25.00    
```

### Viewing Summary
```
$ python3 expense_tracker.py summary
Total expenses: $79.75
Number of expenses: 3

$ python3 expense_tracker.py summary --month 1
Total expenses for January 2024: $79.75
Number of expenses: 3
```

## Error Handling

The application includes basic error handling for:
- Negative amounts (amount cannot be negative)
- Invalid expense IDs (when updating/deleting)
- Invalid month numbers (must be 1-12)
- Corrupted or missing data files

## Project Structure

```
expense_tracker/
├── expense_tracker.py   # Main application file
├── expenses.json        # Data file (auto-generated)
└── README.md           # This documentation
```

## Customization

### Changing Date Format
To change the date format, modify the `datetime.now().strftime()` call in the `add_expense` method. For example:
```python
# Change from "%Y-%m-%d" to "dd/mm/yyyy"
expense['date'] = datetime.now().strftime("%d/%m/%Y")
```

### Changing Currency Symbol
To use a different currency symbol, modify the `list_expenses` and `summary` methods where the `$` symbol is used.

### Adding Categories
To add expense categories:
1. Add a `--category` argument to the `add` and `update` commands
2. Modify the `add_expense` method to accept a category parameter
3. Update the expense dictionary structure
4. Modify the `list_expenses` method to display categories

## License

This project is open source and available for personal and educational use.

## Contributing

Feel free to fork this project and submit pull requests with improvements such as:
- Additional features (categories, tags, budgets)
- Enhanced reporting (weekly summaries, charts)
- Export functionality (CSV, Excel)
- GUI interface