import random
import time
import streamlit as st


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Did you know? Bamboo is the fastest-growing plant in the world, growing up to 91 cm in a day!",
            "Fun fact: The smell of freshly cut grass is actually a plant distress call!",
            "Here's something cool: Some plants, like the Venus flytrap, are carnivorous and eat insects!",
            "Did you know? The Titan Arum, also known as the 'corpse flower,' is famous for its foul smell!",
            "Interesting fact: Trees can communicate with each other through underground fungal networks, often called the 'Wood Wide Web'!",
            "Did you know? Sunflowers can clean up toxic soil through a process called phytoremediation.",
            "Here's a fact: The world's smallest flowering plant is Wolffia, also known as watermeal.",
            "Fun fact: Bananas are technically berries, while strawberries are not!",
            "Did you know? Some plants, like the Resurrection plant, can survive years without water and revive when hydrated!",
            "Interesting fact: The Amazon rainforest produces 20% of the world's oxygen, earning it the name 'lungs of the Earth'.",
        ]
    )
    
    # Simulate typing by splitting into chunks (e.g., sentences) instead of words
    for sentence in response.split(". "):
        yield sentence + "."
        time.sleep(1)  # Delay for a more natural typing effect


st.title("Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = ""
        for sentence in response_generator():
            response += sentence + " "
            st.write(sentence, end="")  # Stream each sentence as it's generated
        st.session_state.messages.append({"role": "assistant", "content": response})
