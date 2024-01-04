import openai
import streamlit as st


# Function to get responses from GPT-3.5
def get_gpt3_response(user_input):
    openai.api_key = 'your-openai-api-key'  # Replace with your actual OpenAI API key

    prompt = f"Answer the following question about the Tudors based on Wikipedia information: {user_input}"

    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # Specify GPT-3.5 model
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"


# Streamlit app for the chatbot
def tudor_history_chatbot_app():
    st.title("Tudor History Chatbot")

    user_input = st.text_input("Ask me anything about the Tudors:")

    if user_input:
        response = get_gpt3_response(user_input)
        st.text_area("Response", response, height=150)


if __name__ == "__main__":
    tudor_history_chatbot_app()
