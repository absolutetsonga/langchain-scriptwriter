import os
from dotenv import load_dotenv

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

def init():
    st.title('🦜🔗 Youtube Title GPT Creator')
    topic = st.text_input('Plug in your Youtube Topic here')

    llm = OpenAI(temperature=0.9)

    title_template = PromptTemplate(
        input_variables=["topic"],
        template="Write me a youtube video title about {topic}"
    )

    script_template = PromptTemplate(
        input_variables=["title", "wikipedia_research"],
        template="Write me a youtube video script based on this title; TITLE: {title} "
                 "while leveraging title with wikipedia research: {wikipedia_research}"
    )

    title_memory = ConversationBufferMemory(input_key="topic", memory_key="chat_history")
    script_memory = ConversationBufferMemory(input_key="title", memory_key="chat_history")

    title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key="title", memory=title_memory)
    script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key="script", memory=script_memory)

    wiki = WikipediaAPIWrapper()

    if topic:
        title = title_chain.run(topic=topic)
        wiki_research = wiki.run(topic)
        script = script_chain.run(title=title, wikipedia_research=wiki_research)

        st.write(title)
        st.write(script)

        with st.expander('Message History'):
            st.info(title_memory.buffer)

        with st.expander('Script History'):
            st.info(script_memory.buffer)

        with st.expander('Wikipedia Research'):
            st.info(wiki_research)


def main():
    init()
    load_dotenv(os.getenv('OPEN_API_KEY'))


if __name__ == '__main__':
    main()
