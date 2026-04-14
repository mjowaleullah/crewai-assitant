import os
import streamlit as st
from dotenv import load_dotenv
from crewai import Crew, LLM, Task, Agent, Process

load_dotenv()

st.title("Hello! I'm Assistant of Mj", anchor=False)
st.divider()

content = st.chat_input("What about you Know...")

if content:
    with st.spinner("Resserching Your Content..."):

        llm = LLM(
            base_url=os.getenv("OPENAI_API_BASE"),
            model=os.getenv("OPENAI_MODEL_NAME"),
            api_key=os.getenv("OPENROUTER_API_KEY")
        )


        researcher = Agent(
            role="Senior Researcher",
            goal = "Find the leatetest and best Information",
            backstory= "You are a Expert Researcher.",
            llm = llm,
            verbose = True
        )


        writer = Agent(
            role="Senior writer",
            goal = "Write the leatetest and best Information",
            backstory= "You are a Expert writer.",
            llm = llm,
            verbose = True
        )

        task1 = Task(
            description= f"Research about '{content}' and find the best information.",
            expected_output= "Write 3-5 point.",
            agent=researcher
        )

        task2 = Task(
            description= f"Write detailed report based on the research.",
            expected_output= "Write report in Markdown format",
            agent=writer
        )


        crew = Crew(
            tasks=[task1, task2],
            agents=[researcher, writer],
            process= Process.sequential,
            verbose=True
        )

        result = crew.kickoff()
        st.success("Done")
        st.markdown(result.raw)
