# EduPath: Career Guidance Chatbot

EduPath is a Flask-based web application powered by OpenAI's GPT-3.5 Turbo model and LangChain. It provides career guidance by leveraging conversational AI and an interactive interface.

## Features

- Conversational AI for career guidance.
- Persistent and reusable vector storage for document retrieval.
- Speech-to-text translation for interactive input.
- Chat history logging with file download support.
- CSV-based search functionality for retrieving user data or specific records.
- Cross-platform compatibility for deployment on Windows, macOS, and Linux.

---
Screenshots
Below are some screenshots of the application in action:

SignIn/SignUP
![signin](https://github.com/user-attachments/assets/a3707d8d-098d-4285-bba6-f05822fdd870)

Chat Interface
![chatinterface](https://github.com/user-attachments/assets/111de290-7bd7-4946-9854-783ef4ce56a0)

Degree Timeline
![degreetimeline](https://github.com/user-attachments/assets/93e4b522-f97f-4fd2-91fe-a9bceaae9150)

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Pip (Python package manager)
- Virtual environment manager (optional but recommended)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/EduPath.git
   cd EduPath
   ```

2. **Set Up a Virtual Environment**
   (Optional but recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # On macOS/Linux
   venv\Scripts\activate         # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set OpenAI API Key**
   Replace `your_openai_api_key` with your actual API key:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"    # On macOS/Linux
   set OPENAI_API_KEY="your_openai_api_key"       # On Windows
   ```

5. **Prepare Data Files**
   - Add documents for retrieval in the `data/` directory.
   - Ensure `data.csv` and `user.csv` are populated with relevant records for CSV search functionality.

---

### Running the Application

1. **Start the Flask Application**
   ```bash
   python app.py
   ```

2. **Access the Web Interface**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:1805
   ```

---

## Cross-Platform Deployment

### Windows
- Run the application directly with Python.
- Consider creating a batch file for ease of execution.

### macOS/Linux
- Use the terminal to execute the Python script.
- Deploy with a process manager like `supervisord` or `systemd` for production use.

### Docker (Optional)
1. **Build Docker Image**
   ```bash
   docker build -t edupath:latest .
   ```

2. **Run the Container**
   ```bash
   docker run -p 1805:1805 edupath:latest
   ```

---

## Directory Structure

```
EduPath/
│
├── data/                      # Directory for documents used by LangChain
├── templates/                 # HTML templates for the Flask web interface
├── static/                    # Static files (CSS, JS, images)
├── chathistory/               # Folder for saving chat history
├── app.py                     # Main Flask application script
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## Known Issues and Future Improvements

1. **Speech Recognition**: Limited language support; improve by integrating additional models or libraries.
2. **Security**: API key is hardcoded for now—switch to environment variables or secret management tools.
3. **UI/UX**: Enhance the user interface for better usability and accessibility.

---

## License

This project is licensed under the MIT License.

---

## Contribution

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.
