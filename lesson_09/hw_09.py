from exchange_rates import exchange_rates


class Price:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value

    def convert_to_usd(self):
        if self.currency == "USD":
            return self.amount
        elif self.currency in exchange_rates:
            exchange_rate = exchange_rates[self.currency]
            return self.amount * exchange_rate
        else:
            raise ValueError("Unsupported currency")

    def __add__(self, other):
        if self.currency == other.currency:
            return Price(self.amount + other.amount, self.currency)
        else:
            # If currencies are different, convert both to usd and then add
            amount1_in_usd = self.convert_to_usd()
            amount2_in_usd = other.convert_to_usd()
            return Price(amount1_in_usd + amount2_in_usd, "USD")

    def __sub__(self, other):
        if self.currency == other.currency:
            return Price(self.amount - other.amount, self.currency)
        else:
            # If currencies are different, convert both to usd and then subtract
            amount1_in_usd = self.convert_to_usd()
            amount2_in_usd = other.convert_to_usd()
            return Price(amount1_in_usd - amount2_in_usd, "USD")

    def __str__(self):
        if self.currency == "USD":
            return f"{self.amount:.2f} USD"
        else:
            return f"{self.amount:.2f} {self.currency}"


price1 = Price(100, "USD")
price2 = Price(50, "USD")
price3 = Price(30, "EUR")

result_add = price1 + price2
result_sub = price1 - price3

print(result_add)
print(result_sub)
