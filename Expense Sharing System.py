class ExpenseSharing:
    def __init__(self, members):
        self.members = members                             # Stores a list of people involved
        self.balances = {member: 0 for member in members}  # Dictionary to track how much each person owes or is owed, Initially, everyone’s balance is zero.

    def expense(self, payer, amount, people):              # Record a shared expense.
        split_amount = amount/len(people)                  # Calculate the equal split at every expenses
        for person in people:
            self.balances[person] -= split_amount          # Subtract each person’s share from their balance
        self.balances[payer] += amount                     # Add the total paid amount to the payer’s balance

    def individual_balance(self):                          # Display how much each person owes or is owed.
        for member, balance in self.balances.items():
            if balance>0:                                  # Positive balance → they should be reimbursed
                print(f"{member} needs to be reimbursed with Rs.{balance:.2f}")
            elif balance<0:                                # Negative balance → they owe money
                print(f"{member} owes Rs.{balance:.2f}") 

    def settlement(self):                                  # Calculate and print the simplest way to settle debts.
        creditors = []                                     # A list of people who are owed money (positive balance)
        debtors = []                                       # A list of people who owe money (negative balance)

        for member, balance in self.balances.items():
            if balance>0:
                creditors.append((member, balance))
            elif balance<0:
                debtors.append((member, -balance))

        while debtors and creditors:
            debtor, debt = debtors.pop()
            creditor, credit = creditors.pop()

            payment = min(debt, credit)                   # Calculates the maximum amount that a debtor can pay a creditor without overpaying

            print(f"{debtor} owes {creditor}: Rs.{payment:.2f}")

            if debt>payment:                              # If the debt or credit is not fully cleared, append the remaining back to the list.
                debtors.append((debtor, debt - payment))
            elif credit>payment:
                creditors.append((creditor, credit - payment))

if __name__ == "__main__":

    transaction_counter = 1

    members = input("Enter the names of Members involved in the Expenses, Separated by commas: ").split(",")
    members = [member.strip() for member in members]

    exp_share = ExpenseSharing(members)

    print('-' * 100)

    while True:

        print(f"Transaction: {transaction_counter}")

        i = True                                         # A flag to track anomaly entries
        payer = input("Enter the name of the payer (if Expenses are finished, the enter 'done')")
        
        if payer.lower() == 'done':                      # To indicate that the user finished entering Expenses details
            break
        elif payer not in members:                       # If the entered Payer is an anomaly entry, skip the current loop 
            print(f"{payer} is not a valid member.")
            continue

        amount = float(input("Enter the amount paid: "))

        people = input("Enter the names of the people involved in this transaction, Separated by commas: ").split(",")
        people = [person.strip() for person in people]

        for person in people:                           # If any of the entered members is an anomaly entry, the flag becomes false
            if person not in members:
                print(f"{person} is not a valid member.")
                i = False

        if i == False:                                  # To skip the current loop due to anomaly entries.
            continue

        exp_share.expense(payer, amount, people)
        transaction_counter += 1
        print('-' * 100)

    print('-' * 100)

    print("\n Individual Balance")
    exp_share.individual_balance()

    print('-' * 100)

    print("\n Final Settlement")
    exp_share.settlement()