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
    if "current_scenario" not in st.session_state:
        st.session_state.current_scenario = 0
        st.session_state.insights = 0
        st.session_state.scenarios = random.sample(SCENARIOS, len(SCENARIOS))
        st.session_state.show_feedback = False

def display_scenario():
    current_index = st.session_state.current_scenario
    if current_index >= len(st.session_state.scenarios):
        show_results_page()
        return

    scenario_data = st.session_state.scenarios[current_index]

    st.header(f"Oracle's Challenge #{current_index + 1}: {scenario_data['title']}")
    st.markdown(f"**Scenario:** *{scenario_data['description']}*")
    st.markdown("---")

    selected_choice = st.radio("Your Decision:", [choice['text'] for choice in scenario_data['choices']], key=f"scenario_{current_index}")
    
    if st.button("Commit Decision", key=f"submit_{current_index}"):
        check_decision(selected_choice, scenario_data)
        st.session_state.show_feedback = True
        st.rerun() # Rerun to show feedback and hide button

    if st.session_state.show_feedback:
        for choice in scenario_data['choices']:
            if selected_choice == choice['text']:
                if choice['correct']:
                    st.success(f"🔮 Insight Gained! {choice['feedback']}")
                    st.session_state.insights += 1
                else:
                    st.error(f"❌ Missed Insight. {choice['feedback']}")
                
                st.markdown(f"---")
                st.markdown(f"**Learn more:** Check out the project at: {scenario_data['project_link']}")
                st.button("Next Challenge", on_click=lambda: (st.session_state.update(current_scenario=current_index + 1, show_feedback=False)), key=f"next_{current_index}")
                break

def check_decision(selected_text, scenario_data):
    for choice in scenario_data['choices']:
        if choice['text'] == selected_text:
            if choice['correct']:
                return "correct"
            else:
                return "incorrect"

def show_results_page():
    st.balloons()
    st.title("The Oracle has Spoken! 🔮")
    final_insights = st.session_state.insights
    total_scenarios = len(st.session_state.scenarios)

    st.markdown(f"### You Gained **{final_insights}** out of **{total_scenarios}** Oracle's Insights.")

    if final_insights >= total_scenarios - 1:
        st.success("Your strategic foresight is peerless. You are a true FinX Oracle!")
        st.markdown(" \nScan to claim your **Proof of Attendance Protocol**.")
    else:
        st.warning("Your insights are valuable, but there's more to discover in the FinTech frontier.")
        st.info("Visit the project demos to unlock more insights!")
    
    if st.button("Restart Journey"):
        st.session_state.clear()
        st.rerun()

def main():
    setup_page()
    initialize_game_state()
    st.title("The FinX Oracle 🔮")
    st.subheader("Your guide to navigating the future of finance.")
    st.markdown("---")
    display_scenario()
    st.markdown(f"**Insights Gained:** {st.session_state.insights}")

if __name__ == "__main__":
    main()
