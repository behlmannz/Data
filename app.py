import streamlit as st

# Title of the app
st.title("Real Estate Deal Analyzer")

# Purchase Details Section
st.header("Purchase Details")
purchase_price = st.number_input("Purchase Price", value=675000)
rehab_costs = st.number_input("Rehab Costs", value=25000)
after_repaid_value = st.number_input("After Repaid Value", value=800000)
percent_down = st.number_input("% Down", value=25)
mortgage_rate = st.number_input("Mortgage Rate (%)", value=6.65)
loan_term_years = st.number_input("Loan Term (Years)", value=25)
loan_term_months = loan_term_years * 12  # This will be auto-calculated based on loan term in years
number_of_units = st.number_input("Number of Units", value=9)
rent_per_unit = st.number_input("Rent Per Unit", value=796)
rent_appreciation = st.number_input("Rent Appreciation (%)", value=3)
property_appreciation = st.number_input("Property Appreciation (%)", value=4)

# Annual Gross Income Section
st.header("Annual Gross Income")
rental_income = rent_per_unit * number_of_units * 12  # Annual rental income based on input
other_income = st.number_input("Other Income", value=5000)
vacancy_allowance_percent = st.number_input("Vacancy Allowance (%)", value=5)
vacancy_allowance = (rental_income + other_income) * (vacancy_allowance_percent / 100)

# Annual Expenses Section
st.header("Annual Expenses")
taxes = st.number_input("Taxes", value=6067)
insurance = st.number_input("Insurance", value=4333)
utilities = st.number_input("Utilities", value=4333)
management_fee = st.number_input("Management Fee", value=1733)
repairs_maintenance = st.number_input("Repairs & Maintenance", value=4333)
make_ready = st.number_input("Make Ready", value=2600)
cam = st.number_input("CAM", value=2600)
reserves = st.number_input("Reserves", value=1733)

# Calculations Section (Results)
st.header("Results")

# Purchase details
investment_down_payment = (percent_down / 100) * purchase_price
mortgage_amount = purchase_price - investment_down_payment
monthly_payment = (mortgage_amount * (mortgage_rate / 100 / 12)) / (1 - (1 + mortgage_rate / 100 / 12) ** (-loan_term_months))
gross_income = rental_income + other_income - vacancy_allowance
annual_expenses = taxes + insurance + utilities + management_fee + repairs_maintenance + make_ready + cam + reserves
net_operating_income = gross_income - annual_expenses
annual_debt_service = monthly_payment * 12

# Debt Service Coverage Ratio (DSCR)
dscr = net_operating_income / annual_debt_service

# Cash on Cash Return
cash_on_cash = (net_operating_income - annual_debt_service) / investment_down_payment * 100

# CAP Rate
cap_rate = net_operating_income / purchase_price * 100

# Projection Results for Year 3, 5, and 10
hold_time_years = [3, 5, 10]
projections = {}

for year in hold_time_years:
    appreciation = purchase_price * ((1 + property_appreciation / 100) ** year)
    rent_growth = rental_income * ((1 + rent_appreciation / 100) ** year)
    cash_flow = rent_growth - annual_expenses - annual_debt_service
    profit = appreciation + cash_flow
    projections[year] = {
        "Appreciation": appreciation,
        "Rental Income Growth": rent_growth,
        "Cash Flow": cash_flow,
        "Profit": profit
    }

# Display Results
st.subheader("Key Financials:")
st.write(f"Purchase Price: ${purchase_price:,.2f}")
st.write(f"Investment/Down Payment: ${investment_down_payment:,.2f}")
st.write(f"Mortgage Amount: ${mortgage_amount:,.2f}")
st.write(f"Monthly Mortgage Payment: ${monthly_payment:,.2f}")
st.write(f"Gross Income: ${gross_income:,.2f}")
st.write(f"Annual Expenses: ${annual_expenses:,.2f}")
st.write(f"Net Operating Income: ${net_operating_income:,.2f}")
st.write(f"Annual Debt Service: ${annual_debt_service:,.2f}")
st.write(f"Debt Service Coverage Ratio (DSCR): {dscr:.2f}")
st.write(f"Cash on Cash Return: {cash_on_cash:.2f}%")
st.write(f"CAP Rate: {cap_rate:.2f}%")

# Display Projections for 3, 5, and 10 years
st.subheader("Projections:")
for year in hold_time_years:
    st.write(f"**Year {year} Projections**")
    st.write(f"Appreciation: ${projections[year]['Appreciation']:,.2f}")
    st.write(f"Rental Income Growth: ${projections[year]['Rental Income Growth']:,.2f}")
    st.write(f"Cash Flow: ${projections[year]['Cash Flow']:,.2f}")
    st.write(f"Profit: ${projections[year]['Profit']:,.2f}")
    st.write("-----------")
