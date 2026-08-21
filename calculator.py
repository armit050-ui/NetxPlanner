def compound_growth(paycheck, percent_invested, annual_rate, years, contributions_per_year=24):
    contribution = paycheck * percent_invested
    periodic_rate = annual_rate / contributions_per_year
    periods_per_year = contributions_per_year

    balance = 0
    yearly_balances = []

    for year in range(1, years + 1):
        for _ in range(periods_per_year):
            balance += contribution
            balance *= (1 + periodic_rate)
        yearly_balances.append(round(balance, 2))

    return yearly_balances


if __name__ == "__main__":
    paycheck = 1200
    percent_invested = 0.15
    years = 10

    for rate in [0.06, 0.07, 0.08]:
        balances = compound_growth(paycheck, percent_invested, rate, years)
        print(f"\nAt {int(rate*100)}% annual return:")
        for year, balance in enumerate(balances, start=1):
            print(f"  Year {year}: ${balance:,.2f}")