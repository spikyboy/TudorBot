import openai
import streamlit as st

# Function to get responses from GPT-3
def get_gpt3_response(prompt):
    try:
        openai.api_key = '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'  # Replace with your actual API key

        response = openai.Completion.create(
            engine="davinci",  # Use the most capable model
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return response.choices[0].text.strip()
    except Exception as e:
        return "An error occurred: " + str(e)

# Streamlit app
def tudor_history_chatbot_app():
    st.title("Tudor History Chatbot")

    user_input = st.text_input("Ask me anything about the Tudors:", key="user_input")

    if st.button("Send"):
        gpt3_prompt = f"Based on Wikipedia knowledge, {user_input}"
        response = get_gpt3_response(gpt3_prompt)
        st.text_area("Chatbot:", value=response, height=100, key="response")

if __name__ == "__main__":
    tudor_history_chatbot_app()
