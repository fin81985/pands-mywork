# convert.py

def convert_to_cents(amount):
    # Convert the amount to absolute value and then to cents
    cents = int(round(abs(amount) * 100))
    return cents

if __name__ == "__main__":
    # Take input from the user
    amount = float(input("Please enter an amount:"))
    
    # Convert to cents
    cents = convert_to_cents(amount)
    
    # Display the result
    print(f"That amount in cent is :{cents}")
