def restart_game():
    """Clears the session state to restart the game."""
    st.session_state.clear()

def display_results():
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

    if st.session_state.uploaded_image is not None:
        uploaded_image_bytes = BytesIO(st.session_state.uploaded_image.getvalue())
        uploaded_image_b64 = base64.b64encode(uploaded_image_bytes.read()).decode('utf-8')
        image_src = f"data:image/jpeg;base64,{uploaded_image_b64}"
        image_html = f"""
            <div style='height: 150px; width: 150px; margin: 20px auto; border-radius: 50%; border: 3px solid #5C6AC4; overflow: hidden; display: flex; align-items: center; justify-content: center;'>
                <img src='{image_src}' style='width: 100%; height: 100%; object-fit: cover;'>
            </div>
        """
    else:
        image_html = """
            <div style='height: 150px; width: 150px; margin: 20px auto; background-color: #D3D3D3; border-radius: 50%; border: 3px solid #5C6AC4;'>
                <p style='padding-top: 60px; font-size: 0.9em; color: #555; text-align: center;'>Add Your Photo Here</p>
            </div>
        """

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
    
    st.info("To share your result on LinkedIn, follow these two steps:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**1. Copy this post text:**")
        linkedin_post_text = (
            f"I just completed the FinX Oracle challenge at the FinX Institute new campus launch! My financial foresight was "
            f"tested on real-world scenarios in blockchain, AI, and derivatives. "
            f"I scored {final_insights}/{NUM_QUESTIONS} Oracle's Insights. \n\n"
            f"What do you think of my score? Let's connect on the future of FinTech. "
            f"#FinXInstitute #FinTech #FinXOracle #FinancialInnovation #CampusLaunch"
        )
        st.code(linkedin_post_text, language='text')

    with col2:
        st.markdown("**2. Click here & paste the text:**")
        st.link_button("Create My LinkedIn Post", "https://www.linkedin.com/feed/?shareActive=true")

    st.markdown("---")
    display_leaderboard(group_name)

    # *** CHANGED LINE ***
    st.button("Restart Journey", on_click=restart_game)
