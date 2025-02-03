# Ollama Streamlit Interface

A simple Streamlit interface for interacting with Ollama AI models.

## Prerequisites

1. Make sure you have Python installed on your Mac
2. Install Ollama by running this command in Terminal:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

## Setup Instructions

1. Open Terminal and clone this repository (or create a new directory with the files)

2. Create and activate a Python virtual environment:
   ```bash
   # Create a virtual environment
   python -m venv venv
   
   # Activate the virtual environment
   source venv/bin/activate
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Ollama service:
   ```bash
   ollama serve
   ```

5. Pull the DeepSeek model (in a new Terminal window):
   ```bash
   # Download and set up the DeepSeek model
   ollama pull deepseek-coder:1.3b
   
   # Create an alias for deepseek-r1:8b
   ollama cp deepseek-coder:1.3b deepseek-r1:8b
   ```

6. Run the Streamlit app (in a new Terminal window):
   ```bash
   # Make sure your virtual environment is activated
   source venv/bin/activate
   
   # Run the app
   streamlit run app.py
   ```

The application should automatically open in your default web browser. If it doesn't, you can access it at http://localhost:8501

## Usage

1. Enter your prompt in the text area
2. Click "Generate Response" to get the AI's response
3. The response will be displayed below the button

## Note

To deactivate the virtual environment when you're done:
```bash
deactivate
``` 