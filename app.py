# app.py
import streamlit as st
from scenarios import SCENARIOS
import random
import pandas as pd
import os

# --- Constants ---
NUM_QUESTIONS = 5
LEADERBOARD_FILE = "leaderboard.csv"

# --- Page Setup ---
def setup_page():
    st.set_page_config(
        page_title="Finance & Fintech Quiz",
        page_icon="💡",
        layout="centered"
    )

# --- Game State Management ---
def initialize_state():
    if "game_state" not in st.session_state:
        st.session_state.game_state = "name_input"
        st.session_state.user_name = ""
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.show_feedback = False
        
        # --- Ratio-Based Randomization Logic ---
        fintech_questions = [q for q in SCENARIOS if q['category'] == 'fintech']
        general_finance_questions = [q for q in SCENARIOS if q['category'] == 'general_finance']

        selected_fintech = random.sample(fintech_questions, min(3, len(fintech_questions)))
        selected_general = random.sample(general_finance_questions, min(2, len(general_finance_questions)))

        scenarios_sample = selected_fintech + selected_general
        random.shuffle(scenarios_sample)
            
        for scenario in scenarios_sample:
            random.shuffle(scenario['choices']) 
            
        st.session_state.scenarios = scenarios_sample
        st.session_state.score_recorded = False

def start_quiz():
    if st.session_state.name_input:
        st.session_state.user_name = st.session_state.name_input
        st.session_state.game_state = "in_quiz"
    else:
        st.warning("Please enter your name to begin.")

def restart_quiz():
    st.session_state.clear()
    st.rerun()

# --- UI Display Functions ---
def display_name_input():
    st.title("Welcome to the Finance & Fintech Quiz! 💡")
    st.markdown("Test your knowledge. **Note: Each question has exactly two correct answers.**")
    st.text_input("Enter Your Name", key="name_input")
    st.button("Start Quiz", on_click=start_quiz)

def display_question():
    if 'scenarios' not in st.session_state or not st.session_state.scenarios:
        st.error("There was an error loading the questions. Please restart the quiz.")
        st.button("Restart Quiz", on_click=restart_quiz)
        return

    current_index = st.session_state.current_question
    if current_index >= len(st.session_state.scenarios):
        st.session_state.game_state = "results"
        st.rerun()
        return

    scenario = st.session_state.scenarios[current_index]
    st.header(f"Question #{current_index + 1}/{NUM_QUESTIONS}")
    st.subheader(scenario['title'])
    st.markdown(f"*{scenario['description']}*")
    st.markdown("---")

    is_disabled = st.session_state.show_feedback
    
    # --- UPDATED: Using st.multiselect instead of st.radio ---
    options = [choice['text'] for choice in scenario['choices']]
    selected_choices = st.multiselect(
        "Select ALL correct answers (there are 2):", 
        options, 
        key=f"question_{current_index}",
        disabled=is_disabled
    )
    
    if not is_disabled and st.button("Submit Answer", key=f"submit_{current_index}"):
        st.session_state.show_feedback = True
        
        # --- UPDATED: Scoring logic for multiple correct answers ---
        correct_answers = {choice['text'] for choice in scenario['choices'] if choice['correct']}
        user_answers = set(selected_choices)
        
        if user_answers == correct_answers:
            st.session_state.score += 1
        st.rerun()

    if st.session_state.show_feedback:
        correct_answers = {choice['text'] for choice in scenario['choices'] if choice['correct']}
        user_answers = set(selected_choices)
        
        # --- UPDATED: Feedback logic for multiple correct answers ---
        if user_answers == correct_answers:
            st.success("✅ Correct! You found both right answers.")
            for choice in scenario['choices']:
                if choice['correct']:
                    st.write(f"✔️ {choice['feedback']}")
        else:
            st.error("❌ Incorrect. The two correct answers were:")
            for choice in scenario['choices']:
                if choice['correct']:
                    st.warning(f"**{choice['text']}**: {choice['feedback']}")
        
        st.info(scenario['references'])
        
        def next_question():
            st.session_state.current_question += 1
            st.session_state.show_feedback = False
        
        st.button("Next Question", on_click=next_question)

def display_results():
    st.balloons()
    final_score = st.session_state.score
    user_name = st.session_state.user_name

    if not st.session_state.score_recorded:
        update_leaderboard(user_name, final_score)
        st.session_state.score_recorded = True

    st.title("Quiz Completed!")
    st.markdown(f"### Congratulations, {user_name}!")
    st.metric(label="Your Final Score", value=f"{final_score} / {NUM_QUESTIONS}")
    
    st.markdown("---")
    display_leaderboard()
    st.button("Play Again", on_click=restart_quiz)

# --- Leaderboard Logic ---
def update_leaderboard(user, score):
    new_entry = pd.DataFrame([{'Name': user, 'Score': score}])
    if not os.path.exists(LEADERBOARD_FILE):
        new_entry.to_csv(LEADERBOARD_FILE, index=False)
    else:
        df = pd.read_csv(LEADERBOARD_FILE)
        df = df[df['Name'] != user]
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv(LEADERBOARD_FILE, index=False)

def display_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        st.subheader("Leaderboard")
        df = pd.read_csv(LEADERBOARD_FILE).sort_values(by="Score", ascending=False).reset_index(drop=True)
        st.dataframe(df, use_container_width=True)

# --- Main App ---
def main():
    setup_page()
    initialize_state()

    if st.session_state.game_state == "name_input":
        display_name_input()
    elif st.session_state.game_state == "in_quiz":
        display_question()
    elif st.session_state.game_state == "results":
        display_results()

if __name__ == "__main__":
    main()
