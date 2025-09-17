import streamlit as st
from scenarios import SCENARIOS
import random

def setup_page():
    st.set_page_config(
        page_title="The FinX Oracle",
        page_icon="🔮",
        layout="centered"
    )

def initialize_game_state():
    if "game_state" not in st.session_state:
        st.session_state.game_state = "name_input"
        st.session_state.user_name = ""
        st.session_state.current_scenario = 0
        st.session_state.insights = 0
        # Randomize the scenarios for replayability
        st.session_state.scenarios = random.sample(SCENARIOS, len(SCENARIOS))
        st.session_state.show_feedback = False

def display_name_input():
    st.title("Welcome to The FinX Oracle 🔮")
    st.markdown("Enter your name to begin your journey and test your financial foresight!")
    
    user_name = st.text_input("Your Name", key="name_input")
    
    if st.button("Start Challenge", key="start_button"):
        if user_name:
            st.session_state.user_name = user_name
            st.session_state.game_state = "in_game"
            st.rerun()
        else:
            st.warning("Please enter your name to begin.")

def display_scenario():
    current_index = st.session_state.current_scenario
    if current_index >= len(st.session_state.scenarios):
        st.session_state.game_state = "results"
        st.rerun()
        return

    scenario_data = st.session_state.scenarios[current_index]

    st.header(f"Oracle's Challenge #{current_index + 1}: {scenario_data['title']}")
    st.markdown(f"**Scenario:** *{scenario_data['description']}*")
    st.markdown("---")

    selected_choice = st.radio("Your Decision:", [choice['text'] for choice in scenario_data['choices']], key=f"scenario_{current_index}")
    
    if st.button("Commit Decision", key=f"submit_{current_index}"):
        st.session_state.show_feedback = True
        for choice in scenario_data['choices']:
            if selected_choice == choice['text']:
                if choice['correct']:
                    st.session_state.insights += 1
                break
        st.rerun()

    if st.session_state.show_feedback:
        for choice in scenario_data['choices']:
            if selected_choice == choice['text']:
                if choice['correct']:
                    st.success(f"🔮 Insight Gained! {choice['feedback']}")
                else:
                    st.error(f"❌ Missed Insight. {choice['feedback']}")
                
                st.markdown(f"---")
                st.markdown(f"**Learn more:** Check out the project at: {scenario_data['project_link']}")
                st.button("Next Challenge", on_click=lambda: (st.session_state.update(current_scenario=current_index + 1, show_feedback=False)), key=f"next_{current_index}")
                break

def display_results():
    st.balloons()
    final_insights = st.session_state.insights
    total_scenarios = len(st.session_state.scenarios)
    user_name = st.session_state.user_name

    st.title("The Oracle Has Spoken! 🔮")
    st.markdown(f"### Congratulations, {user_name}!")
    st.markdown(f"You gained **{final_insights}** out of **{total_scenarios}** Oracle's Insights.")
    
    # Check for a high score to provide special message
    if final_insights >= total_scenarios - 2:
        st.success("Your strategic foresight is peerless. You are a true FinX Oracle!")
    else:
        st.warning("Your insights are valuable, but there's more to discover.")

    st.markdown("---")
    st.subheader("Your Score Frame")
    st.info("Take a screenshot of this frame and add your photo to share on social media!")

    # Use HTML and Markdown for the shareable frame
    shareable_text = f"I just scored {final_insights}/{total_scenarios} Oracle's Insights in the FinX Oracle challenge! My knowledge of #FinTech is 🔥 at the #FinXInstitute new campus launch! @FinXInstitute"
    shareable_link = f"https://twitter.com/intent/tweet?text={shareable_text}"

    st.markdown(
        f"""
        <div style='text-align: center; padding: 20px; border: 4px solid #5C6AC4; border-radius: 15px; background-color: #F0F2F6; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
            <h2 style='color: #2D2D2D;'>FinX Oracle: Final Score</h2>
            <div style='height: 150px; width: 150px; margin: 20px auto; background-color: #D3D3D3; border-radius: 50%; border: 3px solid #5C6AC4;'>
                <p style='padding-top: 60px; font-size: 0.9em; color: #555;'>Add Your Photo Here</p>
            </div>
            <h1 style='font-size: 3em; color: #5C6AC4;'>{final_insights}/{total_scenarios}</h1>
            <p style='font-size: 1.2em; color: #555;'>- {user_name}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(f"""
        <div style='text-align: center; margin-top: 20px;'>
            <a href="{shareable_link}" target="_blank">
                <button style='background-color: #1DA1F2; color: white; border: none; padding: 12px 24px; border-radius: 5px; font-size: 1.1em; cursor: pointer;'>
                    Share on Twitter
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    st.button("Restart Journey", on_click=lambda: (st.session_state.clear(), st.rerun()))

def main():
    setup_page()
    initialize_game_state()

    if st.session_state.game_state == "name_input":
        display_name_input()
    elif st.session_state.game_state == "in_game":
        st.header(f"The FinX Oracle: {st.session_state.user_name}")
        st.markdown("---")
        display_scenario()
    elif st.session_state.game_state == "results":
        display_results()

if __name__ == "__main__":
    main()
