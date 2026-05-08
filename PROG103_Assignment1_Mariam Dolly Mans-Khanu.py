# Constants for business tracking
BUSINESS_NAME = "Empower Growth Initiative"
CURRENCY = "Le"


def calculate_net_profit(total_sales, expenses):
    """Calculates the profit after subtracting operating costs."""
    return total_sales - expenses


def evaluate_growth(profit):
    """Provides a delicate feedback message based on economic performance."""
    if profit > 500:
        return "Excellent growth! Consider reinvesting in new inventory."
    elif profit > 0:
        return "Steady progress. You are maintaining decent work standards."
    else:
        return "Challenging day. Review expenses to ensure long-term sustainability."


def main():
    print(f"--- Welcome to the {BUSINESS_NAME} Sales Tracker ---")
    print("Aligning local business with SDG 8: Decent Work & Economic Growth\n")

    while True:
        # Input Section
        try:
            item_name = input("Enter the item or service sold (or type 'exit' to quit): ")
            if item_name.lower() == 'exit':
                break

            sales_count = int(input(f"How many units of '{item_name}' were sold? "))
            unit_price = float(input("Enter the price per unit: "))
            daily_expenses = float(input("Enter total operating expenses for this record: "))

            # Processing Section
            total_revenue = sales_count * unit_price
            net_profit = calculate_net_profit(total_revenue, daily_expenses)
            growth_message = evaluate_growth(net_profit)

            # Output Section
            print("-" * 40)
            print(f"SALES SUMMARY FOR: {item_name.upper()}")
            print(f"Total Revenue:  {CURRENCY} {total_revenue:,.2f}")
            print(f"Operating Cost: {CURRENCY} {daily_expenses:,.2f}")
            print(f"Net Profit:     {CURRENCY} {net_profit:,.2f}")
            print(f"Status:         {growth_message}")
            print("-" * 40)

        except ValueError:
            print("Invalid input. Please enter numerical values for prices and counts.")

    print("\nThank you for contributing to economic growth. Session closed.")


if __name__ == "__main__":
    main()