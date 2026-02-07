import streamlit as st
import pandas as pd
import plotly.express as px
import time
import os
from dotenv import load_dotenv
from google import genai

# --- AI INTEGRATION SETUP ---
load_dotenv()

MY_API_KEY = os.getenv("MY_API_KEY")


try:
    client = genai.Client(api_key=MY_API_KEY)
except Exception as e:
    st.error(f"API Key Error: {e}")


def ask_ai(prompt):
    model_queue = [
        "gemini-2.0-flash-lite-001",  #  Lightweight/Fast
        "gemini-flash-latest",  #  Stable 1.5 Flash
        "gemini-pro"  #  Standard Pro
    ]

    for model_name in model_queue:
        try:

            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )
            return response.text

        except Exception as e:
            error_msg = str(e)


            if "429" in error_msg or "quota" in error_msg.lower() or "resource_exhausted" in error_msg.lower():
                continue


            if "404" in error_msg or "not found" in error_msg.lower():
                continue


            return f"⚠️ **AI Error ({model_name}):** {error_msg}"

    return "⚠️ **System Overload:** All AI models are currently busy. Please wait 1 minute."


st.set_page_config(page_title="Deaths & Causes AI Dashboard", layout="wide")
st.title("🏥 AI-Powered Deaths & Causes Analysis By Vishal Patwa")

# --- SMART DATA LOADING ---
@st.cache_data
def load_data():
    possible_paths = [
        "deaths_and_causes_synthetic.csv"
    ]

    for path in possible_paths:
        if os.path.exists(path):
            try:
                df = pd.read_csv(path)
                return df, path
            except:
                continue

    return None, None



df, loaded_path = load_data()

if df is not None:
    st.toast(f"✅ Loaded data from: {loaded_path}", icon="📂")
else:
    st.warning("⚠️ Data file not found on Server or Local path.")
    uploaded_file = st.sidebar.file_uploader("Upload your CSV manually", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        st.stop()
# --- DASHBOARD TABS ---
tab1, tab2, tab3, tab4 = st.tabs(
    ["📊 Data Overview", "📈 Univariate Analysis", "📉 Bivariate Analysis", "🔗 Multivariate Analysis"])


with tab1:
    st.header("Dataset Overview")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("First 5 Rows")
        st.dataframe(df.head())
    with col2:
        st.subheader("Last 5 Rows")
        st.dataframe(df.tail())

    st.subheader("Statistical Summary")
    st.dataframe(df.describe())


    if st.button("Generate AI Summary of Dataset", key="btn_overview"):
        with st.spinner("AI is analyzing the dataset..."):
            summary_prompt = f"Here is the statistical summary of a 'Deaths and Causes' dataset: {df.describe().to_string()}. Summarize the key data characteristics in 3 bullet points."
            st.session_state['overview_analysis'] = ask_ai(summary_prompt)

    if 'overview_analysis' in st.session_state:
        st.info(st.session_state['overview_analysis'])


# UNIVARIATE

with tab2:
    st.subheader("Single Column Analysis")

    cat_cols = list(df.select_dtypes(include="object").columns)
    num_cols = list(df.select_dtypes(include=["number"]).columns)

    analysis_type = st.radio("Select Analysis Type:", ["Categorical (Bar)", "Numerical (Histogram)"], horizontal=True)

    if analysis_type == "Categorical (Bar)":
        column = st.selectbox("Select Categorical Column:", cat_cols, key="uni_cat_col")

        if column:
            counts = df[column].value_counts().reset_index()
            counts.columns = [column, 'count']

            fig = px.bar(counts, x=column, y='count', title=f"Count of {column}", color=column)
            st.plotly_chart(fig, use_container_width=True)


            if st.button(f"Analyze {column}", key=f"btn_uni_{column}"):
                with st.spinner(f"Analyzing {column}..."):
                    prompt = f"Analyze this distribution for column '{column}': {counts.head().to_string()}. What are the most frequent categories?"
                    st.session_state[f'uni_analysis_{column}'] = ask_ai(prompt)

            if f'uni_analysis_{column}' in st.session_state:
                st.markdown(f"### 🤖 AI Insight:\n{st.session_state[f'uni_analysis_{column}']}")

    elif analysis_type == "Numerical (Histogram)":
        column = st.selectbox("Select Numerical Column:", num_cols, key="uni_num_col")

        if column:
            fig = px.histogram(df, x=column, nbins=30, title=f"Distribution of {column}", marginal="box",
                               template="plotly_white")
            st.plotly_chart(fig, use_container_width=True)


            if st.button(f"Analyze {column}", key=f"btn_uni_{column}"):
                with st.spinner(f"Analyzing {column}..."):
                    stats = df[column].describe().to_string()
                    prompt = f"Analyze this histogram for '{column}'. Here are the stats: {stats}. Is it skewed? What is the range?"
                    st.session_state[f'uni_analysis_{column}'] = ask_ai(prompt)

            if f'uni_analysis_{column}' in st.session_state:
                st.markdown(f"### 🤖 AI Insight:\n{st.session_state[f'uni_analysis_{column}']}")


# BIVARIATE (Two Columns)

with tab3:
    st.subheader("Compare Two Columns")

    col_x = st.selectbox("Select X-axis (Group):", df.columns, key="bi_x")
    col_y = st.selectbox("Select Y-axis (Value/Split):", df.columns, key="bi_y")

    if col_x != col_y:
        if df[col_y].dtype == 'object':
            counts = df.groupby([col_x, col_y]).size().reset_index(name='count')
            title = f"Distribution of {col_x} grouped by {col_y}"
            color_col = col_y
            plot_y = 'count'
        else:
            counts = df.groupby([col_x])[col_y].sum().reset_index(name='Sum_Value')
            title = f"Total {col_y} by {col_x}"
            color_col = None
            plot_y = 'Sum_Value'

        counts = counts.sort_values(by=plot_y, ascending=False)

        fig = px.bar(
            counts,
            x=col_x,
            y=plot_y,
            color=color_col,
            barmode='group',
            title=title,
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)


        btn_key = f"btn_bi_{col_x}_{col_y}"
        if st.button("Analyze Relationship", key=btn_key):
            with st.spinner("AI is studying the chart..."):
                prompt = f"Analyze this chart titled '{title}'. The top 5 data points are: {counts.head().to_string()}. What trends do you see?"
                st.session_state[f'bi_analysis_{col_x}_{col_y}'] = ask_ai(prompt)

        if f'bi_analysis_{col_x}_{col_y}' in st.session_state:
            st.success(st.session_state[f'bi_analysis_{col_x}_{col_y}'])

    else:
        st.warning("Please select two different columns.")


# MULTIVARIATE
with tab4:
    st.subheader("Advanced Multi-Column View")

    col_x = st.selectbox("X-axis Category:", df.columns, key="multi_x")
    col_hue = st.selectbox("Color Category (Hue):", df.columns, key="multi_hue")
    col_val = "Number_of_Deaths"

    if col_x != col_hue:
        if col_val in df.columns:
            grouped = df.groupby([col_x, col_hue])[col_val].sum().reset_index()
            grouped = grouped.sort_values(by=col_val, ascending=False)

            fig = px.bar(
                grouped,
                x=col_x,
                y=col_val,
                color=col_hue,
                barmode='group',
                title=f"{col_val} by {col_x} and {col_hue}"
            )
            st.plotly_chart(fig, use_container_width=True)


            btn_key = f"btn_multi_{col_x}_{col_hue}"
            if st.button("Analyze Multi-View", key=btn_key):
                with st.spinner("AI is crunching the numbers..."):
                    prompt = f"Analyze this multivariate chart. We are looking at {col_val} broken down by {col_x} and {col_hue}. Top data: {grouped.head().to_string()}. Summary?"
                    st.session_state[f'multi_analysis_{col_x}_{col_hue}'] = ask_ai(prompt)

            if f'multi_analysis_{col_x}_{col_hue}' in st.session_state:
                st.info(st.session_state[f'multi_analysis_{col_x}_{col_hue}'])

        else:
            st.error(f"Column '{col_val}' not found in dataset.")
    else:
        st.warning("X-axis and Color Category must be different.")