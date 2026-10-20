# Expense Tracker (Python)

A simple command-line expense tracker built with Python. It helps you record daily expenses, view them in a table, and see where your money goes. Your data is saved to a file, so nothing is lost when you close the program.

## Features

- Add an expense with title, amount, and category
- View all expenses in a clean table
- See the total amount spent
- Category-wise summary (food, travel, shopping, etc.)
- Delete a wrong entry
- Data is saved automatically in a JSON file
- Input validation: invalid input does not crash the program

## Technologies Used

- Python 3
- Built-in modules: `json`, `os`, `datetime`

## How to Run

1. Install [Python 3](https://www.python.org/downloads/)
2. Download `expense.py`
3. Open a terminal in the same folder and run:

```
python expense.py
```

(On Windows, you can also use `py expense.py`)

## Sample Menu

```
===== EXPENSE TRACKER =====
1. Add expense
2. View all expenses
3. Show total
4. Category-wise summary
5. Delete expense
6. Exit
```

## What I Learned

- Working with variables, lists, and dictionaries
- Using functions to organize code
- Reading and writing files with JSON
- Handling user input errors with `try` and `except`

## Future Improvements

- Month-wise reports
- Export to CSV or Excel
- Web version using Flask
- Monthly budget limit with warnings
