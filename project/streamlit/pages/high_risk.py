import streamlit as st
import requests,io
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components


st.set_page_config(layout='wide', initial_sidebar_state='expanded')

response = requests.post('http://127.0.0.1:5000/get_data')
data = response.json()

# Process and display the data
df = pd.read_json(io.StringIO(data["df"]))


def show_pie(respect_to,msg):
    fig = plt.subplot()
    grouped_data = df.groupby(respect_to)
    percentages = grouped_data.size().div(len(df)).mul(100)
    plt.pie(percentages, labels=percentages.index, autopct='%1.1f%%')
    plt.title(msg)
    st.pyplot(fig.figure)
    plt.close()

def high_risk():
    st.title("High risk")
    st.write("This is the high risk page")
    msg = 'The number of risks form the {respect_to} for the current month'

    with st.container():
        components.html(f'''
        <style>
            label {{
                color: rgb(115 120 141);
            }}
        
            input {{
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background: #f5f5f5;
            color: #666;
            font-size: 14px;
            cursor: not-allowed;
            }}
        </style>
        <form action="info" method="post">
        <fieldset>
            <label for="Name"> Sector name: </label>
            <input type="text" maxlength="12" {"value="+data["info"]["sector_name"] if data["info"]["sector_name"] else ''} disabled="disabled" />
            <label for="Name"> Business unit: </label>
            <input type="text" maxlength="12" {"value="+data["info"]["business_unit"] if data["info"]["business_unit"] else ''} disabled="disabled" />
            <label for="Name"> Project name: </label>
            <input type="text" maxlength="12" {"value="+data["info"]["project_name"] if data["info"]["project_name"] else ''} disabled="disabled" />
            <br />
            <label for="Name"> Contractore: </label>
            <input type="text" maxlength="12" {"value="+data["info"]["contractor"] if data["info"]["contractor"] else ''} disabled="disabled" />
            <label for="Name"> Project's cost: </label>
            <input type="text" maxlength="12" {"value="+data["info"]["project_cost"] if data["info"]["project_cost"] else ''} disabled="disabled" />
            <label for="Name"> Project duration: </label>
            <input type="text" maxlength="12" {"value="+data["info"]["project_duration"] if data["info"]["project_duration"] else ''} disabled="disabled" />
        </fieldset></form>''')

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            show_pie("Reasons",msg.format(respect_to="reasons"))

        with col2:
            show_pie('Deptartment responsible',msg.format(respect_to='deptartment responsible'))
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            show_pie("Source of risk",msg.format(respect_to='source of risk'))

        with col2:
            show_pie("Risk classification",msg.format(respect_to='risk classification'))

high_risk()