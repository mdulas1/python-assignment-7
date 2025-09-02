"""
Bank Account Simulation

Task:
- Manage simple bank accounts.
- Store accounts in dictionary { "account_number": {"name": str, "balance": float} }
- Deposit, withdraw, transfer between accounts.
- Use *args for batch deposits/withdrawals.
- Use **kwargs for flexible account creation (e.g., overdraft_limit).

// NOT FOR THIS TASK
Future OOP Extension:
- BankAccount class with methods deposit(), withdraw(), transfer().
- Bank class to manage all accounts.
"""

accounts = {}

def create_account(account_number, name, **kwargs):
    """Create an account with optional features like overdraft_limit."""
    if account_number in accounts:
        return f"account {account_number} aready exist"
    accounts[account_number] = {
        "name":name,
        "balance":0.0
    }
    #add any extra features (e.g , overdraft_limit)
    for key, value in kwargs.items():
        accounts[account_number][key] = value
    return f"Account created for {name} with account number {account_number}"

def deposit(account_number, *amounts):
    """Deposit money into account.
        return "Account not found!" (if account does not exists)
        return Deposited {amount} into {accounts name}'s account. if account exists
    """
    if account_number not in accounts:
        return "Account not found"
    total = sum(amounts)
    accounts[account_number]["balance"] += total
    return f"Doposited {total} into {accounts[account_number]["name"]}'s account"


def withdraw(account_number, amount):
    """Withdraw money if balance is sufficient. else: insufficient funds"""
    if account_number not in accounts:
        return "Account not found"
    balance = accounts[account_number]["balance"]
    overdraft = accounts[account_number].get("overdraft_limit",0)

    if balance + overdraft >= amount:
        accounts[account_number]["balance"] -= amount
        return f"Withdrew {amount} from {accounts[account_number]["name"]} account"
    else:
        return "insufficient funds"
    
def transfer(from_acc, to_acc, amount):
    """Transfer money between accounts. if funds is sufficient"""
    if from_acc not in accounts:
        return f"Sender account {from_acc} not found!"
    if to_acc not in accounts:
        return f"Receiver account {to_acc} not found!"
    
    balance = accounts[from_acc]["balance"]
    overdraft = accounts[from_acc].get("overdraft_limit", 0)
    
    if balance + overdraft >= amount:
        accounts[from_acc]["balance"] -= amount
        accounts[to_acc]["balance"] += amount
        return f"Transferred {amount} from {accounts[from_acc]['name']} to {accounts[to_acc]['name']}."
    else:
        return "Insufficient funds for transfer!"
    
print(create_account(10,"jibrin"))
print(create_account(11,"tanko",overdraft_limit=200))

print(deposit(10,400,1000))
print(deposit(11,500))

print(withdraw(10,700))
print(withdraw(11,300))
print(transfer(10,11,100))

print(accounts)