import streamlit as st
from scenarios import SCENARIOS # Make sure you have a scenarios.py file
import random
import base64
from io import BytesIO
import pandas as pd
import os
from urllib.parse import quote # IMPORT THIS LINE

# --- Constants ---
NUM_QUESTIONS = 5
LEADERBOARD_FILE = "leaderboard.csv"

# --- Page Setup ---
def setup_page():
    """Sets up the Streamlit page configuration."""
    st.set_page_config(
        page_title="The FinX Oracle",
        page_icon="🔮",
        layout="centered"
    )

# --- Game State Management ---
def initialize_game_state():
    """Initializes the session state for a new game if it doesn't exist."""
    if "game_state" not in st.session_state:
        st.session_state.game_state = "name_input"
        st.session_state.user_name = ""
        st.session_state.group_name = ""
        st.session_state.current_scenario = 0
        st.session_state.insights = 0
        st.session_state.scenarios = random.sample(SCENARIOS, NUM_QUESTIONS)
        st.session_state.show_feedback = False
        st.session_state.uploaded_image = None
        st.session_state.score_recorded = False

def start_game():
    """Starts the game after user provides name and group."""
    if st.session_state.name_input and st.session_state.group_name_input:
        st.session_state.user_name = st.session_state.name_input
        st.session_state.group_name = st.session_state.group_name_input
        st.session_state.game_state = "in_game"
    else:
        st.warning("Please enter both your name and a group name to begin.")

def restart_game():
    """Clears the session state to restart the game."""
    st.session_state.clear()
    st.rerun()

# --- UI Display Functions ---
def display_name_input():
    """Displays the initial screen for user to enter their name and group."""
    st.title("Welcome to The FinX Oracle 🔮")
    st.markdown("Enter your name and a group name to begin your journey and compete with friends!")
    
    st.text_input("Your Name", key="name_input")
    st.text_input("Group Name (e.g., 'Team Apollo')", key="group_name_input")
    
    st.button("Start Challenge", on_click=start_game)

def display_scenario():
    """Displays the current scenario, choices, and handles user input."""
    current_index = st.session_state.current_scenario
    if current_index >= NUM_QUESTIONS:
        st.session_state.game_state = "results"
        st.rerun()
        return

    scenario_data = st.session_state.scenarios[current_index]

    st.header(f"Oracle's Challenge #{current_index + 1}/{NUM_QUESTIONS}: {scenario_data['title']}")
    st.markdown(f"**Scenario:** *{scenario_data['description']}*")
    st.markdown("---")

    is_disabled = st.session_state.show_feedback
    
    selected_choice = st.radio(
        "Your Decision:", 
        [choice['text'] for choice in scenario_data['choices']], 
        key=f"scenario_{current_index}",
        disabled=is_disabled
    )
    
    if not is_disabled:
        if st.button("Commit Decision", key=f"submit_{current_index}"):
            st.session_state.show_feedback = True
            for choice in scenario_data['choices']:
                if selected_choice == choice['text'] and choice['correct']:
                    st.session_state.insights += 1
            st.rerun()

    if st.session_state.show_feedback:
        user_choice_obj = next((c for c in scenario_data['choices'] if c['text'] == selected_choice), None)
        if user_choice_obj:
            if user_choice_obj['correct']:
                st.success(f"🔮 Insight Gained! {user_choice_obj['feedback']}")
            else:
                st.error(f"❌ Missed Insight. {user_choice_obj['feedback']}")
        
        st.markdown("---")
        st.markdown(f"**Learn more:** Check out the project at: {scenario_data['project_link']}")
        
        def next_question():
            st.session_state.current_scenario += 1
            st.session_state.show_feedback = False
        
        st.button("Next Question", on_click=next_question, key=f"next_{current_index}")

def display_results():
    """Displays the final results, score frame, leaderboard, and share options."""
    st.balloons()
    final_insights = st.session_state.insights
    user_name = st.session_state.user_name
    group_name = st.session_state.group_name

    if not st.session_state.score_recorded:
        update_leaderboard(user_name, group_name, final_insights)
        st.session_state.score_recorded = True

    st.title("The Oracle Has Spoken! 🔮")
    st.markdown(f"### Congratulations, {user_name}!")
    st.markdown(f"You gained **{final_insights}** out of **{NUM_QUESTIONS}** Oracle's Insights.")
    
    if final_insights >= NUM_QUESTIONS - 1:
        st.success("Your strategic foresight is peerless. You are a true FinX Oracle!")
    else:
        st.warning("Your insights are valuable, but there's more to discover.")

    st.markdown("---")
    st.subheader("Your Score Frame")

    uploaded_file = st.file_uploader("Upload your photo for the frame", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        st.session_state.uploaded_image = uploaded_file

    image_html = get_image_frame_html()
    st.markdown(image_html, unsafe_allow_html=True)
    
    st.info("Share your result on social media!")
    display_share_options(final_insights, user_name) # THIS FUNCTION IS NOW UPDATED

    st.markdown("---")
    display_leaderboard(group_name)

    st.button("Restart Journey", on_click=restart_game)

def get_image_frame_html():
    """Generates the HTML for the user's score frame with their photo."""
    if st.session_state.uploaded_image is not None:
        uploaded_image_bytes = BytesIO(st.session_state.uploaded_image.getvalue())
        uploaded_image_b64 = base64.b64encode(uploaded_image_bytes.read()).decode('utf-8')
        image_src = f"data:image/jpeg;base64,{uploaded_image_b64}"
        image_element = f"<img src='{image_src}' style='width: 100%; height: 100%; object-fit: cover;'>"
    else:
        image_element = "<p style='padding-top: 60px; font-size: 0.9em; color: #555; text-align: center;'>Add Your Photo</p>"

    return f"""
        <div style='text-align: center; padding: 20px; border: 4px solid #5C6AC4; border-radius: 15px; background-color: #F0F2F6; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
            <h2 style='color: #2D2D2D;'>FinX Oracle: Final Score</h2>
            <div style='height: 150px; width: 150px; margin: 20px auto; border-radius: 50%; border: 3px solid #5C6AC4; overflow: hidden; display: flex; align-items: center; justify-content: center; background-color: #D3D3D3;'>
                {image_element}
            </div>
            <h1 style='font-size: 3em; color: #5C6AC4;'>{st.session_state.insights}/{NUM_QUESTIONS}</h1>
            <p style='font-size: 1.2em; color: #555;'>- {st.session_state.user_name}</p>
        </div>
    """

def display_share_options(final_insights, user_name):
    """Displays the X (Twitter) / Threads sharing text and button."""
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**1. Copy this post text:**")
        # Shorter text suitable for Twitter and Threads
        post_text = (
            f"I just scored {final_insights}/{NUM_QUESTIONS} on the FinX Oracle challenge! 🔮\n\n"
            f"Testing my knowledge on real-world scenarios in blockchain, AI, and derivatives. How would you score?\n\n"
            f"#FinXInstitute #FinTech #FinXOracle #AI"
        )
        st.code(post_text, language='text')

    with col2:
        st.markdown("**2. Click here to post:**")
        # URL-encode the text for the Twitter share link
        encoded_text = quote(post_text)
        twitter_url = f"https://twitter.com/intent/tweet?text={encoded_text}"
        
        st.link_button("Post on X (Twitter)", twitter_url)
        st.markdown("Or, copy the text and post on **Threads**!")

# --- Leaderboard Logic ---
def update_leaderboard(user, group, score):
    """Adds a new entry to the leaderboard CSV file."""
    new_entry = pd.DataFrame([{'User': user, 'Group': group, 'Score': score}])
    try:
        if not os.path.exists(LEADERBOARD_FILE):
            new_entry.to_csv(LEADERBOARD_FILE, index=False)
        else:
            new_entry.to_csv(LEADERBOARD_FILE, mode='a', header=False, index=False)
    except Exception as e:
        st.error(f"Could not save score: {e}")
        
def display_leaderboard(group_name):
    """Reads the CSV and displays the leaderboard for the specified group."""
    if os.path.exists(LEADERBOARD_FILE):
        try:
            leaderboard_df = pd.read_csv(LEADERBOARD_FILE)
            group_leaderboard = leaderboard_df[leaderboard_df['Group'] == group_name].sort_values(
                by='Score', ascending=False
            ).reset_index(drop=True)
            
            st.markdown(f"### Leaderboard for '{group_name}'")
            st.dataframe(group_leaderboard, hide_index=True)
        except Exception as e:
            st.error(f"Could not load leaderboard: {e}")
    else:
        st.markdown("No scores yet for this group. Be the first to play!")

# --- Main App Logic ---
def main():
    """Main function to run the Streamlit app."""
    setup_page()
    initialize_game_state()

    if st.session_state.game_state == "name_input":
        display_name_input()
    elif st.session_state.game_state == "in_game":
        display_scenario()
    elif st.session_state.game_state == "results":
        display_results()

if __name__ == "__main__":
    main()
