# Import necessary libraries
import time
from flask import logging, Flask, render_template, request, redirect, send_file, flash
import openai
import os
import sys
import csv
import speech_recognition as sr
from flask import send_from_directory

from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

text = "Hie"

name = 'EduPath'

# Define the role of the bot
role = 'Career Guidance'

# Define the impersonated role with instructions
impersonated_role = f"""
    From now on, you are going to act as {name}. Your role is {role}.
    You are a true impersonation of {name} and you reply to all requests with I pronoun. You never give unknown information.
    Forward them to the website for more information.
    YOU ARE NOT AN AI MODEL!
"""

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = False

query = None
if len(sys.argv) > 1:
    query = sys.argv[1]

if PERSIST and os.path.exists("persist"):
    print("Reusing index...\n")
    vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
    index = VectorStoreIndexWrapper(vectorstore=vectorstore)
else:
    # loader = TextLoader("data/data.txt") # Use this line if you only need data.txt
    loader = DirectoryLoader("data/")
    if PERSIST:
        index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
    else:
        index = VectorstoreIndexCreator().from_loaders([loader])

chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-3.5-turbo-0125"),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

chat_history = []
cwd = './chathistory'
i = 1

# Find an available chat history file
while os.path.exists(os.path.join(cwd, f'chat_history{i}.txt')):
    i += 1

history_file = os.path.join(cwd, f'chat_history{i}.txt')

# Create a new chat history file
with open(history_file, 'w') as f:
    f.write('\n')

# Create a Flask web application
app = Flask(__name__)

# Function to complete chat input using OpenAI's GPT-3.5 Turbo
def chatcompletion(user_input, chat_history, impersonated_role):
    result = chain({"question": user_input, "chat_history": chat_history, "role": impersonated_role})
    return result['answer']

# Function to handle user chat input
import datetime




    
def chat(user_input):
    global chat_history
    
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Write user input with timestamp to history file
    with open(history_file, 'a') as f:
        f.write(f"{timestamp} [User]: {user_input}\n")
    
    # Get bot response
    result = chatcompletion(user_input, chat_history, impersonated_role)
    
    # Append user input, bot response, and timestamp to chat history
    chat_history.append((user_input, result, timestamp))
    
    # Write bot response with timestamp to history file
    with open(history_file, 'a') as f:
        f.write(f"{timestamp} [Bot]: {result}\n")
    
    return result

# Python Program that helps translate Speech to Text import speech_recognition # The Recognizer is initialized. UserVoiceRecognizer = speech_recognition.Recognizer() while(1): try: with speech_recognition.Microphone() as UserVoiceInputSource: UserVoiceRecognizer.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.5) # The Program listens to the user voice input. UserVoiceInput = UserVoiceRecognizer.listen(UserVoiceInputSource) UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput) UserVoiceInput_converted_to_Text = UserVoiceInput_converted_to_Text.lower() print(UserVoiceInput_converted_to_Text) except KeyboardInterrupt: print('A KeyboardInterrupt encountered; Terminating the Program !!!') exit(0) except speech_recognition.UnknownValueError: print("No User Voice detected OR unintelligible noises detected OR the recognized audio cannot be matched to text !!!") 
@app.route('/download_chat_history/<int:file_number>', methods=['GET'])
def download_chat_history(file_number):
    # Get the current working directory
    cwd = os.getcwd()

    # Define the file path
    file_path = os.path.join(cwd, f'chat_history{file_number}.txt')

    # Check if the file exists
    if os.path.exists(file_path):
        # Send the file to the user for download
        return send_file(file_path, as_attachment=True)
    else:
        return 'Chat history file does not exist.'
    
# Define app routes
@app.route('/')
def index():
    

    return render_template("authenticate.html")

@app.route('/download/<filename>')
def download(filename):
    # Specify the directory path from where the files should be downloaded
    directory = './data'

    return send_from_directory(directory, filename)

@app.route('/index', methods=['GET', 'POST'])
def Page():
    directory = './data'

    # Get a list of files in the directory
    files = os.listdir(directory)
    
    def search_csv(identifier):
        with open('data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['identifier'] == identifier:
                    return row

        with open('user.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['identifier'] == identifier:
                    return row

        return None  
    record = None
    if request.method == 'POST':
        identifier = request.form['identifier']
        record = search_csv(identifier)
    return render_template('index.html', record=record,  files=files)

@app.route("/get")
# Function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    response = chat(userText)
    return response

@app.route('/refresh')
def refresh():
    time.sleep(600) # Wait for 10 minutes
    return redirect('/refresh')

@app.route('/audio', methods=['POST'])
def audio():
    r = sr.Recognizer()
    with open('upload/audio.wav', 'wb') as f:
        f.write(request.data)
  
    with sr.AudioFile('upload/audio.wav') as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='en-IN', show_all=False)
        print(text)
        return_text = text
        
    return render_template('index.html', return_text=return_text)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1805)