print("********************INCOME TAX CALCULATOR**********************")
class IndianTaxFiling:
    def __init__(self, income):
        self.income = income

    def calculate_tax(self):
        if self.income <= 250000:
            return 0
        elif 250001 <= self.income <= 500000:
            return 0.05 * (self.income - 250000)
        elif 500001 <= self.income <= 1000000:
            return 0.05 * (500000 - 250000) + 0.2 * (self.income - 500000)
        else:
            return 0.05 * (500000 - 250000) + 0.2 * (1000000 - 500000) + 0.3 * (self.income - 1000000)

    def display_result(self):
        tax_amount = self.calculate_tax()
        print(f"Income: ₹{self.income}")
        print(f"Tax to be paid: ₹{tax_amount}")

def main():
    try:
        income = float(input("Enter your annual income in INR: "))
        filing = IndianTaxFiling(income)
        filing.display_result()
    except ValueError:
        print("Please enter a valid numerical value for income.")

if __name__ == "__main__":
    main()
    
