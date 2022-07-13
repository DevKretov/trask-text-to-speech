# streamlit_audio_recorder by stefanrmmr (rs. analytics) - version April 2022

import os
import streamlit as st
import streamlit.components.v1 as components

import speech_recognition as sr


# DESIGN implement changes to the standard streamlit UI/UX
st.set_page_config(page_title="Trask Text-to-Speech demo app")
# Design move app further up and remove top padding
st.markdown('''<style>.css-1egvi7u {margin-top: -3rem;}</style>''',
    unsafe_allow_html=True)
# Design change st.Audio to fixed height of 45 pixels
st.markdown('''<style>.stAudio {height: 45px;}</style>''',
    unsafe_allow_html=True)
# Design change hyperlink href link color
st.markdown('''<style>.css-v37k9u a {color: #ff4c4b;}</style>''',
    unsafe_allow_html=True)  # darkmode
st.markdown('''<style>.css-nlntq9 a {color: #ff4c4b;}</style>''',
    unsafe_allow_html=True)  # lightmode


def audiorec_demo_app():

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    # Custom REACT-based component for recording client audio in browser
    build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
    # specify directory and initialize st_audiorec object functionality
    st_audiorec = components.declare_component("st_audiorec", path=build_dir)

    # TITLE and Creator information
    st.title('Trask Speech-to-Text demo app')
    st.markdown('Made for a show-off of the audio file loading and text extraction')
    st.write('\n\n')

    # STREAMLIT AUDIO RECORDER Instance
    st_audiorec()

    data = st.file_uploader("Upload a wav file", type=["wav"])

    if data is not None:

        r = sr.Recognizer()

        audio_file = sr.AudioFile(data)
        with audio_file as source:
          audio = r.record(source)

        text = r.recognize_google(audio, language='cs-CZ')

        st.markdown(text)


if __name__ == '__main__':

    # call main function
    audiorec_demo_app()
