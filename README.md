# 📊 Gradio CSV Question Answering & Visualization with Pydantic AI

This is a **Gradio-based application** that allows users to:
✅ Upload a CSV file 📂  
✅ Ask structured questions about the data using **LLaMA 3.1** 🤖  
✅ Get AI-generated responses powered by **Pydantic AI**  
✅ Plot graphs based on selected columns 📈  

---

## **🚀 Features**
- 🏢 **Built using Gradio for an interactive UI**
- 📊 **Supports line, bar, and scatter plots**
- ⚡ **Uses Pydantic AI Agent for structured query processing**
- 🔥 **Runs LLaMA 3.1 locally via Ollama**
- ✅ **Works with any structured CSV dataset**

---

## **🛠 Installation & Setup**
### **1️⃣ Clone the Repository**
```
git clone https://github.com/<your-username>/gradio-csv-qa.git
cd gradio-csv-qa
```

### **2️⃣ Set Up a Virtual Environment**
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```
pip install -r requirements.txt
```

### **4️⃣ Install Ollama and Pull LLaMA 3.1**
```
curl -fsSL https://ollama.com/install.sh | sh  # macOS/Linux
winget install Ollama.Ollama  # Windows

# Pull the LLaMA model
ollama pull llama3:8b
```

### **5️⃣ Run the Application**
```
python app.py
```

---

## **💡 How to Use**
### **1️⃣ Upload a CSV File**
Click on the "Upload CSV File" button and select a dataset.



### **2️⃣ Ask a Question**
Type a question related to the dataset, such as:
> "What is the average price in this dataset?"



### **3️⃣ Choose Graph Options**
Select **X-axis & Y-axis columns** and pick a **plot type** (line, bar, or scatter).



### **4️⃣ Get AI-Generated Answer & Plot**
The app will:
- ✅ Use LLaMA 3.1 to answer your question.
- ✅ Generate a visualization based on selected columns.


Below is the screenshot of the generated answer
![Screenshot (1595)](https://github.com/user-attachments/assets/4d6b26cc-af98-4d64-aa2e-c776275bacfe)

---

## **🔧 Project Structure**
```
gradio-csv-qa/
│── app.py              # Main Gradio app
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
│── screenshots/        # Folder for UI screenshots
│── .venv/              # Virtual environment (not committed)
```

---

## **📌 API & Technologies Used**
- **👉 Gradio** → UI for uploading files & interaction  
- **👉 Pandas** → CSV file handling  
- **👉 Matplotlib** → Graph plotting  
- **👉 Ollama** → Running LLaMA 3.1 for local AI processing  
- **👉 Pydantic AI** → Structured AI response processing  

---


