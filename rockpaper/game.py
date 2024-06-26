import streamlit as st
import random

# Choices for the game
choices = ['Rock', 'Paper', 'Scissors']

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "You win!"
    else:
        return "You lose!"

# Initialize score tracking
if 'user_score' not in st.session_state:
    st.session_state['user_score'] = 0
if 'computer_score' not in st.session_state:
    st.session_state['computer_score'] = 0

# Streamlit app layout
st.title("Rock-Paper-Scissors Game")
st.write("Choose your move:")

# User input
user_choice = st.radio("", choices)

# Generate computer choice
computer_choice = random.choice(choices)

if st.button("Play"):
    result = determine_winner(user_choice, computer_choice)
    st.write(f"Your choice: {user_choice}")
    st.write(f"Computer's choice: {computer_choice}")
    st.write(result)

    # Update scores
    if result == "You win!":
        st.session_state['user_score'] += 1
    elif result == "You lose!":
        st.session_state['computer_score'] += 1

# Display scores
st.write(f"Your score: {st.session_state['user_score']}")
st.write(f"Computer's score: {st.session_state['computer_score']}")

# Play again option
if st.button("Play Again"):
    st.experimental_rerun()

# Reset scores option
if st.button("Reset Scores"):
    st.session_state['user_score'] = 0
    st.session_state['computer_score'] = 0
