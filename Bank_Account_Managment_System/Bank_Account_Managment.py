# Enhanced Bank Account Management System with Loan Feature
from _datetime import datetime

# Initialize lists to hold account data
account_holders = []  # List to store account holder names
balances = []  # List to store corresponding balances
transaction_histories = []  # List to store transaction histories
loans = []  # List to store outstanding loans for each account

MAX_LOAN_AMOUNT = 10000  # Maximum loan amount
INTEREST_RATE = 0.03  # Interest rate for loans


def create_account():
    """Create a new bank account."""
    holder_name = input("Insert account holder's name:")    # 1. Prompt the user for the account holder's name.

                                                            # 2. Add the new account holder to the list of account holders.
    account_holders.append(holder_name)
    balances.append(0)                                      # 3. Corresponding balance initialized to 0
    transaction_histories.append([])                        # 4. Corresponding empty transaction history
    loans.append(0)                                         # 5. Corresponding loan amount initialized to 0

    print("The account was created successfully")           # 6. Notify the user of the successful account creation.


def deposit():
    """Deposit money into an account."""
    holder_name = input("Insert account holder's name:") # 1. Prompt the user for the account holder's name.

    if holder_name in account_holders:                    # 2. Check if the account exists in the system.

        account_index = account_holders.index(holder_name)  # 3. Get the index of the account holder to update the corresponding balance and transaction history

        amount_to_deposit = float(input("Insert amount to deposit:")) # 4.If the account exists, prompt the user for the amount to deposit.
        balances[account_index] += amount_to_deposit                    # 5.Update the account's balance
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 6.Format the current date and time
        transaction_histories[account_index].append(f"Deposited: {amount_to_deposit:.2f} BGN on {current_date}") # 7. Log the transaction in the account's transaction history
        print(f"New balance is : {amount_to_deposit}")  # 8.Display the updated balance to the user.
    else:
        print("Sorry, the account does not exist")                  # 9.If the account does not exist, inform the user.



def withdraw():
    """Withdraw money from an account."""
    holder_name = input("Insert account holder's name:")  # 1. Prompt the user for the account holder's name.

    if holder_name in account_holders:  # 2. Check if the account exists in the system.
        account_index = account_holders.index(holder_name)  # 2.Get the index of the account holder to update the corresponding balance and transaction history

        amount_to_withdraw = float(input("Insert amount to withdraw:")) # 3. If the account exists, prompt the user for the amount to withdraw.

        if balances[account_index] >= amount_to_withdraw:       # 4. Check if there are sufficient funds for the withdrawal.
            balances[account_index] -= amount_to_withdraw       # 5. If funds are sufficient, update the balance and log the transaction.

            print(f"Current balance is: {balances[account_index]:.2f} BGN")  # 6. Display the updated balance to the user.
            print("Transaction completed!")
            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 7.Format the current date and time
            transaction_histories[account_index].append(
                f"Withdrew: {amount_to_withdraw:.2f} BGN on {current_date}")  # 8.Log the transaction in the account's transaction history
        else:
            print("Insufficient funds")         # 9. If insufficient funds, inform the user.
    else:
           print("Sorry, the account does not exist")   # 10. If the account does not exist, inform the user.





def check_balance():
    """Check the balance of an account."""
    holder_name = input("Insert account holder's name:")  # 1. Prompt the user for the account holder's name.

    if holder_name in account_holders:  # 2. Check if the account exists in the system.
        account_index = account_holders.index(holder_name)  # 3.Get the index of the account holder to update the corresponding balance and transaction history
        print(f"Current balance is: {balances[account_index]} BGN.") # 4. If the account exists, display the current balance.
    else:
        print("Sorry, the account does not exist")  # 5. If the account does not exist, inform the user.


def list_accounts():
    """List all accounts and their balances."""
    if account_holders:# 1. Check if there are any accounts in the system.
        for account in account_holders: # 2. If there are accounts, loop through each account holder.
            current_index = account_holders.index(account) # 3.Get the index of the account holder

            print(f"{account} -> current balance :{balances[current_index]} BGN"
                  f"{account} -> outstanding loan:{loans[current_index]} BGN") # 4. Display the account holder's name, balance, and outstanding loan amount.

    else:
        print("Sorry, the account does not exist") # 5. If there are no accounts, inform the user.






def transfer_funds():
    """Transfer funds between two accounts."""
    sender = input("Input sender account holder name:")# 1. Prompt the user for the sender's and recipient's account holder names.
    recipient = input("Input recipient account holder name:")

    if sender in account_holders and recipient in account_holders: # 2. Check if both accounts exist in the system.
        amount_to_transfer = float(input("Import amount to transfer")) # 3. If both accounts exist, prompt the user for the amount to transfer.
        current_index_sender = account_holders.index(sender)
        current_index_recipient = account_holders.index(recipient)

        if balances[current_index_sender] > amount_to_transfer: # 4. Check if the sender has sufficient funds for the transfer.
            balances[current_index_sender] -= amount_to_transfer    # 5. If funds are sufficient, update both balances and log the transactions.
            balances[current_index_recipient] += amount_to_transfer

            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 6.Format the current date and time
            transaction_histories[current_index_sender].append(
                f"Amount transferred: {amount_to_transfer:.2f} BGN on {current_date}")
            transaction_histories[current_index_recipient].append(
                f"Amount received: {amount_to_transfer:.2f} BGN on {current_date}")  # 7.Log the transaction in the account's transaction history

            print("Tender transferred successfully!") # 8. Inform the user of the successful transfer.
        else:
            print("Insufficient funds") # 9. If insufficient funds does not exist, inform the user.
    else:
        print("Sorry, the account does not exist") # 10. if account does not exist, inform the user.


def view_transaction_history():
    """View transaction history for a specific account."""
    holder_name = input("Insert account holder's name:")  # 1. Prompt the user for the account holder's name.

    if holder_name in account_holders:  # 2. Check if the account exists in the system.
        if transaction_histories:
            print("\n".join(["\n".join(history) for history in transaction_histories])) # 3. Should show  transaction history on different lines.
        else:
            print("No transactions")        # 4. If there are no transactions, inform the user.
    else:
        print("Sorry, the account does not exist") # 5. If the account does not exist, inform the user.



def apply_for_loan():
    """Apply for a loan."""
    name = input("Enter the account holder's name: ")

    # Check if the account exists in the system
    if name in account_holders:
        index = account_holders.index(name)  # Find the account index

        # Prompt user for the loan amount they wish to apply for
        loan_amount = float(input(f"Enter the loan amount (max {MAX_LOAN_AMOUNT} leva): "))

        # Check if the loan amount is within the limit
        if loan_amount <= MAX_LOAN_AMOUNT:
            # Update balance and loan amount
            balances[index] += loan_amount
            loans[index] += loan_amount * (1 + INTEREST_RATE)  # Calculate total loan with interest

            print(f"Loan of {loan_amount:.2f} leva approved for {name}. New balance: {balances[index]:.2f} leva.")
        else:
            print(f"Loan amount exceeds maximum limit of {MAX_LOAN_AMOUNT} leva.")
    else:
        print("Account not found.")


def repay_loan():
    """Repay a loan."""
    name = input("Enter the account holder's name: ")

    # Check if the account exists in the system
    if name in account_holders:
        index = account_holders.index(name)  # Find the account index

        # Prompt user for repayment amount
        repayment_amount = float(input(f"Enter repayment amount (Outstanding loan: {loans[index]:.2f} leva): "))

        # Check if the repayment amount is valid
        if repayment_amount <= loans[index]:
            # Update balance and outstanding loan amount
            balances[index] -= repayment_amount
            loans[index] -= repayment_amount

            print(
                f"Repayment of {repayment_amount:.2f} leva accepted for {name}. Remaining loan: {loans[index]:.2f} leva.")
        else:
            print("Repayment amount exceeds outstanding loan.")
    else:
        print("Account not found.")


def display_menu():
    """Display the main menu."""
    print("\n--- Bank Account Management System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. List Accounts")
    print("6. Transfer Funds")
    print("7. View Transaction History")
    print("8. Apply for Loan")
    print("9. Repay Loan")
    print("10. Exit")

    # Prompt user for their choice
    choice = int(input("Enter your choice: "))
    return choice


def main():
    """Main function to run the banking system."""
    while True:
        choice = display_menu()  # Display the menu and get user choice

        # Process user input based on their choice
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please try again.")

main()
