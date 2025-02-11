import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import plotly.express as px
import requests
import streamlit.components.v1 as components
import io

st.set_page_config(page_title="General", page_icon="📊",layout='wide', initial_sidebar_state='expanded')

response = requests.post('http://127.0.0.1:5000/get_data')
data = response.json()

# Process and display the data
df = pd.read_json(io.StringIO(data["df"]))

def general():
    st.markdown("# General needs")
    st.write("Welcome to the general needs plans")
    
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
    
    # Source of risk
    with st.container():
        st.subheader("Source of risk")
        col1, col2 = st.columns(2)
        with col1:
            fig = plt.subplot()

            Source = (
                df["Source of risk"].value_counts().sort_values(ascending=False).head(5).index.values
            )
            sn.boxplot(
                y="Source of risk",
                x="No.",
                data=df[df["Source of risk"].isin(Source)],
                orient="h",
            )
            st.pyplot(fig.figure)
            plt.close()

        with col2:
            fig = plt.subplot()
            sn.countplot(x="Source of risk", data=df)
            st.pyplot(fig.figure)
            plt.close()
            

    # Risk type
    with st.container():
        st.subheader("Risk type")
        col1, col2= st.columns(2)
        count = df['Risk type '].value_counts()

        with col1:

            colors = {"Opportunity": 'green', "Threat": 'red'}
            slice_colors = [colors.get(value, 'gray') for value in count.index]

            fig = plt.subplot()

            plt.pie(count.values, labels=count.index, colors=slice_colors, autopct = '%1.1f%%')

            # Add a title and legend
            plt.title('Risk type ')
            plt.legend()
            st.pyplot(fig.figure)
            plt.close()

        with col2:
            fig = px.pie(values = count,
            labels = count,
            opacity = 0.75)
            st.plotly_chart(fig)
        
        
    with st.container():
        col1,col2 = st.columns(2)
        
        with col1:
            risk_type = df['Risk type '].astype(str)
            # Create a stem plot
            fig, ax = plt.subplots()
            ax.stem(risk_type, risk_type, linefmt='C0-', markerfmt='C0o', basefmt='k-')

            # Add labels and title
            ax.set_xlabel('Risk Type')
            ax.set_ylabel('Value')
            ax.set_title('Stem Plot')
            st.pyplot(fig)
        
        with col2:
            count = df['Risk type '].value_counts()
            d= pd.DataFrame(count)
            fig = px.pie(d,values=count,names=['Opportunity','Threat'],hole=0.4,opacity=0.6,labels={'label':'Risk type ','Potability':'No. Of Samples'})
            st.plotly_chart(fig)

            
    # Risk classification
    with st.container():
        st.subheader("Risk classification")
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots()
            sn.histplot(df["Risk classification"], bins=50,ax=ax)
            ax.set_title("Risk classification")
            st.pyplot(fig)
        
    # Deptartment responsible of danger
    with st.container():
        st.subheader("Deptartment responsible of danger")
        col1,col2 = st.columns(2)
        with col1:
            fig = plt.figure()
            plt.title("Deptartment responsible of danger")
            sn.barplot(x=df.index, y=df['Deptartment responsible'])
            plt.ylabel("Department")
            st.pyplot(fig)
        
        with col2:
            fig, ax = plt.subplots()
            sn.histplot(df['Deptartment responsible'],kde = True,ax=ax)
            st.pyplot(fig)

general()