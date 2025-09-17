# app.py
import streamlit as st
from scenarios import SCENARIOS
import random
import pandas as pd
import os
import base64
from io import BytesIO
from urllib.parse import quote

# --- Constants ---
NUM_QUESTIONS = 5
LEADERBOARD_FILE = "leaderboard.csv"

# --- Page Setup ---
def setup_page():
    st.set_page_config(
        page_title="FinX Oracle",
        page_icon="🔮",
        layout="centered"
    )

# --- Helper Functions ---
def get_player_photo_html():
    """Generates the HTML for the circular player photo frame."""
    if st.session_state.uploaded_image is not None:
        image_bytes = BytesIO(st.session_state.uploaded_image.getvalue())
        encoded_image = base64.b64encode(image_bytes.read()).decode()
        image_element = f"<img src='data:image/png;base64,{encoded_image}' style='width: 100%; height: 100%; object-fit: cover;'>"
    else:
        image_element = "<p style='text-align: center; margin-top: 55px; font-size: 14px; color: #888;'>Upload Photo</p>"

    frame_html = f"""
        <div style='width: 150px; height: 150px; border-radius: 50%; border: 3px solid #FFFFFF; overflow: hidden; background-color: #333;'>
            {image_element}
        </div>
    """
    return frame_html

def display_share_options(player_name, final_score):
    """Displays the X (Twitter) sharing text and button."""
    st.subheader("Share Your Score")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**1. Copy this post text:**")
        post_text = (
            f"I scored {final_score}/{NUM_QUESTIONS} in the FinX Oracle challenge! 🔮\n\n"
            f"My knowledge of fintech, finance, and global markets was put to the test with scenarios from late 2025. How would you do?\n\n"
            f"#FinXOracle #Fintech #FinanceQuiz"
        )
        st.code(post_text, language='text')

    with col2:
        st.markdown("**2. Post on X (Twitter):**")
        encoded_text = quote(post_text)
        twitter_url = f"https://twitter.com/intent/tweet?text={encoded_text}"
        st.link_button("Post on X (Twitter)", twitter_url)

# --- Game State Management ---
def initialize_state():
    if "game_state" not in st.session_state:
        st.session_state.game_state = "name_input"
        st.session_state.player_name = ""
        st.session_state.team_name = ""
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.show_feedback = False
        st.session_state.uploaded_image = None # Added for photo frame
        
        fintech_questions = [q for q in SCENARIOS if q['category'] == 'fintech']
        general_finance_questions = [q for q in SCENARIOS if q['category'] == 'general_finance']
        gk_questions = [q for q in SCENARIOS if q['category'] == 'gk']

        selected_fintech = random.sample(fintech_questions, min(2, len(fintech_questions)))
        selected_general = random.sample(general_finance_questions, min(2, len(general_finance_questions)))
        selected_gk = random.sample(gk_questions, min(1, len(gk_questions)))

        scenarios_sample = selected_fintech + selected_general + selected_gk
        random.shuffle(scenarios_sample)
            
        for scenario in scenarios_sample:
            random.shuffle(scenario['choices']) 
            
        st.session_state.scenarios = scenarios_sample
        st.session_state.score_recorded = False

def start_game():
    if st.session_state.name_input and st.session_state.team_input:
        st.session_state.player_name = st.session_state.name_input
        st.session_state.team_name = st.session_state.team_input
        st.session_state.game_state = "in_game"
    else:
        st.warning("Please enter both your name and a team name to begin.")

def restart_game():
    st.session_state.clear()

# --- UI Display Functions ---
def display_name_input():
    st.title("Welcome to the FinX Oracle 🔮")
    st.markdown("Join a team, test your financial knowledge, and compete for the top spot.")
    st.markdown("**Each question has exactly two correct answers.**")
    st.text_input("Your Name", key="name_input")
    st.text_input("Team Name", key="team_input")
    st.button("Begin Challenge", on_click=start_game)

def display_question():
    if 'scenarios' not in st.session_state or not st.session_state.scenarios:
        st.error("There was an error loading questions. Please restart.")
        st.button("Restart Challenge", on_click=restart_game)
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
    
    options = [choice['text'] for choice in scenario['choices']]
    selected_choices = st.multiselect(
        "Select ALL correct answers (there are 2):", 
        options, 
        key=f"question_{current_index}",
        disabled=is_disabled
    )
    
    if not is_disabled and st.button("Submit Answer", key=f"submit_{current_index}"):
        st.session_state.show_feedback = True
        correct_answers = {choice['text'] for choice in scenario['choices'] if choice['correct']}
        user_answers = set(selected_choices)
        
        if user_answers == correct_answers:
            st.session_state.score += 1
        st.rerun()

    if st.session_state.show_feedback:
        correct_answers = {choice['text'] for choice in scenario['choices'] if choice['correct']}
        user_answers = set(selected_choices)
        
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
    if 'score' not in st.session_state or 'player_name' not in st.session_state:
        st.error("SESSION ERROR: Game state not found. Please start a new challenge.")
        st.button("Restart Challenge", on_click=restart_game)
        return

    st.balloons()
    final_score = st.session_state.score
    player_name = st.session_state.player_name
    team_name = st.session_state.team_name

    if not st.session_state.score_recorded:
        update_leaderboard(player_name, team_name, final_score)
        st.session_state.score_recorded = True

    st.title("Challenge Completed!")
    
    # --- Player Card with Photo Frame ---
    st.subheader("Player Card")
    col1, col2 = st.columns([1, 2])
    with col1:
        photo_frame = get_player_photo_html()
        st.markdown(photo_frame, unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload Your Photo", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
        if uploaded_file:
            st.session_state.uploaded_image = uploaded_file
            st.rerun()

    with col2:
        st.text_input("Player", value=player_name, disabled=True)
        st.text_input("Team", value=team_name, disabled=True)
        st.metric(label="Your Final Score", value=f"{final_score} / {NUM_QUESTIONS}")
    
    st.markdown("---")
    display_leaderboard(team_name)
    
    st.markdown("---")
    display_share_options(player_name, final_score)

    st.markdown("---")
    st.button("Play Again", on_click=restart_game)

# --- Leaderboard Logic ---
def update_leaderboard(player, team, score):
    new_entry = pd.DataFrame([{'Player': player, 'Team': team, 'Score': score}])
    required_columns = ['Player', 'Team', 'Score']

    if os.path.exists(LEADERBOARD_FILE):
        try:
            df = pd.read_csv(LEADERBOARD_FILE)
            if list(df.columns) != required_columns:
                raise ValueError("Incorrect column format")
            
            df = df[df['Player'] != player]
            df = pd.concat([df, new_entry], ignore_index=True)
            df.to_csv(LEADERBOARD_FILE, index=False)
        except (ValueError, pd.errors.EmptyDataError):
            new_entry.to_csv(LEADERBOARD_FILE, index=False)
    else:
        new_entry.to_csv(LEADERBOARD_FILE, index=False)

def display_leaderboard(current_team_name):
    if not os.path.exists(LEADERBOARD_FILE):
        st.subheader("Leaderboard")
        st.write("Be the first to set a score!")
        return

    try:
        df = pd.read_csv(LEADERBOARD_FILE)
        if df.empty:
            st.subheader("Leaderboard")
            st.write("Be the first to set a score!")
            return
    except (FileNotFoundError, pd.errors.EmptyDataError):
        st.subheader("Leaderboard")
        st.write("Be the first to set a score!")
        return

    st.subheader("🏆 Leaderboards")
    tab1, tab2 = st.tabs(["Team Rankings", f"Team '{current_team_name}' Players"])

    with tab1:
        st.markdown("##### Overall Team Standings (by Average Score)")
        team_scores = df.groupby('Team').agg(
            Average_Score=('Score', 'mean'),
            Players=('Player', 'count')
        ).round(2).sort_values(by="Average_Score", ascending=False).reset_index()
        st.dataframe(team_scores, use_container_width=True)

    with tab2:
        team_df = df[df['Team'] == current_team_name].sort_values(by="Score", ascending=False).reset_index(drop=True)
        st.dataframe(team_df, use_container_width=True)

# --- Main App ---
def main():
    setup_page()
    initialize_state()

    if st.session_state.game_state == "name_input":
        display_name_input()
    elif st.session_state.game_state == "in_game":
        display_question()
    elif st.session_state.game_state == "results":
        display_results()

if __name__ == "__main__":
    main()
