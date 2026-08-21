import streamlit as st
from calculator import compound_growth

st.title("Paycheck Compound Growth Calculator")

paycheck = st.slider("Paycheck amount ($)", min_value=200, max_value=10000, value=1200, step=50)
percent_invested = st.slider("Percent of each paycheck invested (%)", min_value=1, max_value=50, value=15) / 100
annual_rate = st.slider("Expected annual return (%)", min_value=1, max_value=15, value=7) / 100
years = st.slider("Number of years", min_value=1, max_value=40, value=10)

contribution_per_paycheck = paycheck * percent_invested
st.write(f"You're investing **${contribution_per_paycheck:,.2f}** per paycheck, twice a month.")

balances = compound_growth(paycheck, percent_invested, annual_rate, years)

st.subheader(f"Projected balance after {years} years: ${balances[-1]:,.2f}")

st.line_chart(balances)
