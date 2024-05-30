def currency_converter():
    """Converts an amount from one currency to another."""

    # Get user input for the amount and currencies
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency you are converting from: ").upper()
    to_currency = input("Enter the currency you are converting to: ").upper()

    # Define exchange rates
    exchange_rates = {
        "USD": {"EUR": 0.92, "GBP": 0.80, "JPY": 130.00, "CAD": 1.33, "AUD": 1.48, "CHF": 0.99, "CNY": 6.95, "INR": 74.83},
        "EUR": {"USD": 1.09, "GBP": 0.87, "JPY": 142.00, "CAD": 1.45, "AUD": 1.61, "CHF": 1.08, "CNY": 7.56, "INR": 81.33},
        "GBP": {"USD": 1.25, "EUR": 1.15, "JPY": 163.00, "CAD": 1.67, "AUD": 1.85, "CHF": 1.24, "CNY": 8.73, "INR": 93.44},
        "JPY": {"USD": 0.0077, "EUR": 0.0070, "GBP": 0.0061, "CAD": 0.0102, "AUD": 0.0114, "CHF": 0.0076, "CNY": 0.0535, "INR": 0.575},
        "CAD": {"USD": 0.75, "EUR": 0.69, "GBP": 0.60, "JPY": 98.00, "AUD": 1.11, "CHF": 0.74, "CNY": 5.23, "INR": 56.13},
        "AUD": {"USD": 0.67, "EUR": 0.62, "GBP": 0.54, "JPY": 88.00, "CAD": 0.90, "CHF": 0.67, "CNY": 4.71, "INR": 50.53},
        "CHF": {"USD": 1.01, "EUR": 0.93, "GBP": 0.81, "JPY": 132.00, "CAD": 1.35, "AUD": 1.49, "CNY": 7.03, "INR": 75.51},
        "CNY": {"USD": 0.14, "EUR": 0.13, "GBP": 0.11, "JPY": 18.73, "CAD": 0.19, "AUD": 0.21, "CHF": 0.14, "INR": 10.77},
        "INR": {"USD": 0.013, "EUR": 0.012, "GBP": 0.011, "JPY": 1.74, "CAD": 0.018, "AUD": 0.020, "CHF": 0.013, "CNY": 0.093}
    }

    # Check if the currencies are valid
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Invalid currency code. Please enter a valid currency code.")
        return

    # Convert the amount
    converted_amount = amount * exchange_rates[from_currency][to_currency]

    # Print the converted amount
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

# Call the currency converter function
currency_converter()