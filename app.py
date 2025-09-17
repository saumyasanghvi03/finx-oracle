import streamlit as st
from scenarios import SCENARIOS
import random
import base64
from PIL import Image
from io import BytesIO

# Number of questions per game
NUM_QUESTIONS = 5

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
        # Select 5 random scenarios from the total pool of 20
        st.session_state.scenarios = random.sample(SCENARIOS, NUM_QUESTIONS)
        st.session_state.show_feedback = False
        st.session_state.uploaded_image = None

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
    if current_index >= NUM_QUESTIONS:
        st.session_state.game_state = "results"
        st.rerun()
        return

    scenario_data = st.session_state.scenarios[current_index]

    st.header(f"Oracle's Challenge #{current_index + 1}/{NUM_QUESTIONS}: {scenario_data['title']}")
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
    user_name = st.session_state.user_name

    st.title("The Oracle Has Spoken! 🔮")
    st.markdown(f"### Congratulations, {user_name}!")
    st.markdown(f"You gained **{final_insights}** out of **{NUM_QUESTIONS}** Oracle's Insights.")
    
    if final_insights >= NUM_QUESTIONS - 1:
        st.success("Your strategic foresight is peerless. You are a true FinX Oracle!")
    else:
        st.warning("Your insights are valuable, but there's more to discover.")

    st.markdown("---")
    st.subheader("Your Score Frame")

    # Image uploader for the user's photo
    uploaded_file = st.file_uploader("Upload your photo for the frame", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        st.session_state.uploaded_image = uploaded_file
        # Convert the uploaded image to a base64 string for embedding in HTML
        uploaded_image_bytes = BytesIO(st.session_state.uploaded_image.getvalue())
        uploaded_image_b64 = base64.b64encode(uploaded_image_bytes.read()).decode('utf-8')
        image_src = f"data:image/jpeg;base64,{uploaded_image_b64}"
        # Use HTML to display the uploaded image with a circular crop
        image_html = f"""
            <div style='height: 150px; width: 150px; margin: 20px auto; border-radius: 50%; border: 3px solid #5C6AC4; overflow: hidden; display: flex; align-items: center; justify-content: center;'>
                <img src='{image_src}' style='width: 100%; height: 100%; object-fit: cover;'>
            </div>
        """
    else:
        # Placeholder HTML when no image is uploaded
        image_html = """
            <div style='height: 150px; width: 150px; margin: 20px auto; background-color: #D3D3D3; border-radius: 50%; border: 3px solid #5C6AC4;'>
                <p style='padding-top: 60px; font-size: 0.9em; color: #555; text-align: center;'>Add Your Photo Here</p>
            </div>
        """

    # Combine the dynamic image HTML with the static frame
    st.markdown(
        f"""
        <div style='text-align: center; padding: 20px; border: 4px solid #5C6AC4; border-radius: 15px; background-color: #F0F2F6; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
            <h2 style='color: #2D2D2D;'>FinX Oracle: Final Score</h2>
            {image_html}
            <h1 style='font-size: 3em; color: #5C6AC4;'>{final_insights}/{NUM_QUESTIONS}</h1>
            <p style='font-size: 1.2em; color: #555;'>- {user_name}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.info("Take a screenshot of the frame above to share on LinkedIn!")
    st.markdown("### Share on LinkedIn")
    st.markdown("1. Copy the text below.")
    st.markdown("2. Click the button to open LinkedIn.")
    st.markdown("3. Paste the text into your new post.")

    linkedin_post_text = (
        f"I just completed the FinX Oracle challenge at the FinX Institute new campus launch! My financial foresight was "
        f"tested on real-world scenarios in blockchain, AI, and derivatives. "
        f"I scored {final_insights}/{NUM_QUESTIONS} Oracle's Insights. \n\n"
        f"What do you think of my score? Let's connect on the future of FinTech. "
        f"#FinXInstitute #FinTech #FinXOracle #FinancialInnovation #CampusLaunch"
    )
    st.code(linkedin_post_text, language='text')

    st.link_button("Create My LinkedIn Post", "https://www.linkedin.com/feed/?shareActive=true")
    
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
