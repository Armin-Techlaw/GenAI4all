import streamlit as st

Start_here = st.Page("Allpages/Intro/Start_here.py", title="Start here", icon="🤟", default=True)
Lesson_1 = st.Page("Allpages/Intro/Lesson_1.py", title="Lesson 1", icon="🤟", default=True)


pg = st.navigation(
    {
        "Home":[Start_here],
        "Step 1": [Lesson_1],
    }
)

pg.run()