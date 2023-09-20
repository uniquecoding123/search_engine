#import required modules

import time
import pyttsx3
import streamlit as st
import wikipedia
try:
    # Streamlit < 0.65
    from streamlit.ReportThread import get_report_ctx

except ModuleNotFoundError:
    try:
        # Streamlit > 0.65
        from streamlit.report_thread import get_report_ctx

    except ModuleNotFoundError:
        try:
            # Streamlit > ~1.3
            from streamlit.script_run_context import get_script_run_ctx as get_report_ctx

        except ModuleNotFoundError:
            try:
                # Streamlit > ~1.8
                from streamlit.scriptrunner.script_run_context import get_script_run_ctx as get_report_ctx

            except ModuleNotFoundError:
                # Streamlit > ~1.12
                from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx as get_report_ctx



engine = pyttsx3.init()

st.title("Ask Anything")
query=st.text_area("Enter the content you want")
query=query.capitalize()

num=st.slider("Enter the number of sentences",min_value=2,max_value=15,step=1)

if st.button("Search"):
    with st.spinner("Please wait.."):
        time.sleep(2)

    try:
        result=wikipedia.summary(query, sentences=num)

        st.header("you searched for...")
        lines=result.split(".")
        for i in lines:
            time.sleep(2)
            st.subheader(i)

    except:
        st.subheader("please enter text correctly")

num1=st.slider("Enter the number of sentences do you want to speak",min_value=2,max_value=15,step=1)
if st.button("Speak"):
    engine.say(wikipedia.summary(query, sentences=num1))
    engine.runAndWait()
    #