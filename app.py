import streamlit as st
from scenarios import SCENARIOS # Make sure you have a scenarios.py file
import random
import base64
from io import BytesIO
import pandas as pd
import os
from urllib.parse import quote

# --- Constants ---
NUM_SCENARIOS = 5
LEADERBOARD_FILE = "leaderboard.csv"

# --- Page Setup & Styling ---
def setup_page():
    """Sets up the Streamlit page configuration."""
    st.set_page_config(
        page_title="FinX Trading Simulator",
        page_icon="📈",
        layout="centered"
    )

def load_css():
    """Injects custom CSS for a dark, trader-focused theme."""
    css = """
    <style>
    /* Main app background */
    .stApp {
        background-color: #121212;
        color: #E0E0E0;
    }
    /* Main content area */
    .main .block-container {
        background-color: #1E1E1E;
        border-radius: 10px;
        padding: 2rem;
    }
    /* Buttons */
    .stButton>button {
        border: 2px solid #00BFFF;
        background-color: transparent;
        color: #00BFFF;
        border-radius: 5px;
    }
    .stButton>button:hover {
        border-color: #FFFFFF;
        background-color: #00BFFF;
        color: #FFFFFF;
    }
    /* Headers and Titles */
    h1, h2, h3 {
        color: #FFFFFF;
    }
    /* Success/Profitable Trade */
    .stAlert.st-alert.stSuccess {
        background-color: rgba(46, 139, 87, 0.3);
        border-left: 5px solid #2E8B57;
    }
    /* Error/Trade Loss */
    .stAlert.st-alert.stError {
        background-color: rgba(220, 20, 60, 0.3);
        border-left: 5px solid #DC143C;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


# --- Game State Management ---
def initialize_game_state():
    """Initializes the session state for a new trading day."""
    if "game_state" not in st.session_state:
        st.session_state.game_state = "login"
        st.session_state.trader_name = ""
        st.session_state.desk_name = ""
        st.session_state.current_scenario = 0
        st.session_state.alpha = 0
        st.session_state.scenarios = random.sample(SCENARIOS, NUM_SCENARIOS)
        st.session_state.show_feedback = False
        st.session_state.uploaded_image = None
        st.session_state.score_recorded = False

def start_session():
    """Starts the session after trader provides credentials."""
    if st.session_state.name_input and st.session_state.desk_name_input:
        st.session_state.trader_name = st.session_state.name_input
        st.session_state.desk_name = st.session_state.desk_name_input
        st.session_state.game_state = "in_game"
    else:
        st.warning("Please enter both Trader Name and Desk to begin.")

def new_trading_day():
    """Clears the session state to start a new day."""
    st.session_state.clear()
    st.rerun()

# --- UI Display Functions ---
def display_login():
    """Displays the initial screen for trader to enter credentials."""
    st.title("FinX Trading Simulator 📈")
    st.markdown("Enter your credentials to access the trading terminal.")
    
    st.text_input("Trader Name", key="name_input")
    st.text_input("Trading Desk (e.g., 'Alpha One')", key="desk_name_input")
    
    st.button("Access Terminal", on_click=start_session)

def display_scenario():
    """Displays the current market scenario and trading options."""
    current_index = st.session_state.current_scenario
    if current_index >= NUM_SCENARIOS:
        st.session_state.game_state = "results"
        st.rerun()
        return

    scenario_data = st.session_state.scenarios[current_index]

    st.header(f"Market Scenario #{current_index + 1}/{NUM_SCENARIOS}")
    st.subheader(scenario_data['title'])
    st.markdown(f"**Intel Briefing:** *{scenario_data['description']}*")
    st.markdown("---")

    is_disabled = st.session_state.show_feedback
    
    selected_choice = st.radio(
        "Your Strategy:", 
        [choice['text'] for choice in scenario_data['choices']], 
        key=f"scenario_{current_index}",
        disabled=is_disabled
    )
    
    if not is_disabled:
        if st.button("Execute Trade", key=f"submit_{current_index}"):
            st.session_state.show_feedback = True
            for choice in scenario_data['choices']:
                if selected_choice == choice['text'] and choice['correct']:
                    st.session_state.alpha += 1
            st.rerun()

    if st.session_state.show_feedback:
        user_choice_obj = next((c for c in scenario_data['choices'] if c['text'] == selected_choice), None)
        
        st.subheader("Post-Trade Analysis")
        col1, col2 = st.columns([1, 3])

        with col1:
            if user_choice_obj['correct']:
                st.metric(label="P&L", value="+1 Alpha", delta="Profitable")
            else:
                st.metric(label="P&L", value="0 Alpha", delta="Loss", delta_color="inverse")
        
        with col2:
            if user_choice_obj['correct']:
                st.success(f"✅ Trade executed successfully. {user_choice_obj['feedback']}")
            else:
                st.error(f"❌ Trade resulted in a loss. {user_choice_obj['feedback']}")

        st.markdown(f"**Further Reading:** {scenario_data['project_link']}")
        
        def next_scenario():
            st.session_state.current_scenario += 1
            st.session_state.show_feedback = False
        
        st.button("Next Scenario", on_click=next_scenario, key=f"next_{current_index}")


def display_results():
    """Displays the End of Day report with performance metrics."""
    st.balloons()
    final_alpha = st.session_state.alpha
    trader_name = st.session_state.trader_name
    desk_name = st.session_state.desk_name

    if not st.session_state.score_recorded:
        update_leaderboard(trader_name, desk_name, final_alpha)
        st.session_state.score_recorded = True

    st.title("End of Day Report 📝")
    st.markdown(f"### Performance Summary for **{trader_name}**")
    
    # --- Performance Metrics Dashboard ---
    win_rate = (final_alpha / NUM_SCENARIOS) * 100
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Total Alpha Generated", value=f"{final_alpha}", help="Each correct decision generates 1 Alpha.")
    with col2:
        st.metric(label="Win Rate", value=f"{win_rate:.1f}%", help="Percentage of profitable trades.")
    
    st.markdown("---")

    # --- Trader ID Card ---
    st.subheader("Trader ID")
    col1, col2 = st.columns([1, 2])
    with col1:
        uploaded_file = st.file_uploader("Upload Trader Photo", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
        if uploaded_file:
            st.session_state.uploaded_image = uploaded_file
        
        if st.session_state.uploaded_image:
            st.image(st.session_state.uploaded_image, width=150, caption="Trader Photo")
        else:
            st.markdown("_Upload a photo to display on your ID._")

    with col2:
        st.text_input("Trader", value=trader_name, disabled=True)
        st.text_input("Desk", value=desk_name, disabled=True)
        if final_alpha >= NUM_SCENARIOS - 1:
            st.success("Status: Top Performer")
        else:
            st.warning("Status: Performance Review Required")

    st.markdown("---")
    st.info("Share your performance report.")
    display_share_options(final_alpha)

    st.markdown("---")
    display_leaderboard(desk_name)

    st.button("New Trading Day", on_click=new_trading_day)


def display_share_options(final_alpha):
    """Displays sharing options for X (Twitter) / Threads."""
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**1. Copy Post Text:**")
        post_text = (
            f"Finished the day on the FinX Trading Simulator with {final_alpha} Alpha and a { (final_alpha / NUM_SCENARIOS) * 100 :.0f}% win rate. 📈\n\n"
            f"Challenging scenarios in AI, blockchain, and derivatives. Think you can do better?\n\n"
            f"#FinX #TradingSim #FinTech #Alpha"
        )
        st.code(post_text, language='text')

    with col2:
        st.markdown("**2. Post to Socials:**")
        encoded_text = quote(post_text)
        twitter_url = f"https://twitter.com/intent/tweet?text={encoded_text}"
        st.link_button("Post on X (Twitter)", twitter_url)
        st.markdown("Or, copy the text to post elsewhere.")

# --- Leaderboard Logic ---
def update_leaderboard(user, group, score):
    """Adds a new entry to the leaderboard CSV file."""
    new_entry = pd.DataFrame([{'Trader': user, 'Desk': group, 'Alpha': score}])
    try:
        if not os.path.exists(LEADERBOARD_FILE):
            new_entry.to_csv(LEADERBOARD_FILE, index=False)
        else:
            # Load existing, append, drop duplicates for the same trader, save
            df = pd.read_csv(LEADERBOARD_FILE)
            df = pd.concat([df, new_entry], ignore_index=True)
            df.drop_duplicates(subset=['Trader', 'Desk'], keep='last', inplace=True)
            df.to_csv(LEADERBOARD_FILE, index=False)
    except Exception as e:
        st.error(f"Could not save score: {e}")

def display_leaderboard(desk_name):
    """Reads the CSV and displays the P&L ranking for the specified desk."""
    if os.path.exists(LEADERBOARD_FILE):
        try:
            leaderboard_df = pd.read_csv(LEADERBOARD_FILE)
            # Rename columns for display
            leaderboard_df.rename(columns={'Trader': 'Trader', 'Desk': 'Desk', 'Alpha': 'Alpha'}, inplace=True)
            desk_leaderboard = leaderboard_df[leaderboard_df['Desk'] == desk_name].sort_values(
                by='Alpha', ascending=False
            ).reset_index(drop=True)
            
            st.subheader(f"P&L Ranking for '{desk_name}'")
            st.dataframe(desk_leaderboard, use_container_width=True)
        except Exception as e:
            st.error(f"Could not load leaderboard: {e}")
    else:
        st.markdown("No performance data recorded for this desk yet.")


# --- Main App Logic ---
def main():
    """Main function to run the Streamlit app."""
    setup_page()
    load_css()
    initialize_game_state()

    if st.session_state.game_state == "login":
        display_login()
    elif st.session_state.game_state == "in_game":
        display_scenario()
    elif st.session_state.game_state == "results":
        display_results()

if __name__ == "__main__":
    main()
