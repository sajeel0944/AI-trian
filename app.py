import streamlit as st
import google.generativeai as genai
import time


st.set_page_config(page_title="AI Assistant for Sir Zain")
st.title("AI Assistant for Sir Zain")

# is ky andar user or AI ky chat save ho rahy hai
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


value = st.chat_input("Enter your question:") # user input


if value:
    # chat_history ky andar user ka question jaraha hai
    st.session_state.chat_history.append({"role": "user", "message": value}) 


if value:
    try:

        with st.spinner("Generating response... Please wait"): # jab tak AI ka response nhi aye 
            API_KEY_TOKEN = st.secrets["API_KEY"]
            genai.configure(api_key=API_KEY_TOKEN) 
            model = genai.GenerativeModel("gemini-1.5-pro")

            # Custom Training Prompt
            prompt = f"""
            You are an AI that only answers about Sir Zain. Do not answer anything else.

            User: Who is Sir Zain?
            AI: Sir Zain is a professional teacher based in Karachi, Pakistan. He has been teaching for 12 years and is known for his expertise in education.

            User: Where does Sir Zain live?
            AI: Sir Zain lives in Buffer Zone, Sector 15A1 polt R,28, Karachi, Pakistan. Here is his location:  

            user: sir zain google map location?
            AI: https://www.google.com/maps/place/Sir+Zain's+Student+Circle+(SZSC)/@24.9529676,67.0588524,16z/data=!4m6!3m5!1s0x3eb3419715c9ae89:0xd6213e8a0a8a2228!8m2!3d24.9529638!4d67.0638917!16s%2Fg%2F11v9bwnff5?authuser=0&entry=ttu&g_ep=EgoyMDI1MDMwNC4wIKXMDSoASAFQAw%3D%3D
                
            User: What is Sir Zain's age?
            AI: Sir Zain is between 30 to 37 years old.

            User: Who lives with Sir Zain?
            AI: Sir Zain lives with his wife, daughter, mother, father, and brother.

            User: How many students does Sir Zain have?
            AI: Sir Zain teaches between 150 to 200 students.

            User: What is Sir zain full name?
            AI: zain.

            User: Where does Sir Zain teach?
            AI: Sir Zain teaches at LTD.

            User: What is Sir Zain's height?
            AI: Sir Zain's height is approximately 5'4", but it is not confirmed.

            User: What is Sir Zain's daily teaching schedule?
            AI: Sir Zain starts teaching at 1 PM and finishes at 8:30 PM.

            User: Does Sir Zain get angry quickly?
            AI: Yes, Sir Zain gets angry very quickly.

            user: what is sir zain university?
            AI : Studies at Allama Iqbal Open University
                 Started in 2017

            
            User: {value}
            AI:
            """

            response = model.generate_content(prompt)

        
        # ✅ Extracting AI Response Correctly
        if response and response.candidates:
            ai_answer = response.candidates[0].content.parts[0].text  # Ai ka response object main araha hai us ko fetch karrahy hai
            st.session_state.chat_history.append({"role": "AI", "message": ai_answer})     # chat_history ky andar AI ka response jaraha hai
        else:
            st.session_state.chat_history.append( {"role": "AI", "message": "⚠️ AI did not return a valid response."})

    except Exception as e:
            st.session_state.chat_history.append( {"role": "AI", "message": f"5 minute wait them try"})




for chat in st.session_state.chat_history :
    if chat["role"] == "user": # is ky anadr user ka question araha hai
        st.markdown(
            f"<div style='text-align: left;  color: black; background: rgb(233, 230, 230); "
            "border-radius: 20px; padding: 10px;  margin-bottom: 20px; width: 55%; margin-left: auto;'>"
            f"{chat['message']}</div>", unsafe_allow_html=True
        )

    else: # is ky andar AI ka response araha hai
        time.sleep(1)
        st.write(f"**AI:** {chat['message']}")






