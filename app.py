import streamlit as st
from ollama import Client

def create_example():
    # Initialize Ollama client
    ollama = Client()
    
    # Display the app
    st.title("Interface")
    
    # Create text input for the prompt
    user_input = st.text_area("Enter your prompt here", height=150)
    
    # Create a button to trigger the AI response
    if st.button("Generate Response"):
        # Use Ollama to generate a response
        response = ollama.chat(
            model="deepseek-r1:8b",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant"},
                {"role": "user", "content": user_input}
            ]
        )
        
        st.write("AI Response:")
        st.markdown(response['message']['content'])
    
    # Display the help message
    st.markdown("Click the button above to get an AI response to your input.")

# Run the Streamlit app
if __name__ == "__main__":
    create_example()