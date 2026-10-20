import json
import os
from datetime import date

FILE_NAME = "expenses.json"


def load_expenses():
    """File se purane expenses padho. File na ho to khali list do."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_expenses(expenses):
    """Expenses ko file me save karo."""
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense(expenses):
    title = input("Kharcha kis cheez ka tha? ").strip()
    if title == "":
        print("Title khali nahi ho sakta.")
        return

    try:
        amount = float(input("Kitna kharcha hua? "))
    except ValueError:
        print("Amount number me daalo (jaise 150 ya 99.5).")
        return

    if amount <= 0:
        print("Amount 0 se zyada hona chahiye.")
        return

    category = input("Category (food/travel/shopping/other): ").strip().lower()
    if category == "":
        category = "other"

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": str(date.today()),
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense add ho gaya!")


def view_expenses(expenses):
    if len(expenses) == 0:
        print("Abhi koi expense nahi hai.")
        return

    print("\nNo.  Date         Category    Amount     Title")
    print("-" * 55)
    for i, e in enumerate(expenses, start=1):
        print(f"{i:<4} {e['date']:<12} {e['category']:<11} {e['amount']:<10.2f} {e['title']}")


def show_total(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"\nKul kharcha: Rs {total:.2f}")


def category_summary(expenses):
    if len(expenses) == 0:
        print("Abhi koi expense nahi hai.")
        return

    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]

    print("\nCategory-wise kharcha:")
    for cat, amt in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat:<12} Rs {amt:.2f}")


def delete_expense(expenses):
    if len(expenses) == 0:
        print("Delete karne ke liye kuch nahi hai.")
        return

    view_expenses(expenses)
    try:
        number = int(input("\nKaunsa number delete karna hai? "))
    except ValueError:
        print("Number daalo.")
        return

    if 1 <= number <= len(expenses):
        removed = expenses.pop(number - 1)
        save_expenses(expenses)
        print(f"'{removed['title']}' delete ho gaya.")
    else:
        print("Galat number.")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Expense add karo")
        print("2. Saare expenses dekho")
        print("3. Kul kharcha dekho")
        print("4. Category-wise summary")
        print("5. Expense delete karo")
        print("6. Exit")

        choice = input("Option chuno (1-6): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            print("Bye! Data save ho chuka hai.")
            break
        else:
            print("Galat option, 1 se 6 ke beech chuno.")


if __name__ == "__main__":
    main()
