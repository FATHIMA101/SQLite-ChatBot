# SQLite-ChatBot
This is a **Flask-based Chat Assistant** that allows users to query an SQLite database using natural language. The assistant processes user queries, converts them into SQL statements, executes them on the database, and returns the results.

## 🚀 Live Demo
You can access the live demo of the chatbot here:  
🔗 https://sqlite-chatbot-1-ehgf.onrender.com  

⚠️ **Note**: This app is hosted on Render's free tier, so if it's inactive, it may take **50+ seconds** to start. Please be patient! 🚀  


## 🚀 How It Works
1. The assistant receives a natural language query from the user.
2. It processes the query and dynamically generates an SQL statement.
3. The generated SQL query is executed on the SQLite database.
4. The results are retrieved and returned to the user in a structured format.

## 🛠️ Running the Project Locally
Follow these steps to set up and run the project on your local machine:

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/FATHIMA101/SQLite-ChatBot.git
cd SQLite-ChatBot
```

### 2️⃣ **Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run the Flask Application**
```bash
python app.py
```
The app will start running on **http://127.0.0.1:5000/**.

### 5️⃣ **Test the API Using cURL or Postman**
To test the chat assistant, send a POST request to `/query` with a JSON payload:
```bash
curl -X POST http://127.0.0.1:5000/query \
     -H "Content-Type: application/json" \
     -d '{"query": "How many employees are in the Sales department?"}'
```

### 6️⃣ **Access the UI**
The application serves a frontend UI at **http://127.0.0.1:5000/**.

## ⚠️ Known Limitations & Suggestions for Improvement

- **Render Deployment Performance**: The app is deployed on Render, which may slow down processing times. It would perform better on **dedicated hosting solutions like AWS, Google Cloud, or DigitalOcean**.
- **Limited Query Understanding**: Currently, the assistant is rule-based and may not handle all types of user queries accurately.
- **Transformer Model Integration**: To improve query processing, **NLP models like BERT or OpenAI's GPT** could be integrated for better understanding and conversion to SQL.
- **Support for More Databases**: Right now, it works only with **SQLite**. Future improvements could support **PostgreSQL, MySQL, or MongoDB**.

## 📌 Future Enhancements
- Implementing **machine learning-based query interpretation**.
- Expanding support for **complex SQL queries**.
- Enhancing the UI for a better user experience.

---

💡 **Contributions are welcome!** If you have ideas for improvements, feel free to fork the repository and submit a pull request. 😊


