import streamlit as st
import requests, io
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

response = requests.post('http://127.0.0.1:5000/get_data')
data = response.json()

# Process and display the data
df = pd.read_json(io.StringIO(data["df"]))


def pie_chart_2(f):
    fig = plt.subplot()
    data = df.groupby(f)['Risk type '].apply(lambda x: (x == 'Opportunity').sum()).reset_index(name='Number of Opportunity')
    plt.pie(data['Number of Opportunity'], labels=data[f], autopct='%1.1f%%')
    plt.title(f'Number of Opportunity by {f.lower()}')
    st.pyplot(fig.figure)
    plt.close()


def opportunities():
    st.title("Opportunities")
    st.write("This is the opportunities page")

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
            pie_chart_2("Risk classification")
        
        with col2:
            pie_chart_2("Source of risk")
            
    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            pie_chart_2("Deptartment responsible")
        

opportunities()