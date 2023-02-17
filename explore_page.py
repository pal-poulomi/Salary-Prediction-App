import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def required_categories(categories, cutoff):
    categorical_map = {}
    for i in range (len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Others'
    return categorical_map


def clean_yearsofexperience(exp):
    if exp == 'More than 50 years':
        return 50
    if exp == 'Less than 1 year':
        return 0.5
    return float(exp)


def clean_Edlevel(ed):
    
    if "Bachelor’s degree (B.A., B.S., B.Eng., etc.)" in ed:
        return "Bachelor's degree"
    if "Master’s degree (M.A., M.S., M.Eng., MBA, etc.)" in ed:
        return "Master's degree"
    if "Professional degree" in ed or "Other doctoral" in ed:
        return "Post grad"
    return "Less than a Bachelor degree"


@st.cache_resource
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    required_columns = ['Country', 'EdLevel', 'YearsCodePro', 'Employment', 'ConvertedComp']
    df = df[required_columns]
    df = df.rename({'ConvertedComp':'Salary'}, axis=1)

    df = df[df['Salary'].notnull()]
    df = df.dropna()
    df = df[df['Employment'] == 'Employed full-time']
    df = df.drop('Employment', axis=1)

    country_map = required_categories(df.Country.value_counts(), 400)
    df['Country'] = df['Country'].map(country_map)
    df = df[df['Salary'] <= 250000]
    df = df[df['Salary'] >= 10000]
    df = df[df['Country'] != 'Others']

    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_yearsofexperience)
    df['EdLevel'] = df['EdLevel'].apply(clean_Edlevel)

    return df


df = load_data()

def show_explore_page():

    st.title("Explore Software Developer Yearly Salaries")

    st.write("""### Stack Overflow Developer Survey 2020""")


    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")

    st.write("""### Distribution of data across different countries""")

    st.pyplot(fig1)


    st.write(
        """
        ### Mean Salary based on Country
        """
    )

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)


    st.write(
        """
        ### Mean Salary based on Experience
        """
    )

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)

    
