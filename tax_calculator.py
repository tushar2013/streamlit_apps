import streamlit as st

from utils.format_indian import format_indian

# Calculation starts.
st.markdown('# TAX CALCULATOR')

gross_salary = st.text_input('Enter Gross Salary')
if gross_salary:
    counter = 0
    tax = 0
    gross = int(gross_salary)
    slabs = {300000: 0, 700000: 0.05, 1000000: 0.1, 1200000: 0.15, 1500000: 0.2}
    #st.code(f'initial counter :: {counter}')
    #st.code(f'GROSS SALARY = INR {format_indian(gross)}')
    for slab in slabs:
        previous_counter = counter
        counter += slab
        if counter < gross:
            tax += slabs[slab] * slab
            #st.code(f'current slab :: {slab}')
            #st.code(f'tax at slab {slab} :: {tax}')
        elif counter > gross:
            tax += slabs[slab] * (gross - previous_counter)
            #st.code(f'last diff :: {gross - previous_counter}')
            #st.code(f'tax at last diff :: {tax}')
            break
    if counter < gross:
        st.code(f'CURRENT COUNTER = {counter}')
        tax += (gross - counter) * 0.3

    st.code(f'INCOME TAX = INR {format_indian(int(tax))}')
    st.code(f'IN-HAND ANNUAL SALARY = INR {format_indian(gross - int(tax))}')
    st.code(f'IN-HAND MONTHLY SALARY = INR {format_indian(int((gross - int(tax))/12))}')
