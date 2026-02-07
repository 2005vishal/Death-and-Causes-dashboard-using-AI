# 🏥 AI-Powered Deaths & Causes Dashboard

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gemini AI](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)

An interactive data analytics dashboard that visualizes mortality trends and uses **Google's Gemini AI** to generate instant insights, summaries, and explanations of the data.

## 🚀 Live Demo
**[Click here to view the deployed app](YOUR_STREAMLIT_APP_URL_HERE)**
*(Replace this link after you deploy on Streamlit Cloud)*

## 📊 Key Features
- **AI Analyst Integration:** Uses Google Gemini (Flash 2.0 & Pro) to analyze charts and data summaries on demand.
- **Smart Data Loading:** Automatically detects data from Kaggle, local storage, or allows manual CSV upload.
- **Interactive Visualizations:**
  - **Univariate Analysis:** Histograms and Bar charts for single-column distribution.
  - **Bivariate Analysis:** Compare relationships between two variables (Grouped Bar Charts).
  - **Multivariate Analysis:** Complex views with 3 variables (X-axis, Y-axis, Color Hue).
- **Robust API Handling:** Includes auto-retry logic and model rotation to handle API rate limits gracefully.

## 🛠️ Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io/)
- **Data Processing:** Pandas
- **Visualization:** Plotly Express
- **AI Model:** Google GenAI (`google-genai` library)

## ⚙️ Installation & Local Setup

Follow these steps to run the dashboard on your local machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
