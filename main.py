import requests


def get_rate(from_currency="EUR", to_currency="USD"):
    """
    Fetches the live exchange rate between two currencies
    using the Frankfurter API.

    Args:
        from_currency (str): Source currency code (default: EUR).
        to_currency (str): Target currency code (default: USD).

    Returns:
        float: Exchange rate, or None if the request fails.
    """
    url = f"https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["rates"][to_currency]
    except requests.exceptions.ConnectionError:
        print("\nError: No internet connection. Please check your network.")
        return None
    except requests.exceptions.Timeout:
        print("\nError: The request timed out. Please try again.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"\nError fetching exchange rate: {e}")
        return None


def convert(amount, rate, direction):
    """
    Converts an amount between EUR and USD.

    Args:
        amount (float): The amount to convert.
        rate (float): The EUR/USD exchange rate.
        direction (int): 1 for EUR→USD, 2 for USD→EUR.

    Returns:
        str: Formatted conversion result.
    """
    if direction == 1:
        result = amount * rate
        return f"\nAmount in dollars: {amount} € -> {result:.2f} $"
    else:
        result = amount / rate
        return f"\nAmount in euros: {amount} $ -> {result:.2f} €"


def main():
    """Main loop — displays the menu and handles user input."""
    print("\nFetching live exchange rate...")
    rate = get_rate("EUR", "USD")

    if rate is None:
        print("Could not retrieve exchange rate. Exiting.")
        return

    print(f"Current rate: 1 EUR = {rate:.4f} USD\n")

    menu = (
        "Choose the conversion direction:\n"
        "1. Euros -> Dollars\n"
        "2. Dollars -> Euros\n"
        "0. Quit\n> "
    )

    while True:
        try:
            direction = int(input(menu))

            if direction == 0:
                print("\nProgram stopped. See you next time!")
                break

            if direction not in (1, 2):
                print("\nPlease choose only 1, 2 or 0.\n")
                continue

            amount = float(input("\nAmount (0 to quit): "))

            if amount == 0:
                print("\nProgram stopped. See you next time!")
                break

            if amount < 0:
                print("\nAmount must be a positive number.\n")
                continue

            print(f"\nAmount: {amount}")
            print(convert(amount, rate, direction))
            break

        except ValueError:
            print("\nInvalid value. Please enter a number.")


if __name__ == "__main__":
    main()
