# 🏥 AI-Powered Deaths & Causes Dashboard

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gemini AI](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)

An interactive data analytics dashboard that visualizes mortality trends and uses **Google's Gemini AI** to generate instant insights, summaries, and explanations of the data.

## 🚀 Live Demo
**[[Click here to view the deployed app](https://death-and-causes-dashboard-using-ai-fknvnxcqsyxjlnipwppgup.streamlit.app/)**


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

```

### 2. Install Dependencies

Make sure you have Python installed. Then run:

```bash
pip install -r requirements.txt

```

### 3. Set up the API Key

This project requires a Google Gemini API Key.

1. Get your key from [Google AI Studio](https://aistudio.google.com/).
2. Create a file named `.env` in the root folder.
3. Add your key inside:

```properties
GOOGLE_API_KEY="your_actual_api_key_here"

```

*(Note: If deploying to Streamlit Cloud, add this key to the "Secrets" settings instead of a .env file.)*

### 4. Run the App

```bash
streamlit run main.py

```

## 📂 Project Structure

```text
├── main.py                     # The main Streamlit application code
├── requirements.txt            # List of Python dependencies
├── deaths_and_causes_synthetic.csv  # The dataset (bundled for deployment)
├── README.md                   # Project documentation
└── .gitignore                  # Files to exclude from GitHub

```

## 🛡️ Security Note

This project uses **Streamlit Secrets** management to keep the API key safe. The key is never hardcoded in the script. When deploying, ensure the key is added to the hosting platform's environment variables or secrets manager.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

```

### 📝 What to do next:
1.  **Create the file:** In your project folder (`D:\death&Causes`), create a text file named `README.md`.
2.  **Paste:** Paste the code above into it.
3.  **Update the Link:** Once you deploy your app on Streamlit Cloud, come back and replace `YOUR_STREAMLIT_APP_URL_HERE` with the actual link so people can click it!
4.  **Push:** Run `git add .`, `git commit -m "Add README"`, and `git push` to send it to GitHub.

```
