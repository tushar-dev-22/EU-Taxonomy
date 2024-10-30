from datetime import datetime
from pathlib import Path
import streamlit as st
from dateutil.relativedelta import relativedelta
from openpyxl import load_workbook
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
from io import StringIO
import plotly.express as px
import plotly.graph_objects as go
from datetime import timedelta
import os
# Page configuration
st.set_page_config(
    page_title="EU Taxonomy",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

file_path = 'Project Damietta_CashFlow Model_01b.xlsx'

os.chmod(file_path, 0o666)

@st.cache_data
def load_financial_model(file_path,sheet_name,header):
    file_extension = Path(file_path).suffix.lower()[1:]

    if file_extension == 'xlsx':
        return pd.read_excel(file_path, sheet_name=sheet_name, header=header, engine='openpyxl')

    elif file_extension == 'xls':
        st.write('its a xls file')
        return pd.read_excel(file_path, sheet_name=sheet_name, header=header)
    elif file_extension == 'csv':
        return pd.read_csv(file_path)
    else:
        raise Exception("File not supported")
    


# Define a common background color
bg_color = "#000C66"  # Adjust this color as needed
check_phase1 = False
check_phase2 = False
# CSS style for larger font size
if 'field1' not in st.session_state:
    st.session_state.field1 = ""
if 'field2' not in st.session_state:
    st.session_state.field2 = ""
if 'field3' not in st.session_state:
    st.session_state.field3 = ""
if 'field4' not in st.session_state:
    st.session_state.field4 = ""
if 'field5' not in st.session_state:
    st.session_state.field5 = ""
if 'field9' not in st.session_state:
    st.session_state.field9 = ""
if 'field11' not in st.session_state:
    st.session_state.field11 = ""
if 'field16' not in st.session_state:
    st.session_state.field16 = 0.0
if 'field19' not in st.session_state:
    st.session_state.field19 = 0.0
if 'field27' not in st.session_state:
    st.session_state.field27 = 0.0
if 'field32' not in st.session_state:
    st.session_state.field32 = 0.0
if 'field34' not in st.session_state:
    st.session_state.field34 = 0.0
if 'field37' not in st.session_state:
    st.session_state.field37 = 0.0
if 'field39' not in st.session_state:
    st.session_state.field39 = 0.0
if 'field44' not in st.session_state:
    st.session_state.field44 = 0.0
if 'field47' not in st.session_state:
    st.session_state.field47 = 0.0
if 'field60' not in st.session_state:
    st.session_state.field60 = 0.0

if 'osdp1' not in st.session_state:
        st.session_state.osdp1 = 0.0

if 'field17' not in st.session_state:
        st.session_state.field17 = 0.0

if 'osdp2' not in st.session_state:
    st.session_state.osdp2 = None

st.markdown(
    """
    <style>
    .big-font-section {
        font-size: 18px !important;
        text-align: center;
    }
    .big-font {
        font-size: 18px !important;
    }
    .center-text {
        text-align: center;
        margin: 0 auto;
        width: 70%; /* Adjust the width as needed */
    }
    .info-button {
        margin-left: 10px;
        background-color: #007BFF;
        border: none;
        color: white;
        padding: 5px 10px;
        border-radius: 50%;
        cursor: pointer;
        display: inline-block;
        width: 30px; /* Adjust the width and height to ensure the button is circular */
        height: 30px; /* Adjust the width and height to ensure the button is circular */
        text-align: center;
        line-height: 20px; /* Align the text vertically in the center */
        float: right;
    }
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: pointer;
        margin-left: 10px;
    }
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 220px;
        background-color: #555;
        color: #fff;
        text-align: center;
        border-radius: 5px;
        padding: 5px 10px;
        position: absolute;
        z-index: 1;
        bottom: 150%; /* Adjust this value to move the tooltip */
        left: 50%;
        margin-left: -110px;
        opacity: 0;
        transition: opacity 0.3s;
        font-size: 15px !important;
    }
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    .bold-hr {
        border: 0;
        height: 5px; /* Adjust height to make it more bold */
        background: #000; /* Change color if needed */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
if 'show_eligibility' not in st.session_state:
        st.session_state.show_eligibility = False

if 'page' not in st.session_state:
    st.session_state.page = 'main'

def continue_to_phase():
    st.session_state.page = 'phase'

def continue_to_phase2():
    st.session_state.page = 'phase2'

def continue_to_risk_management():
    st.session_state.page = 'risk-management'

def continue_to_dashboard():
    st.session_state.page = 'dashboard'
    
# def go_back_to_main_page():
#     st.session_state.page = 'main'
    # st.session_state.show_eligibility = False
# Sidebar for input fields and logos
if st.session_state.page == 'main':
    with st.sidebar:
        # Logos at the top of the sidebar
        col1, col2 = st.columns((1, 1))
        with col1:
            st.image("egypt.jpg", width=100)
        with col2:
            st.image("eu.jpg", width=100)
        
        st.markdown("# User Details")
        # field1 = ""
        # field2 = ""
        # field3 = ""
        # field4 = ""
        # field5 = ""
        st.session_state.field1 = st.text_input("Username", key='1', placeholder="Enter username")
        st.session_state.field2 = st.text_input("Project", key='2', placeholder="Enter project name")
        st.session_state.field3 = st.text_input("Capacity", key='3', placeholder="Enter capacity in m3/d")
        st.session_state.field4 = st.text_input("Location", key='4', placeholder="Enter location")
        st.session_state.field5 = st.date_input("Date", key='5')

        if st.button('Next') and st.session_state.field1 != "" and st.session_state.field2 != "" and st.session_state.field3 != "" and st.session_state.field4 != "" and st.session_state.field5 != "":
            st.session_state['show_eligibility'] = True

    # Main content
    with st.container():
        col1, col2 = st.columns((1, 5))
        with col1:
            st.image("CL3.png",width=180)
        with col2:
            st.markdown(
                f'<br><br><div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 100%; text-align: center; font-size: 36px; margin-top: -50px;" class="center-text">'
                '<strong>EU-WATER-FIT (Water Assessment and EU Taxonomy Evaluation for Resilient Financing and Investment Tool)</strong>'
                '</div>', unsafe_allow_html=True)

    # Adding some space below the logos
    st.markdown("<br>", unsafe_allow_html=True)

    # Eligibility section (displayed only if Next button is clicked and all fields are filled)
    if st.session_state.get('show_eligibility', False):
        col1, col2 = st.columns((1, 5))
        options1 = ['Click here to select option', 'E36.00', 'F42.9']

        # Eligibility
        with col1:
            st.markdown(
                f'<div style="background-color: #3f3f3f; color: white; padding: 15px; border-radius: 100px; margin-bottom: 15px; width: 100%;" class="big-font-section">'
                '<strong>ELIGIBILITY</strong>'
                '<button class="info-button tooltip" id="info-btn">i'
                '<span class="tooltiptext">Confirm if the Economic Activity matches a suitable Macro Economic Sector as stipulated in the Delegated Acts or Technical Screening Criteria based on Nomenclature of Economic Activities(NACE) code</span>'
                '</div>', unsafe_allow_html=True)
        with col2:
            st.markdown(
                f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                '<strong>Provide the NACE (Nomenclature of Economic Activities) Code for Desalination</strong>'
                '<button class="info-button tooltip" id="info-btn">i'
                '<span class="tooltiptext">Desalination is not assigned a NACE code; however, desalination can be substituted by two other activity codes</span>'
                '</button>'
                '</div>', unsafe_allow_html=True)
            answer1 = st.selectbox('Select your response', options1, label_visibility='collapsed', key='answer1')

            answer2 = ""
            answer3 = ""
            answer4 = 0
            answer5 = 0
            answer6 = 0
            answer7 = 0
            answer8 = 0
            answer9 = []
            answer10 = ""
            answer11 = ""
            answer12 = ""
            if answer1 == 'E36.00':
                st.markdown(
                    f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                    '<strong>Is the desalination activity associated with construction, extension and operation of water collection, treatment and supply systems?</strong>'
                    '<button class="info-button tooltip" id="info-btn">i'
                    '<span class="tooltiptext">Desalination is not assigned a NACE code; however, desalination can be substituted by two other activity codes</span>'
                    '</button>'
                    '</div>', unsafe_allow_html=True)
                answer2 = st.radio('Yes or No?', options=['Yes', 'No'], label_visibility='collapsed')
            elif answer1 == 'Click here to select option':
                st.write("")
            else:
                st.markdown(
                    f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                    '<strong>NACE Code F42.9 is not eligible to continue.</strong>'
                    '</div>', unsafe_allow_html=True)

            if answer1 == "E36.00":
                st.markdown(
                    f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                    '<strong>Is the desalination activity associated with renewal of water collection, treatment and supply systems?</strong>'
                    '<button class="info-button tooltip" id="info-btn">i'
                    '<span class="tooltiptext">Desalination is not assigned a NACE code; however, desalination can be substituted by two other activity codes</span>'
                    '</button>'
                    '</div>', unsafe_allow_html=True)
                answer3 = st.radio('Yes or No?2', options=['Yes', 'No'], label_visibility='collapsed')
            if answer2 == "No" and answer3 == "No":
                st.markdown(
                    f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;text-align: center;" class="big-font">'
                    '<strong>The envisioned Activity is Not EU Taxonomy Eligible</strong>'
                    '</div>', unsafe_allow_html=True)
        col3, col4 = st.columns((1, 5))
        with col4:
            if (answer2 == "Yes" or answer3 == "Yes") and answer1 == "E36.00":
                st.markdown(
                    f'<div style="background-color: #00FF00; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                    '<strong>The envisioned Activity is EU Taxonomy Eligible</strong>'
                    '</div>', unsafe_allow_html=True)
        if answer2 == "Yes" or answer3 == "Yes":
            st.markdown("<hr class='bold-hr'>", unsafe_allow_html=True)
        col1, col2 = st.columns((1, 5))
        if answer2 == "Yes" or answer3 == "Yes":
            with col1:
                st.markdown(
                    f'<br><div style="background-color: #3f3f3f; color: white; padding: 15px; border-radius: 100px; margin-bottom: 15px; width: 100%;" class="big-font-section">'
                    '<strong>ALIGNMENT</strong>'
                    '<button class="info-button tooltip" id="info-btn">i'
                    '<span class="tooltiptext">Confirm if the Economic Activity provides a "Substantial Contribution" to one environmental objective and will "Do No Significant Harm" (DNSH)  to the remaining five environmental objectives, as designated per sector</span>'
                    '</div>', unsafe_allow_html=True)
            if answer2 == "Yes":
                # Alignment
                with col2:
                    st.markdown(
                        f'<br><div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                        '<strong>What is the net average energy consumption for abstraction and treatment for produced water supply (in kWh/m3)?</strong>'
                        '<button class="info-button tooltip" id="info-btn">i'
                        '<span class="tooltiptext">Should be less than or equal to 0.5</span>'
                        '</div>', unsafe_allow_html=True)
                    answer4 = st.number_input('Enter your response (kWh/m3)', min_value=0.0, step=0.01,label_visibility='collapsed')

                    answer5 = ""
                    st.markdown(
                        f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                        '<strong>What is the Leakage Level associated with this activity?</strong>'
                        '<button class="info-button tooltip" id="info-btn">i'
                        '<span class="tooltiptext">ILI= Current Annual Real Losses (CARL) / Unavoidable Annual Real Losses (UARL)<br>Should be less than or equal to 1.5</span>'
                        '</button>'
                        '</div>', unsafe_allow_html=True)
                    answer5 = st.number_input('Enter your response (kWh/m3)1', min_value=0.0, step=0.01,label_visibility='collapsed')

                    if answer5 > 1.5 or answer4 > 0.5:
                        st.markdown(
                            f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                            '<strong>The envisioned Activity is Not EU Taxonomy Eligible</strong>'
                            '</div>', unsafe_allow_html=True)
            if answer3 == "Yes" and answer5 <= 1.5 and answer4 <= 0.5:
                with col2:
                    st.markdown(
                        f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                        '<strong>What is the net average energy consumption compared to own baseline performance average for three years (in kWh/m3)</strong>'
                        '<button class="info-button tooltip" id="info-btn">i'
                        '<span class="tooltiptext">Should be greater than or equal to 20</span>'
                        '</button>'
                        '</div>', unsafe_allow_html=True)
                    answer6 = st.number_input('Enter your response (kWh/m3)', min_value=0.0, max_value=100.0, step=0.01,label_visibility='collapsed')

                    answer7 = ""
                    st.markdown(
                        f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                        '<strong>What is the Leakage Level between the current leakage level averaged over three years, calculated using the ILI of 1.5?</strong>'
                        '<button class="info-button tooltip" id="info-btn">i'
                        '<span class="tooltiptext">Should be greater than or equal to 20</span>'
                        '</button>'
                        '</div>', unsafe_allow_html=True)
                    answer7 = st.number_input('Enter your response (kWh/m3)1', min_value=0.0, max_value=100.0, step=0.01,label_visibility='collapsed')
            #2B
            if (answer2 == "Yes" and (answer5 <= 1.5 and answer4 <= 0.5) and (answer5 != 0.0 and answer4 != 0.0)) or (answer3 == "Yes"  and (answer6 >= 20 and answer7 >= 20)):
                with col2:
                    st.markdown(
                        f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                        '<strong>What is the Greenhouse Gas emissions of your activity (in CO2e/m3)?</strong>'
                        '<button class="info-button tooltip" id="info-btn">i'
                        '<span class="tooltiptext">Should be less than 1080</span>'
                        '</button>'
                        '</div>', unsafe_allow_html=True)
                    answer8 = st.number_input('Enter your response (gCO2e/m3)', min_value=0.0, step=0.01,label_visibility='collapsed')

                    st.markdown(
                        f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                        '<strong>Does your activity significantly harm one of the remaining following Environmental Objectives:</strong>'
                        '</div>', unsafe_allow_html=True)
                    options = {
                            "Option 1": "Sustainable use and protection of water and marine resources",
                            "Option 2": "Transition to a circular economy",
                            "Option 3": "Pollution prevention and control",
                            "Option 4": "Protection and restoration of biodiversity and ecosystems",
                            "Option 5": "None of the above"
                        }
                    for key in options:
                        if key not in st.session_state:
                            st.session_state[key] = False

                    # Handle the logic for deselecting checkboxes before rendering the UI
                    if st.session_state["Option 5"]:
                        for k in options:
                            if k != "Option 5":
                                st.session_state[k] = False
                    else:
                        for k in options:
                            if k != "Option 5" and st.session_state[k]:
                                st.session_state["Option 5"] = False
                                break

                    # Create checkboxes
                    answer9 = {}
                    for key, label in options.items():
                        answer9[key] = st.checkbox(label, key=key)
                    answer9 = [label for key, label in options.items() if answer9[key]]
                if len(answer9) == 1 and ("None of the above" in answer9) and answer8 < 1080:
                    col3, col4 = st.columns((1, 5))
                    with col4:
                        st.markdown(
                        f'<div style="background-color: #00FF00; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                        '<strong>The envisioned Activity is EU Taxonomy Eligible</strong>'
                        '</div>', unsafe_allow_html=True)
                    st.markdown("<hr class='bold-hr'>", unsafe_allow_html=True)
                    col1, col2 = st.columns((1, 5))
                    with col1:
                        st.markdown(
                        f'<div style="background-color: #3f3f3f; color: white; padding: 15px; border-radius: 100px; margin-bottom: 15px; width: 100%;" class="big-font-section">'
                        '<strong>MINIMUM SAFEGUARDS</strong>'
                        '</div>', unsafe_allow_html=True)
                    #3A
                    with col2:
                        st.markdown(
                            f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                            '<strong>Did you implement an adequate Human Resources Due Diligence (HRDD)?</strong>'
                            '<button class="info-button tooltip" id="info-btn">i'
                            '<span class="tooltiptext">Promotion and protection of fundamental human rights as outlined in international conventions and agreements.</span>'
                            '</button>'
                            '</div>', unsafe_allow_html=True)
                        answer10 = st.radio('Yes or No?3', options=['Yes', 'No'], label_visibility='collapsed')
                        if answer10 == "No":
                            st.markdown(
                                f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                '<strong>Not Compliant</strong>'
                                '</div>', unsafe_allow_html=True)
                        else:
                            st.markdown(
                                f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                                '<strong>Is there any Signals of abuse to Human Resource?</strong>' 
                                '<button class="info-button tooltip" id="info-btn">i'
                                '<span class="tooltiptext">Support for fair labor practices, including ensuring safe working conditions, non- discrimination, and the right to organize and bargain collectively.</span>'
                                '</button>'
                                '</div>', unsafe_allow_html=True)
                            options = {
                                    "Option 1": "Found in breach of labour law or human rights",
                                    "Option 2": "Do not engage with relevant stakeholders",
                                    "Option 3": "None"
                                }
                            answer11 = {key: st.checkbox(label1) for key, label1 in options.items()}
                            answer11 = [label1 for key, label1 in options.items() if answer11[key]]
                            if len(answer11) >= 1 and "None" not in answer11:
                                st.markdown(
                                    f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                    '<strong>Not Compliant</strong>'
                                    '</div>', unsafe_allow_html=True)
                            elif len(answer11) == 1 and "None" in answer11:
                                #3B
                                st.markdown(
                                    f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                                    '<strong>Did any anti-corruption processes took place?</strong>'
                                    '<button class="info-button tooltip" id="info-btn">i'
                                    '<span class="tooltiptext">Implementation of measures to combat bribery and corruption in partner countries.</span>'
                                    '</button>'
                                    '</div>', unsafe_allow_html=True)
                                answer12 = st.radio('Yes or No?4', options=['Yes', 'No'], label_visibility='collapsed')
                                if answer12 == "Yes":
                                    st.markdown(
                                        f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                        '<strong>Not Compliant</strong>'
                                        '</div>', unsafe_allow_html=True)
                                else:
                                    st.markdown(
                                        f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                                        '<strong>Did the company or its senior management, including the senior management of its subsidiaries, has been convicted in court on corruption?</strong>'
                                        '<button class="info-button tooltip" id="info-btn">i'
                                        '<span class="tooltiptext">Assistance in establishing and enforcing anti-corruption policies and practices, aligned with international standards.</span>'
                                        '</button>'
                                        '</div>', unsafe_allow_html=True)
                                    answer13 = st.radio('Yes or No?9', options=['Yes', 'No'], label_visibility='collapsed')
                                    if answer13 == "Yes":
                                        st.markdown(
                                            f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                            '<strong>Not Compliant</strong>'
                                            '</div>', unsafe_allow_html=True)
                                    else:
                                        #3C
                                        st.markdown(
                                            f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                                            '<strong>The company confirms that it treats tax governance and compliance as important elements of oversight, and there are adequate tax risk management strategies and processes in place?</strong>'
                                            '<button class="info-button tooltip" id="info-btn">i'
                                            '<span class="tooltiptext">Collaboration on tax-related matters to promote fair and transparent tax systems.</span>'
                                            '</button>'
                                            '</div>', unsafe_allow_html=True)
                                        answer14 = st.radio('Yes or No?5', options=['Yes', 'No'], label_visibility='collapsed')
                                        if answer14 == "No":
                                            st.markdown(
                                                f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                                '<strong>Not Compliant</strong>'
                                                '</div>', unsafe_allow_html=True)
                                        else:
                                            st.markdown(
                                                f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                                                '<strong>Has the company or its subsidiaries violated the tax laws?</strong>'
                                                '<button class="info-button tooltip" id="info-btn">i'
                                                '<span class="tooltiptext">Support for partner countries in adopting international best practices in tax administration, compliance, and combating tax evasion.</span>'
                                                '</button>'
                                                '</div>', unsafe_allow_html=True)
                                            answer15 = st.radio('Yes or No?6', options=['Yes', 'No'], label_visibility='collapsed')
                                            if answer15 == "Yes":
                                                st.markdown(
                                                    f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                                    '<strong>Not Compliant</strong>'
                                                    '</div>', unsafe_allow_html=True)
                                            else:
                                                st.markdown(
                                                f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                                                '<strong>Does the company promote employee awareness on importance of compliance with all applicable competition laws and regulations?</strong>'
                                                '<button class="info-button tooltip" id="info-btn">i'
                                                '<span class="tooltiptext">Encouragement of open and competitive markets in partner countries to stimulate economic growth and development.</span>'
                                                '</button>'
                                                '</div>', unsafe_allow_html=True)
                                                answer16 = st.radio('Yes or No?7', options=['Yes', 'No'], label_visibility='collapsed')
                                                if answer16 == "No":
                                                    st.markdown(
                                                        f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                                        '<strong>Not Compliant</strong>'
                                                        '</div>', unsafe_allow_html=True)
                                                else:
                                                    st.markdown(
                                                    f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                                                    '<strong>Does the company or its senior management, including the senior management of its subsidiaries, has been convicted on violating competition laws?</strong>'
                                                    '<button class="info-button tooltip" id="info-btn">i'
                                                    '<span class="tooltiptext">Assistance in establishing and enforcing competition laws and regulations to prevent anti-competitive behavior and monopolies .</span>'
                                                    '</button>'
                                                    '</div>', unsafe_allow_html=True)
                                                    answer17 = st.radio('Yes or No?8', options=['Yes', 'No'], label_visibility='collapsed')
                                                    if answer17 == "Yes":
                                                        st.markdown(
                                                            f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                                            '<strong>Not Compliant</strong>'
                                                            '</div>', unsafe_allow_html=True)
                                                    else:
                                                        st.markdown(
                                                            f'<div style="background-color: #00FF00; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                                            '<strong>The envisioned Activity is compliant with the Minimum Safeguards of the EU Taxonomy. And the User can proceed to Financial Assessment.</strong>'
                                                            '</div>', unsafe_allow_html=True)
                                                        if st.session_state.page == 'main':
                                                            st.button("Continue", on_click=continue_to_phase)
                elif len(answer9) >= 1:
                    with col2:
                        st.markdown(
                            f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                            '<strong>EU Taxonomy does not align</strong>'
                            '</div>', unsafe_allow_html=True)
            else:
                with col2:
                    st.markdown(
                        f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                        '<strong>EU Taxonomy does not align</strong>'
                        '</div>', unsafe_allow_html=True)
    else:
        st.info("Please fill in all input fields to proceed with eligibility questions.")
#Make changes for the next page here
elif st.session_state.page == 'phase':

    df = load_financial_model(file_path,sheet_name='Inp_C',header=3)

    df_cleaned = df[df.notna().any(axis=1)]

    df_cleaned = df_cleaned.drop([1,3,5,8,13,18,23,29,31,35,38,41,46,48,54,56,62,70,72,77,83])

    df_cleaned['Unit'] = df_cleaned['Unit'].fillna(0)
    df_cleaned['Unnamed: 4'] = df_cleaned['Unnamed: 4'].fillna(0)
    df_cleaned['Phase_1'] = df_cleaned['Phase_1'].fillna(0)
    df_cleaned['Phase_2'] = df_cleaned['Phase_2'].fillna(0)

    df_cleaned = df_cleaned.dropna(axis=1, how='any')

    # if 'df_cleaned' not in st.session_state:
    #     st.session_state.df_cleaned = load_financial_model(file_path,sheet_name='Inp_C',header=3)

    # df_cleaned = st.session_state.df_cleaned

    # st.write(df_cleaned,"after changes dataframe")

    def custom_number_input(label, key, placeholder,value=0.0):
        return st.number_input(label, key=key, step=0.01,value=value,placeholder=placeholder)
    
    def custom_percentage_input(label, key, placeholder,value=0.0):
        return st.number_input(label, key=key, step=0.01,max_value=100.0,value=value,placeholder=placeholder)

    def custom_text_input(label, key, placeholder):
        return st.text_input(label, key=key, placeholder=placeholder)
    
    def format_date(date):
        """Format date to dd/mm/yy."""
        return date.strftime('%d/%m/%Y')
    
    def custom_date_input(label, key):
        return st.date_input(label, key=key)
    

    def calculate_future_date_months(date, months):
        whole_months = int(months)
        fractional_months = months - whole_months
        future_date = date + relativedelta(months=whole_months)
        additional_days = int(fractional_months * 30)
        future_date += relativedelta(days=additional_days)
        return future_date
    
    def calculate_future_date_years(date, years):
        whole_years = int(years)
        fractional_years = years - whole_years
        future_date = date + relativedelta(years=whole_years)
        additional_days = int(fractional_years * 365)
        future_date += relativedelta(days=additional_days)
        return future_date

    st.markdown(
        f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 100%; text-align: center; font-size: 54px; margin-top: -50px;" class="center-text">'
        '<strong>FINANCIAL ASSESSMENT</strong>'
        '</div>', unsafe_allow_html=True)
    options = ["Select an option","1", "2"]
    st.session_state.field100 = st.selectbox("Is your project a one phase or two phase project?", options, key='100')
    if st.session_state.field100 == "1":
        check_phase1 = True
        check_phase2 = False
    if st.session_state.field100 == "2":
        check_phase1 = True
        check_phase2 = True
    if check_phase1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 80%; text-align: center; font-size: 36px; margin-top: -50px;" class="center-text">'
            '<strong>Phase 1</strong>'
            '</div>', unsafe_allow_html=True)
        st.session_state.fcp1 = custom_date_input("Financial Close - Phase 1", 'fcp1key')
        st.session_state.field7 = custom_date_input("Construction Start Date - Phase 1", '7')
        st.session_state.field8 = custom_number_input("Construction Period(in months) - Phase 1", '8', "Enter")
        if st.session_state.field8 != 0:    
            st.session_state.field9 = st.write("Construction End Date: - Phase 1", calculate_future_date_months(st.session_state.field7,st.session_state.field8)) # TBC
            st.session_state.field9 = calculate_future_date_months(st.session_state.field7,st.session_state.field8)
        if st.session_state.field8 != 0:
            st.session_state.field9 = calculate_future_date_months(st.session_state.field7, st.session_state.field8)
            operations_start_date = st.session_state.field9 + timedelta(days=1)
            st.session_state.osdp1 = operations_start_date
            st.write("Operations Start Date - Phase 1:", st.session_state.osdp1)        
        st.session_state.field10 = custom_number_input("Operations Period(in Years) - Phase 1", '10', "Enter")
        if st.session_state.field10 != 0:
            st.session_state.oedp1 = st.write("Operations End Date: - Phase 1", calculate_future_date_years(st.session_state.osdp1,st.session_state.field10)) # TBC
            st.session_state.oedp1 = calculate_future_date_years(st.session_state.osdp1,st.session_state.field10)
        if st.session_state.osdp1 != 0: 
            st.session_state.drsdp1 =  st.session_state.osdp1
            st.write("Debt Repayment Start Date - Phase 1:", st.session_state.drsdp1)
        st.session_state.drtp1 = custom_number_input("Debt Repayment Tenor(in Years) - Phase 1", 'drtp1key', "Enter")
        if st.session_state.drtp1 != 0:
            st.session_state.dredp1 = st.write("Debt Repayment End Date: - Phase 1", calculate_future_date_years(st.session_state.drsdp1,st.session_state.drtp1)) # TBC
            st.session_state.dredp1 = calculate_future_date_years(st.session_state.drsdp1,st.session_state.drtp1)
        st.session_state.cepsp1 = custom_number_input("Capital Expenditure - Pre sensitivity(in LE'000s) - Phase 1", 'cepsp1key', "Enter")
        st.session_state.ces1 = custom_percentage_input("Capital Expenditure - Sensitivity (%) - Phase 1", 'cesp1key', "Enter")
        if st.session_state.cepsp1 != 0 and st.session_state.ces1 != 0:
                post_sensitivity_value = st.session_state.cepsp1 * (st.session_state.ces1 / 100)
                st.write("Calculated Capital Expenditure - Post Sensitivity (in LE'000s):", post_sensitivity_value)
                st.session_state.field11 = post_sensitivity_value
        st.session_state.field12 = custom_percentage_input("Debt (%) - Phase 1", '12', "Enter")
        if st.session_state.field12 != 0:
            equity_percentage = 1 - (st.session_state.field12 / 100)
            round_equity = round(equity_percentage * 100)
            st.write("Equity (%): ",round_equity)
            st.session_state.cep1 = round_equity
        # st.session_state.field13 = custom_percentage_input("Equity (%) - Phase 1", '13', "Enter")
        st.session_state.upfp1 = custom_number_input("Upfront Fees (%) - Phase 1", 'upfp1key', "Enter")
        st.session_state.cfp1 = custom_number_input("Commitment Fees (%) - Phase 1", 'cfp1key', "Enter")
        st.session_state.field14 = custom_percentage_input("Construction Interest Rate (Base Rate %) - Phase 1", '14', "Enter") 
        st.session_state.field15 = custom_percentage_input("Construction Interest Rate (Margin Spread %) - Phase 1",'15', "Enter")
        if st.session_state.field14 != 0 and st.session_state.field15 != 0:
            st.write("All in Rate (%)", st.session_state.field14 + st.session_state.field15) # TBC
            st.session_state.field16 = st.session_state.field14 + st.session_state.field15
        st.session_state.field17 = custom_percentage_input("Operations Interest Rate (Base Rate %) - Phase 1",'17', "Enter")
        st.session_state.field18 = custom_percentage_input("Operations Interest Rate (Margin Spread %) - Phase 1",'18', "Enter")
        if st.session_state.field17 != 0 and st.session_state.field18 != 0:
            st.write("All in Rate (%) - Phase 1", st.session_state.field17 + st.session_state.field18) # TBC
            st.session_state.field19 = st.session_state.field17 + st.session_state.field18
        st.session_state.ofwaccp1 = custom_percentage_input("Offtake - WACC (%) - Phase 1" , "ofwaccp1key" , "Enter")
        st.session_state.drcitrp1 = custom_percentage_input("Corporate Income Tax Rate (%) - Phase 1","citrp1key" ,"Enter")


        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 80%; text-align: center; font-size: 36px; margin-top: -50px;" class="center-text">'
            '<strong>Phase 1</strong>'
            '</div>', unsafe_allow_html=True)
        col1, col2 = st.columns((1, 1))
        with col1:
            st.markdown(
                '<div style="font-size:24px; font-weight:bold; color:#333333; border-bottom:2px solid #cccccc; padding-bottom:8px; margin-bottom:15px;">'
                'Fixed Operating Costs Per Year - Phase 1'
                '</div>',
                unsafe_allow_html=True
            )
            st.session_state.cgp1 = custom_number_input("Chlorine Gas (in LE'000s) - Phase 1",'cgp1key', "Enter", 0.0)
            st.session_state.cfltp1 = custom_number_input("Chemical for laboratory test (in LE'000s) - Phase 1",'cfltp1key', "Enter", 0.0)
            st.session_state.ogsgp1 = custom_number_input("Oil, Gas, Solar, and Gasoline (in LE'000s)  - Phase 1",'ogsgp1key', "Enter", 0.0)
            st.session_state.ofo1 = custom_number_input("Other Fixed Opex (in LE'000s)  - Phase 1",'ofo1key', "Enter", 0.0)
        with col2:

            st.markdown(
                '<div style="font-size:24px; font-weight:bold; color:#333333; border-bottom:2px solid #cccccc; padding-bottom:8px; margin-bottom:15px;">'
                'Variable Operating Costs Per Year - Phase 1'
                '</div>',
                unsafe_allow_html=True
            )
            st.session_state.field25 = custom_number_input("Labor (in LE'000s) - Phase 1", '25',"Enter")
            st.session_state.field26 = custom_number_input("Spare Part Cost  (in LE'000s) - Phase 1", '32',"Enter")
            st.session_state.field27 = custom_number_input("Energy Costs (LE/Kw) - Phase 1", '31',"Enter")
            st.session_state.field28 = custom_number_input("Energy Consumption (KW/m³) - Phase 1", '30',"Enter")
            if st.session_state.field27 != 0 and st.session_state.field28 != 0:
                st.write("Effective Price- Energy Costs (LE/m³) - Phase 1",st.session_state.field27*st.session_state.field28)
                st.session_state.field29 = st.session_state.field27*st.session_state.field28
            st.session_state.field34 = custom_number_input("Maintenance Costs (in LE'000s/Year) - Phase 1", '26',"Enter")
        if check_phase1 and not check_phase2:
            st.button("Continue to Risk Management", on_click=continue_to_risk_management,key='cont1')
        if check_phase2:
            st.button("Continue", on_click=continue_to_phase2,key='cont2')


        # Updating data into financial model:

        if 'oedp1' not in st.session_state:
             st.session_state.oedp1 = None

        if 'dredp1' not in st.session_state:
             st.session_state.dredp1 = None

        if 'cep1' not in st.session_state:
             st.session_state.cep1 = None

        if 'field29' not in st.session_state:
             st.session_state.field29 = None

        if 'osdp1' not in st.session_state:
             st.session_state.osdp1 = None

        if 'drsdp1' not in st.session_state:
             st.session_state.drsdp1 = None

        if st.session_state.fcp1:
            # Store the new date input into the DataFrame
            df_cleaned.at[6, 'Phase_1'] = st.session_state.fcp1

        if st.session_state.field7:
            df_cleaned.at[9, 'Phase_1'] = st.session_state.field7

        if st.session_state.field8:
            df_cleaned.at[10, 'Phase_1'] = (st.session_state.field8)

        if st.session_state.field9:
            df_cleaned.at[11, 'Phase_1'] = st.session_state.field9

        if getattr(st.session_state, 'osdp1', None):
            df_cleaned.at[14, 'Phase_1'] = st.session_state.osdp1

        if st.session_state.field10:
            df_cleaned.at[15, 'Phase_1'] = st.session_state.field10

        if getattr(st.session_state, 'oedp1', None):
            df_cleaned.at[16, 'Phase_1'] = st.session_state.oedp1

        if getattr(st.session_state, 'drsdp1', None):
            df_cleaned.at[19, 'Phase_1'] = st.session_state.drsdp1

        if st.session_state.drtp1:
            df_cleaned.at[20, 'Phase_1'] = st.session_state.drtp1

        if getattr(st.session_state, 'dredp1', None):
            df_cleaned.at[21, 'Phase_1'] = st.session_state.dredp1

        if st.session_state.cepsp1:
            df_cleaned.at[25, 'Phase_1'] = st.session_state.cepsp1

        if st.session_state.ces1:
            df_cleaned.at[26, 'Phase_1'] = st.session_state.ces1
            
        if st.session_state.field11:
            df_cleaned.at[27, 'Phase_1'] = st.session_state.field11

        if st.session_state.field12:
            df_cleaned.at[32, 'Phase_1'] = st.session_state.field12

        if getattr(st.session_state, 'cep1', None):
            df_cleaned.at[33, 'Phase_1'] = st.session_state.cep1

        if st.session_state.upfp1:
            df_cleaned.at[36, 'Phase_1'] = st.session_state.upfp1

        if st.session_state.cfp1:
            df_cleaned.at[39, 'Phase_1'] = st.session_state.cfp1

        if st.session_state.field14:
            df_cleaned.at[42, 'Phase_1'] = st.session_state.field14

        if st.session_state.field15:
            df_cleaned.at[43, 'Phase_1'] = st.session_state.field15

        if st.session_state.cgp1:
            df_cleaned.at[57, 'Phase_1'] = st.session_state.cgp1

        if st.session_state.cfltp1:
            df_cleaned.at[58, 'Phase_1'] = st.session_state.cfltp1

        if st.session_state.ogsgp1:
            df_cleaned.at[59, 'Phase_1'] = st.session_state.ogsgp1

        if st.session_state.ofo1:
            df_cleaned.at[60, 'Phase_1'] = st.session_state.ofo1

        if st.session_state.field25:
            df_cleaned.at[63, 'Phase_1'] = st.session_state.field25

        if st.session_state.field26:
            df_cleaned.at[64, 'Phase_1'] = st.session_state.field26

        if st.session_state.field27:
            df_cleaned.at[65, 'Phase_1'] = st.session_state.field27

        if st.session_state.field28:
            df_cleaned.at[66, 'Phase_1'] = st.session_state.field28

        if getattr(st.session_state, 'field29', None):
            df_cleaned.at[67, 'Phase_1'] = st.session_state.field29

        if st.session_state.field34:
            df_cleaned.at[68, 'Phase_1'] = st.session_state.field34

        if st.session_state.field17:
            df_cleaned.at[73, 'Phase_1'] = st.session_state.field17

        if st.session_state.field18:
            df_cleaned.at[74, 'Phase_1'] = st.session_state.field18

        if st.session_state.field19:
            df_cleaned.at[75, 'Phase_1'] = st.session_state.field19

        if st.session_state.ofwaccp1:
            df_cleaned.at[79, 'Phase_1'] = st.session_state.ofwaccp1

        if st.session_state.drcitrp1:
            df_cleaned.at[81, 'Phase_1'] = st.session_state.drcitrp1


        # st.write(df_cleaned


        # file_extension = Path(file_path).suffix.lower()[1:]
        # if file_extension in ['xlsx', 'xls']:

        #     with open(file_path, 'rb') as file:
        #         content = file.read(4)
        #         print(content)

        #     workbook = load_workbook(file_path)
        #     sheet = workbook['Inp_C']


        # if 'Phase_1' in df_cleaned.columns:
        #     sheet.cell(row=11, column=10, value=df_cleaned.at[6, 'Phase_1'])
        #     sheet.cell(row=14, column=10, value=df_cleaned.at[9, 'Phase_1'])
        #     sheet.cell(row=15, column=10, value=df_cleaned.at[10, 'Phase_1']) 
        #     sheet.cell(row=16, column=10, value=df_cleaned.at[11, 'Phase_1']) 
        #     sheet.cell(row=19, column=10, value=df_cleaned.at[14, 'Phase_1']) 
        #     sheet.cell(row=20, column=10, value=df_cleaned.at[15, 'Phase_1']) 
        #     sheet.cell(row=21, column=10, value=df_cleaned.at[16, 'Phase_1']) 
        #     sheet.cell(row=24, column=10, value=df_cleaned.at[19, 'Phase_1']) 
        #     sheet.cell(row=25, column=10, value=df_cleaned.at[20, 'Phase_1']) 
        #     sheet.cell(row=26, column=10, value=df_cleaned.at[21, 'Phase_1']) 
        #     sheet.cell(row=30, column=10, value=df_cleaned.at[25, 'Phase_1']) 
        #     sheet.cell(row=31, column=10, value=df_cleaned.at[26, 'Phase_1']  / 100) 
        #     sheet.cell(row=32, column=10, value=df_cleaned.at[27, 'Phase_1']) 
        #     sheet.cell(row=37, column=10, value=df_cleaned.at[32, 'Phase_1'] / 100) 
        #     sheet.cell(row=38, column=10, value=df_cleaned.at[33, 'Phase_1'] / 100) 
        #     sheet.cell(row=41, column=10, value=df_cleaned.at[36, 'Phase_1'] / 100) 
        #     sheet.cell(row=44, column=10, value=df_cleaned.at[39, 'Phase_1'] / 100) 
        #     sheet.cell(row=47, column=10, value=df_cleaned.at[42, 'Phase_1'] / 100) 
        #     sheet.cell(row=48, column=10, value=df_cleaned.at[43, 'Phase_1'] / 100) 
        #     sheet.cell(row=62, column=10, value=df_cleaned.at[57, 'Phase_1']) 
        #     sheet.cell(row=63, column=10, value=df_cleaned.at[58, 'Phase_1']) 
        #     sheet.cell(row=64, column=10, value=df_cleaned.at[59, 'Phase_1']) 
        #     sheet.cell(row=65, column=10, value=df_cleaned.at[60, 'Phase_1']) 
        #     sheet.cell(row=68, column=10, value=df_cleaned.at[63, 'Phase_1']) 
        #     sheet.cell(row=69, column=10, value=df_cleaned.at[64, 'Phase_1']) 
        #     sheet.cell(row=70, column=10, value=df_cleaned.at[65, 'Phase_1']) 
        #     sheet.cell(row=71, column=10, value=df_cleaned.at[66, 'Phase_1']) 
        #     sheet.cell(row=72, column=10, value=df_cleaned.at[67, 'Phase_1']) 
        #     sheet.cell(row=73, column=10, value=df_cleaned.at[68, 'Phase_1']) 
        #     sheet.cell(row=78, column=10, value=df_cleaned.at[73, 'Phase_1'] / 100)
        #     sheet.cell(row=79, column=10, value=df_cleaned.at[74, 'Phase_1'] / 100)
        #     sheet.cell(row=80, column=10, value=df_cleaned.at[75, 'Phase_1'] / 100)
        #     sheet.cell(row=84, column=10, value=df_cleaned.at[79, 'Phase_1']  / 100)
        #     sheet.cell(row=86, column=10, value=df_cleaned.at[81, 'Phase_1']  / 100)


        #     workbook.save(file_path)



    
elif st.session_state.page == 'phase2':

    df = load_financial_model(file_path,sheet_name='Inp_C',header=3)


    df_cleaned = df[df.notna().any(axis=1)]

    # more_df_cleaned = df_cleaned.drop([1,3,5,8,13,18,23,29,31,35,38,41,46,48,54,56,62,70,72,77,83,85,86,87])
    df_cleaned = df_cleaned.drop([1,3,5,8,13,18,23,29,31,35,38,41,46,48,54,56,62,70,72,77,83])

    df_cleaned['Unit'] = df_cleaned['Unit'].fillna(0)
    df_cleaned['Unnamed: 4'] = df_cleaned['Unnamed: 4'].fillna(0)
    df_cleaned['Phase_1'] = df_cleaned['Phase_1'].fillna(0)
    df_cleaned['Phase_2'] = df_cleaned['Phase_2'].fillna(0)

    df_cleaned = df_cleaned.dropna(axis=1, how='any')

    def custom_number_input(label, key, placeholder,value=0.0):
        return st.number_input(label, key=key, step=0.01,value=value,placeholder=placeholder)
    
    def custom_percentage_input(label, key, placeholder,value=0.0):
        return st.number_input(label, key=key, step=0.01,max_value=100.0,value=value,placeholder=placeholder)

    def custom_text_input(label, key, placeholder):
        return st.text_input(label, key=key, placeholder=placeholder)
    
    def custom_date_input(label, key):
        return st.date_input(label, key=key)
    
    def calculate_future_date_months(date, months):
        whole_months = int(months)
        fractional_months = months - whole_months
        future_date = date + relativedelta(months=whole_months)
        additional_days = int(fractional_months * 30)
        future_date += relativedelta(days=additional_days)
        return future_date
    
    def calculate_future_date_years(date, years):
        whole_years = int(years)
        fractional_years = years - whole_years
        future_date = date + relativedelta(years=whole_years)
        additional_days = int(fractional_years * 365)
        future_date += relativedelta(days=additional_days)
        return future_date

    st.markdown(
        f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 100%; text-align: center; font-size: 54px; margin-top: -50px;" class="center-text">'
        '<strong>FINANCIAL ASSESSMENT</strong>'
        '</div>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 80%; text-align: center; font-size: 36px; margin-top: -50px;" class="center-text">'
        '<strong>Phase 2</strong>'
        '</div>', unsafe_allow_html=True)
    st.session_state.fcp2 = custom_date_input("Financial Close - Phase 2", 'fcp2key')
    st.session_state.field35 = custom_date_input("Construction Start Date - Phase 2", '35')
    st.session_state.field36 = custom_number_input("Construction Period(in months) - Phase 2", '36', "Enter",0.0)
    if st.session_state.field36 != 0:
        st.write("Construction End Date:", calculate_future_date_months(st.session_state.field35,st.session_state.field36)) # TBC
        st.session_state.field37 = calculate_future_date_months(st.session_state.field35,st.session_state.field36)

    if st.session_state.field36 != 0:
        st.session_state.field37 = calculate_future_date_months(st.session_state.field35, st.session_state.field36)
        operations_start_date = st.session_state.field37 + timedelta(days=1)
        st.session_state.osdp2 = operations_start_date
        st.write("Operations Start Date - Phase 2:", st.session_state.osdp2)    
    # st.session_state.osdp2 = custom_date_input("Operations Start Date - Phase 2", 'osdp2key')
    st.session_state.field38 = custom_number_input("Operations Period(in Years) - Phase 2", '38', "Enter",0.0)
    if st.session_state.field38 != 0:
        st.session_state.oedp2 = st.write("Operations End Date: - Phase 2", calculate_future_date_years(st.session_state.osdp2,st.session_state.field38)) # TBC
        st.session_state.oedp2 = calculate_future_date_years(st.session_state.osdp2,st.session_state.field38)
    if st.session_state.osdp2 != 0: 
        st.session_state.drsdp2 =  st.session_state.osdp2
        st.write("Debt Repayment Start Date - Phase 2:", st.session_state.drsdp2)
    # st.session_state.drsdp2 = custom_date_input("Debt Repayment Start Date - Phase 2", 'drsdp2key')
    st.session_state.drtp2 = custom_number_input("Debt Repayment Tenor(in Years) - Phase 2", 'drtp2key', "Enter")
    if st.session_state.drtp2 != 0:
        st.session_state.dredp2 = st.write("Debt Repayment End Date: - Phase 2", calculate_future_date_years(st.session_state.drsdp2,st.session_state.drtp2)) # TBC
        st.session_state.dredp2 = calculate_future_date_years(st.session_state.drsdp2,st.session_state.drtp2)
    st.session_state.cepsp2 = custom_number_input("Capital Expenditure - Pre sensitivity (in LE'000s) - Phase 2", 'cepsp1key', "Enter")
    st.session_state.ces2 = custom_percentage_input("Capital Expenditure - Sensitivity (%) - Phase 2", 'cesp1key', "Enter")
    if st.session_state.cepsp2 != 0 and st.session_state.ces2 != 0:
            post_sensitivity_value = st.session_state.cepsp2 * (st.session_state.ces2 / 100)
            st.write("Calculated Capital Expenditure - Post Sensitivity (in LE'000s):", post_sensitivity_value)
            st.session_state.field69 = post_sensitivity_value
    st.session_state.field40 = custom_percentage_input("Debt (%) - Phase 2", '40', "Enter",0.0) 
    if st.session_state.field40 != 0:
        equity_percentage = 1 - (st.session_state.field40 / 100)
        round_equity = round(equity_percentage * 100)
        st.write("Equity (%): ",round_equity)
        st.session_state.cep2 = round_equity
    st.session_state.upfp2 = custom_number_input("Upfront Fees (%) - Phase 2", 'upfp1key', "Enter")
    st.session_state.cfp2 = custom_number_input("Commitment Fees (%) - Phase 2", 'cfp1key', "Enter")
    st.session_state.field42 = custom_percentage_input("Construction Interest Rate (Base Rate %) - Phase 2", '42', "Enter",0.0) 
    st.session_state.field43 = custom_percentage_input("Construction Interest Rate (Margin Spread %) - Phase 2",'43', "Enter",0.0)
    if st.session_state.field42 != 0 and st.session_state.field43 != 0:
        st.write("All in Rate (%) - Phase 2", st.session_state.field42 + st.session_state.field43) # TBC
        st.session_state.field44 = st.session_state.field42 + st.session_state.field43
    st.session_state.field45 = custom_percentage_input("Operations Interest Rate (Base Rate %) - Phase 2",'45', "Enter",0.0)
    st.session_state.field46 = custom_percentage_input("Operations Interest Rate (Margin Spread %) - Phase 2",'46', "Enter",0.0)
    if st.session_state.field45 != 0 and st.session_state.field46 != 0:
        st.write("All in Rate (%) - Phase 2", st.session_state.field45 + st.session_state.field46) # TBC
        st.session_state.field47 = st.session_state.field45 + st.session_state.field46
    st.session_state.ofwaccp2 = custom_percentage_input("Offtake - WACC (%) - Phase 2" , "ofwaccp2key" , "Enter")
    st.session_state.drcitrp2 = custom_percentage_input("Corporate Income Tax Rate (%) - Phase 2","citrp2key" ,"Enter")
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 80%; text-align: center; font-size: 36px; margin-top: -50px;" class="center-text">'
        '<strong>Phase 2</strong>'
        '</div>', unsafe_allow_html=True)
    col1, col2 = st.columns((1, 1))
    with col1:
        st.markdown(
            '<div style="font-size:24px; font-weight:bold; color:#333333; border-bottom:2px solid #cccccc; padding-bottom:8px; margin-bottom:15px;">'
            'Fixed Operating Costs Per Year - Phase 2'
            '</div>',
            unsafe_allow_html=True
        )
        st.session_state.cgp2 = custom_number_input("Chlorine Gas (in LE'000s) - Phase 2",'cgp2key', "Enter",0.0)
        st.session_state.cfltp2 = custom_number_input("Chemical for laboratory test (in LE'000s) - Phase 2",'cfltp2key', "Enter",0.0)
        st.session_state.ogsgp2 = custom_number_input("Oil, Gas, Solar, and Gasoline (in LE'000s)  - Phase 2",'ogsgp2key', "Enter",0.0)
        st.session_state.ofo2 = custom_number_input("Other Fixed Opex (in LE'000s)  - Phase 2",'ofo2key', "Enter",0.0)
    with col2:
        st.markdown(
            '<div style="font-size:24px; font-weight:bold; color:#333333; border-bottom:2px solid #cccccc; padding-bottom:8px; margin-bottom:15px;">'
            'Variable Operating Costs Per Year - Phase 2'
            '</div>',
            unsafe_allow_html=True
        )
        st.session_state.field53 = custom_number_input("Labor (in LE'000s) - Phase 2", '53',"Enter",0.0)
        st.session_state.field62 = custom_number_input("Spare Part Cost  (in LE'000s) - Phase 2", '32',"Enter")
        st.session_state.field59 = custom_number_input("Energy Costs (LE/Kw) - Phase 2", '59',"Enter",0.0)
        st.session_state.field58 = custom_number_input("Energy Consumption (KW/m³) - Phase 2", '58',"Enter",0.0)
        if st.session_state.field58 != 0 and st.session_state.field59 != 0:
            st.write("Effective Price - Energy Costs (LE/m³) - Phase 2",st.session_state.field58*st.session_state.field59)
            st.session_state.field60 = st.session_state.field58*st.session_state.field59
        st.session_state.field54 = custom_number_input("Maintenance Costs (in LE'000s/Year) - Phase 2", '54',"Enter",0.0)
    col1,col2 = st.columns([1,18])
    with col1:
        if st.session_state.page == 'phase2':
            st.button("Back", on_click=continue_to_phase)
    with col2:
        # if st.session_state.page == 'phase2':
        st.button("Continue to Risk Assesment", on_click=continue_to_risk_management)


    # Update data in financial model of phase 2

    if 'oedp2' not in st.session_state:
            st.session_state.oedp1 = None

    if 'dredp2' not in st.session_state:
            st.session_state.dredp1 = None

    if 'cep2' not in st.session_state:
            st.session_state.cep1 = None

    if 'field60' not in st.session_state:
            st.session_state.field60 = None

    if 'field69' not in st.session_state:
            st.session_state.field69 = None

    if 'drsdp2' not in st.session_state:
        st.session_state.drsdp2 = None

    if st.session_state.fcp2:
        df_cleaned.at[6, 'Phase_2'] = st.session_state.fcp2

    if st.session_state.field35:
        df_cleaned.at[9, 'Phase_2'] = st.session_state.field35

    if st.session_state.field36:
        df_cleaned.at[10, 'Phase_2'] = st.session_state.field36

    if st.session_state.field37:
        df_cleaned.at[11, 'Phase_2'] = st.session_state.field37

    if st.session_state.osdp2:
        df_cleaned.at[14, 'Phase_2'] = st.session_state.osdp2

    if st.session_state.field38:
        df_cleaned.at[15, 'Phase_2'] = st.session_state.field38

    if getattr(st.session_state, 'oedp2', None):
        df_cleaned.at[16, 'Phase_2'] = st.session_state.oedp2

    if getattr(st.session_state, 'drsdp2', None):
        df_cleaned.at[19, 'Phase_2'] = st.session_state.drsdp2

    if st.session_state.drtp2:
        df_cleaned.at[20, 'Phase_2'] = st.session_state.drtp2

    if getattr(st.session_state, 'dredp2', None):
        df_cleaned.at[21, 'Phase_2'] = st.session_state.dredp2

    if st.session_state.cepsp2:
        df_cleaned.at[25, 'Phase_2'] = st.session_state.cepsp2

    if st.session_state.ces2:
        df_cleaned.at[26, 'Phase_2'] = st.session_state.ces2
        
    if getattr(st.session_state, 'field69', None):
        df_cleaned.at[27, 'Phase_2'] = st.session_state.field69

    if st.session_state.field40:
        df_cleaned.at[32, 'Phase_2'] = st.session_state.field40

    if getattr(st.session_state, 'cep2', None):
        df_cleaned.at[33, 'Phase_2'] = st.session_state.cep2

    if st.session_state.upfp2:
        df_cleaned.at[36, 'Phase_2'] = st.session_state.upfp2

    if st.session_state.cfp2:
        df_cleaned.at[39, 'Phase_2'] = st.session_state.cfp2

    if st.session_state.field42:
        df_cleaned.at[42, 'Phase_2'] = st.session_state.field42

    if st.session_state.field43:
        df_cleaned.at[43, 'Phase_2'] = st.session_state.field43

    if st.session_state.field44:
        df_cleaned.at[44, 'Phase_2'] = st.session_state.field44

    if st.session_state.cgp2:
        df_cleaned.at[57, 'Phase_2'] = st.session_state.cgp2

    if st.session_state.cfltp2:
        df_cleaned.at[58, 'Phase_2'] = st.session_state.cfltp2

    if st.session_state.ogsgp2:
        df_cleaned.at[59, 'Phase_2'] = st.session_state.ogsgp2

    if st.session_state.ofo2:
        df_cleaned.at[60, 'Phase_2'] = st.session_state.ofo2

    if st.session_state.field53:
        df_cleaned.at[63, 'Phase_2'] = st.session_state.field53

    if st.session_state.field62:
        df_cleaned.at[64, 'Phase_2'] = st.session_state.field62

    if st.session_state.field58:
        df_cleaned.at[65, 'Phase_2'] = st.session_state.field58

    if st.session_state.field59:
        df_cleaned.at[66, 'Phase_2'] = st.session_state.field59

    if st.session_state.field60:
        df_cleaned.at[67, 'Phase_2'] = st.session_state.field60

    if st.session_state.field54:
        df_cleaned.at[68, 'Phase_2'] = st.session_state.field54

    if st.session_state.field45:
        df_cleaned.at[73, 'Phase_2'] = st.session_state.field45

    if st.session_state.field46:
        df_cleaned.at[74, 'Phase_2'] = st.session_state.field46

    if st.session_state.field47:
        df_cleaned.at[75, 'Phase_2'] = st.session_state.field47

    if st.session_state.ofwaccp2:
        df_cleaned.at[79, 'Phase_2'] = st.session_state.ofwaccp2

    if st.session_state.drcitrp2:
        df_cleaned.at[81, 'Phase_2'] = st.session_state.drcitrp2



    # file_extension = Path(file_path).suffix.lower()[1:]
    # if file_extension in ['xlsx', 'xls']:
    #     workbook = load_workbook(file_path)
    #     sheet = workbook['Inp_C']

    # if 'Phase_2' in df_cleaned.columns:
    #     sheet.cell(row=11, column=11, value=df_cleaned.at[6, 'Phase_2'])
    #     sheet.cell(row=14, column=11, value=df_cleaned.at[9, 'Phase_2'])
    #     sheet.cell(row=15, column=11, value=df_cleaned.at[10, 'Phase_2']) 
    #     sheet.cell(row=16, column=11, value=df_cleaned.at[11, 'Phase_2']) 
    #     sheet.cell(row=19, column=11, value=df_cleaned.at[14, 'Phase_2']) 
    #     sheet.cell(row=20, column=11, value=df_cleaned.at[15, 'Phase_2']) 
    #     sheet.cell(row=21, column=11, value=df_cleaned.at[16, 'Phase_2']) 
    #     sheet.cell(row=24, column=11, value=df_cleaned.at[19, 'Phase_2']) 
    #     sheet.cell(row=25, column=11, value=df_cleaned.at[20, 'Phase_2']) 
    #     sheet.cell(row=26, column=11, value=df_cleaned.at[21, 'Phase_2']) 
    #     sheet.cell(row=30, column=11, value=df_cleaned.at[25, 'Phase_2']) 
    #     sheet.cell(row=31, column=11, value=df_cleaned.at[26, 'Phase_2']  / 100) 
    #     sheet.cell(row=32, column=11, value=df_cleaned.at[27, 'Phase_2']) 
    #     sheet.cell(row=37, column=11, value=df_cleaned.at[32, 'Phase_2'] / 100) 
    #     sheet.cell(row=38, column=11, value=df_cleaned.at[33, 'Phase_2'] / 100) 
    #     sheet.cell(row=41, column=11, value=df_cleaned.at[36, 'Phase_2'] / 100) 
    #     sheet.cell(row=44, column=11, value=df_cleaned.at[39, 'Phase_2'] / 100) 
    #     sheet.cell(row=47, column=11, value=df_cleaned.at[42, 'Phase_2'] / 100) 
    #     sheet.cell(row=48, column=11, value=df_cleaned.at[43, 'Phase_2'] / 100) 
    #     sheet.cell(row=62, column=11, value=df_cleaned.at[57, 'Phase_2']) 
    #     sheet.cell(row=63, column=11, value=df_cleaned.at[58, 'Phase_2']) 
    #     sheet.cell(row=64, column=11, value=df_cleaned.at[59, 'Phase_2']) 
    #     sheet.cell(row=65, column=11, value=df_cleaned.at[60, 'Phase_2']) 
    #     sheet.cell(row=68, column=11, value=df_cleaned.at[63, 'Phase_2']) 
    #     sheet.cell(row=69, column=11, value=df_cleaned.at[64, 'Phase_2']) 
    #     sheet.cell(row=70, column=11, value=df_cleaned.at[65, 'Phase_2']) 
    #     sheet.cell(row=71, column=11, value=df_cleaned.at[66, 'Phase_2']) 
    #     sheet.cell(row=72, column=11, value=df_cleaned.at[67, 'Phase_2']) 
    #     sheet.cell(row=78, column=11, value=df_cleaned.at[73, 'Phase_2'] / 100)
    #     sheet.cell(row=79, column=11, value=df_cleaned.at[74, 'Phase_2'] / 100)
    #     sheet.cell(row=80, column=11, value=df_cleaned.at[75, 'Phase_2'] / 100)
    #     sheet.cell(row=84, column=11, value=df_cleaned.at[79, 'Phase_2']  / 100)
    #     sheet.cell(row=86, column=11, value=df_cleaned.at[81, 'Phase_2']  / 100)


    #     workbook.save(file_path)


elif st.session_state.page == 'risk-management':
    st.markdown(
        f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 50px; margin-bottom: 15px; width: 80%; text-align: center;font-size: 36px; margin-top: -50px;" class="center-text">'
        '<strong>Risk Assesment</strong>'
        '</div>', unsafe_allow_html=True)


    if 'editable_values' not in st.session_state:
        st.session_state.editable_values = { 
            column: [""] * 15 for column in [
                "Category", 
                "Base Cost Link (CAPEX/OPEX/Maintenance)", 
                "Percentage of Base Cost (%)", 
                "Recurrence (if OPEX related)", 
                "Probability of Occurrence (%)", 
                "Allocation to Government (%)", 
                "Allocation to Private Sector (%)",
                "mitigation cost"
            ]
        }

    # Load the Excel file into a Pandas DataFrame
    # df = pd.read_excel(excel_file_path, sheet_name='Sheet1', header=4)
    # def load_financial_model(file_path):
    #     return pd.read_excel(file_path, sheet_name='Sheet1',header=4)
    
    # df = load_financial_model('Project Damietta_CashFlow Model_01b.xlsx')

    # @st.cache_data
    # def load_financial_model(file_path):
    #     file_extension = Path(file_path).suffix.lower()[1:]
        
    #     if file_extension == 'xlsx':
    #         return pd.read_excel(file_path, sheet_name='Sheet1',header=4, engine='openpyxl')
    #     elif file_extension == 'xls':
    #         return pd.read_excel(file_path, sheet_name='Sheet1',header=4)
    #     elif file_extension == 'csv':
    #         return pd.read_csv(file_path)
    #     else:
    #         raise Exception("File not supported")
 
    
        
    df = load_financial_model(file_path,sheet_name='Sheet1',header=4)



    df = df.iloc[:, 1:]

    # st.write(df)

    df = df.drop([37,38])
   
    df = df.dropna(axis=1, how='any')

    

    # Extract risk list
    risk_list = df['Risk'].dropna().tolist()

    # Store selected risks in session state
    if 'selected_risks' not in st.session_state:
        st.session_state.selected_risks = ["Select a risk"] * 15

    # List of editable fields
    editable_fields = [
        "Category", 
        "Base Cost Link (CAPEX/OPEX/Maintenance)", 
        "Percentage of Base Cost (%)", 
        "Recurrence (if OPEX related)", 
        "Probability of Occurrence (%)", 
        "Allocation to Government (%)", 
        "Allocation to Private Sector (%)",
        "Mitigation cost"
    ]

    # Function to ensure a risk can only be selected once
    def available_risks(index):
        selected = st.session_state.selected_risks[:index] + st.session_state.selected_risks[index+1:]
        return ["Select a risk"] + [risk for risk in risk_list if risk not in selected]

    for i in range(15):
        st.markdown(f"### Select Risk {i + 1}")

        # Dropdown to select the risk, ensure each risk can only be selected once
        selected_risk = st.selectbox(
            f"Risk {i + 1}",
            available_risks(i),
            key=f"risk_{i}",
            index=available_risks(i).index(st.session_state.selected_risks[i])
        )

        st.session_state.selected_risks[i] = selected_risk

        # If a valid risk is selected, show editable inputs
        if selected_risk != "Select a risk":
            selected_risk_data = df[df['Risk'] == selected_risk].iloc[0]

                # Use an expander to show editable fields for the selected risk
            with st.expander(f"Details for {selected_risk}"):
                for column in editable_fields:
                    # Check if the column is one of the exceptions
                    if column in ["Mitigation cost"]:
                        current_value_str = "0.0"
                    else:
                        current_value = selected_risk_data[column] if pd.notna(selected_risk_data[column]) else ""  # Set default value to 0 for other fields

                        current_value_str = f"{current_value * 100:.2f}" if column in [
                            "Percentage of Base Cost (%)", 
                            "Probability of Occurrence (%)", 
                            "Allocation to Government (%)", 
                            "Allocation to Private Sector (%)"
                        ] else str(current_value)

                    # Display as text input for user to edit
                    new_value = st.text_input(
                        f"{column} (Risk {i + 1})", 
                        value=current_value_str,  
                        key=f"text_input_{i}_{column}"
                    )

                    # Update the value in the DataFrame
                    if column in ["Percentage of Base Cost (%)", "Probability of Occurrence (%)", 
                                "Allocation to Government (%)", "Allocation to Private Sector (%)"]:
                        try:
                            df.loc[df['Risk'] == selected_risk, column] = float(new_value) / 100
                        except ValueError:
                            pass
                    elif column == "Mitigation cost":
                        try:
                            df.loc[df['Risk'] == selected_risk, column] = float(new_value)
                        except ValueError:
                            pass
                    else:
                        df.loc[df['Risk'] == selected_risk, column] = new_value
    # if st.button("Save Changes"):
    #     if "Select a risk" in st.session_state.selected_risks:
    #         st.error("Please select all 15 risks before saving changes.")
    #     else:
    #         try:
    #             file_extension = Path(file_path).suffix.lower()[1:]
    #             if file_extension in ['xlsx', 'xls']:
    #                 book = load_workbook(file_path)
    #                 sheet = book['Sheet1']

    #             # Iterate through all selected risks and update corresponding rows in the Excel sheet
    #             for i, selected_risk in enumerate(st.session_state.selected_risks):
    #                 # Find the row corresponding to the selected risk
    #                 risk_row = df.index[df['Risk'] == selected_risk].tolist()[0] + 6  # +5 to account for header offset in Excel

    #                 # Update only the changed fields in the sheet
    #                 for column in editable_fields:
    #                     col_idx = df.columns.get_loc(column) + 2  

    #                     if column in ["Percentage of Base Cost (%)", "Probability of Occurrence (%)", 
    #                                 "Allocation to Government (%)", "Allocation to Private Sector (%)"]:
    #                         sheet.cell(row=risk_row, column=col_idx, value=df.loc[df['Risk'] == selected_risk, column].values[0])  # Convert back to percentage
    #                     elif column == "mitigation cost":
    #                         sheet.cell(row=risk_row, column=col_idx, value=df.loc[df['Risk'] == selected_risk, column].values[0])
    #                     else:
    #                         sheet.cell(row=risk_row, column=col_idx, value=df.loc[df['Risk'] == selected_risk, column].values[0])
    #             book.save(file_path)
    #             st.success("All changes have been saved successfully!")

    #         except Exception as e:
    #             st.error(f"Error saving changes: {e}")

    if st.session_state.page == 'risk-management':
        st.button("Back" , on_click = continue_to_phase2)
    st.button("Dashboard",on_click = continue_to_dashboard)

elif st.session_state.page == 'dashboard':

    def load_lottie_url(url: str):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    lottie_url1 = "https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json"  
    lottie_url2 = "https://lottie.host/da208e68-3a3a-48a9-b73f-17f8925cde2a/zJ0MoRmhHJ.json"
    lottie_animation1 = load_lottie_url(lottie_url1)
    lottie_animation2 = load_lottie_url(lottie_url2)
    st.sidebar.header("Dashboard Navigation")
    options = st.sidebar.radio("Select a page:", ["Data Overview","User Details","Download Report"])
    if  options == "Data Overview":
        df = load_financial_model(file_path,sheet_name='Output',header=7)

        fixed_indices = [0, 1, 2,3,9]

        range_indices = list(range(11, 63))

        indcies_to_drop = range_indices + fixed_indices

        df_cleaned = df.drop(fixed_indices)


        # Total risk values:
        df_risks = load_financial_model(file_path,sheet_name='Sheet1',header=4)

        cell_value = df_risks.iloc[38, 14]
        cell_value_2 = df_risks.iloc[38, 15]

        rounded_value_risk_total = f'{cell_value:.2f}'
        rounded_value_risk_total_2 = f'{cell_value_2:.2f}'


        # st.write(df_risks)


        # Dashboard title
        # st.set_page_config(page_title="Financial Analytics Dashboard", layout="wide")
        st.markdown("""
            <style>
                .custom-title {
                    font-size: 32px;
                    font-weight: 800;
                    color: #FFFFFF; /* White text for contrast */
                    background-color: #000c66; 
                    padding: 15px 20px;
                    border-radius: 10px;
                    text-align: center;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3); 
                    margin-bottom: 20px;
                    letter-spacing: 1px; 

                }
                
            </style>
            <div class="custom-title">Financial Analytics Dashboard</div>
            """, unsafe_allow_html=True
        )
        st.divider()

        total_unitary_charge_phase_1 = df_cleaned.loc[8, 'Phase_1']
        total_unitary_charge_phase_2 = df_cleaned.loc[8, 'Phase_2']
        equity_irr_phase_1 = df_cleaned.loc[10, 'Phase_1']
        equity_irr_phase_2 = df_cleaned.loc[10, 'Phase_2']

        # Convert IRR to percentage
        equity_irr_phase_1_percentage = equity_irr_phase_1 * 100  
        equity_irr_phase_2_percentage = equity_irr_phase_2 * 100

        # Summary Metrics Section
        st.markdown("""
            <style>
                .custom-subheader {
                    color: #000c66;
                    font-size: 28px;
                    font-weight: bold;
                    margin-top: 20px; /* Optional: add space above the subheader */
                    margin-bottom: 10px; /* Optional: add space below the subheader */
                }
            </style>
            <h2 class='custom-subheader'>Key Financial Metrics</h2>
            """, unsafe_allow_html=True
        )

        # Create a container for the cards to ensure they are displayed inline
        cols = st.columns(6)

        # Define a function to create a styled metric card with different colors
        def create_metric_card(col, label, value, color):
            col.markdown(
                f"""
                <div style="
                    border-radius: 10px; 
                    padding: 15px; 
                    text-align: left; 
                    background-color: {color}; 
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                    color: white;
                    margin-bottom: 15px;
                    display:flex;
                    flex-direction:column;
                    align-items:center;
                    min-height:144px
                ">
                    <h4 style="margin: 0; font-size: 15px; font-weight: 800;text-align:center">{label}</h4>
                    <p style="font-size: 16px;font-weight:900; margin: 5px 0 0 0;">{value}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Create cards for each metric with custom colors
        create_metric_card(cols[0], "Total Unity Charge - Phase 1", f"{total_unitary_charge_phase_1:.2f} LE/m³", "#00C9A7")  # Navy blue
        create_metric_card(cols[1], "Total Unity Charge - Phase 2", f"{total_unitary_charge_phase_2:.2f} LE/m³", "#FFDD44")  # Gold/yellow
        create_metric_card(cols[2], "Equity IRR - Phase 1", f"{equity_irr_phase_1_percentage:.2f}%", "#17A2B8")  # Teal
        create_metric_card(cols[3], "Equity IRR - Phase 2", f"{equity_irr_phase_2_percentage:.2f}%", "#E74C3C")  # Red
        create_metric_card(cols[4], "Cost of risk on the Government (post mitigation)", f"{rounded_value_risk_total}", "#E67E22")  
        create_metric_card(cols[5], "Cost of risk on the Private (post mitigation)", f"{rounded_value_risk_total_2}", "#D35400") 

        st.divider()

        # Tariffs Comparison (Phase 1 vs Phase 2)
        st.markdown("""
            <style>
                .custom-header {
                    font-size: 24px;
                    font-weight: 700;
                    color: #FFFFFF; /* White text */
                    background-color: #001f3f; /* Navy blue background */
                    padding: 10px 15px;
                    border-radius: 8px;
                    text-align: left;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15); /* Optional shadow for depth */
                    margin-bottom: 10px;
                }
            </style>
            <div class="custom-header">Comparison of Tariffs between Phase 1 and Phase 2</div>
            """, unsafe_allow_html=True
        )

        tariffs = df_cleaned[['Unnamed: 4', 'Phase_1', 'Phase_2']].iloc[:5].set_index('Unnamed: 4')

        fig = px.bar(
            tariffs,
            barmode='group',
            title="Tariff Comparison (Phase 1 vs Phase 2)",
            color_discrete_sequence=["#001f3f", "#FFDD44"],
            labels={"value": "Tariff", "Unnamed: 4": "Metric"},
            text_auto=True  # Display labels on bars
        )

        fig.update_layout(
            title_font=dict(size=18, color='darkblue'),
            xaxis=dict(title="Metric"),
            yaxis=dict(title="Tariff Value"),
            legend=dict(orientation="h", y=1.1)
        )

        # Update traces to position labels on top of bars
        fig.update_traces(
            textposition="outside"
        )

        st.plotly_chart(fig, use_container_width=True)

        # Equity IRR Bar Chart with Labels on Top
        st.markdown("""
            <style>
                .custom-subheader {
                    font-size: 24px;
                    font-weight: 700;
                    color: #FFFFFF; /* White text for contrast */
                    background-color: #FFDD44; /* Yellow background matching the dashboard theme */
                    padding: 10px 15px;
                    border-radius: 8px;
                    text-align: left;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15); /* Soft shadow for depth */
                    margin-bottom: 10px;
                }
            </style>
            <div class="custom-subheader">Equity IRR Distribution</div>
            """, unsafe_allow_html=True
        )

        equity_irr_data = {
            "Phase": ["Phase 1", "Phase 2"],
            "Equity IRR (%)": [equity_irr_phase_1_percentage, equity_irr_phase_2_percentage]
        }

        fig_bar = px.bar(
            equity_irr_data,
            x="Phase",
            y="Equity IRR (%)",
            title="Equity IRR Distribution between Phase 1 and Phase 2",
            color="Phase",
            color_discrete_map={"Phase 1": "#001f3f", "Phase 2": "#FFDD44"},
            text="Equity IRR (%)"  # Adding labels for the bars
        )

        fig_bar.update_layout(
            title_font=dict(size=18, color='darkblue'),
            xaxis=dict(title="Phase"),
            yaxis=dict(title="Equity IRR (%)"),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
            margin=dict(l=40, r=40, t=40, b=40)
        )

        fig_bar.update_traces(
            texttemplate='%{text:.2f}',  # Format text label as needed
            textposition="outside" ,      # Position label on top of the bars
            textfont=dict(size=10)
        )

        st.plotly_chart(fig_bar, use_container_width=True)

        # Total Unitary Charge Bar Chart with Labels on Top
        st.markdown("""
            <style>
                .custom-subheader {
                    font-size: 24px;
                    font-weight: 700;
                    color: #FFFFFF; /* White text for contrast */
                    background-color: #001f3f; /* Yellow background matching the dashboard theme */
                    padding: 10px 15px;
                    border-radius: 8px;
                    text-align: left;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15); /* Soft shadow for depth */
                    margin-bottom: 10px;
                }
            </style>
            <div class="custom-subheader">Total Unitary Charge Comparison</div>
            """, unsafe_allow_html=True
        )

        unitary_charge_data = {
            "Phase": ["Phase 1", "Phase 2"],
            "Total Unitary Charge (LE/m³)": [total_unitary_charge_phase_1, total_unitary_charge_phase_2]
        }

        fig_bar = px.bar(
            unitary_charge_data,
            x="Phase",
            y="Total Unitary Charge (LE/m³)",
            title="Total Unitary Charge for Phase 1 and Phase 2",
            color="Phase",
            color_discrete_map={"Phase 1": "#001f3f", "Phase 2": "#FFDD44"},
            text="Total Unitary Charge (LE/m³)"  # Adding labels for the bars
        )

        fig_bar.update_layout(
            title_font=dict(size=18, color='darkblue'),
            xaxis=dict(title="Phase"),
            yaxis=dict(title="Total Unitary Charge (LE/m³)"),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
            margin=dict(l=40, r=40, t=40, b=40)
        )

        fig_bar.update_traces(
            texttemplate='%{text:.2f}',  # Format text label as needed
            textposition="outside" ,      # Position label on top of the bars
            textfont=dict(size=10)
        )

        st.plotly_chart(fig_bar, use_container_width=True)

        # Conclusion or Additional Notes Section
        st.markdown("### Additional Insights")
        st.text("Provide additional analysis, insights, or explanations here to aid user interpretation.")

    elif options == "User Details":
        col1,col2 = st.columns([3,5])
        with col1:
            st.markdown("<br><br>", unsafe_allow_html=True)
            # st_lottie(lottie_animation1, height=350, key="home1")
            st_lottie(lottie_animation2, height=400, key="home2")
        with col2:
            st.markdown(
            f'<br><div style="background-color: #3f3f3f; color: white; padding: 10px; border-radius: 50px; width:70%; margin-bottom: 15px; font-size: 28px;text-align: center;">'
            '<strong>USER DETAILS</strong>'
            '</div>', unsafe_allow_html=True)
            custom_css = """
            <style>
            .custom-text {
                font-family: 'Arial', sans-serif; /* Change the font family here */
                font-size: 24px; /* Change the text size here */
                color: #333; /* Change the text color here */
                padding: 10px; /* Add some padding if needed */
                background-color: #FFD700; /* Change the background color here */
                border-radius: 50px; /* Optional: Add rounded corners */
                text-align: center;
                margin-bottom: 15px;
                width:70%;
            }
            </style>
            """

            st.markdown(custom_css, unsafe_allow_html=True)

            st.markdown(f'<div class="custom-text">Username: {st.session_state.field1}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="custom-text">Project: {st.session_state.field2}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="custom-text">Capacity: {st.session_state.field3}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="custom-text">Location: {st.session_state.field4}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="custom-text">Date: {st.session_state.field5}</div>', unsafe_allow_html=True)
    elif options == "Download Report":
        st_lottie(lottie_animation1, height=400, key="home3")
        def generate_report():
            data = {
                "Field": ["Username", "Project", "Capacity", "Location", "Option"],
                "Value": [
                    st.session_state.field1,
                    st.session_state.field2,
                    st.session_state.field3,
                    st.session_state.field4,
                    st.session_state.field5
                ]
            }
            df = pd.DataFrame(data)
            
            buffer = StringIO()
            df.to_csv(buffer, index=False)
            return buffer.getvalue()

        # Download button
        csv_report = generate_report()
        st.markdown("""
            <style>
            .download-button {
                display: flex;
                justify-content: center;
                align-items: center;
                
            }
            .download-button a {
                display: inline-block;
                padding: 20px 40px;
                font-size: 18px;
                color: white;
                background-color: #007bff;
                border-radius: 5px;
                text-decoration: none;
                text-align: center;
            }
            .download-button a:hover {
                background-color: #0056b3;
            }
            </style>
            <div class="download-button">
                <a href="data:text/csv;charset=utf-8,{csv_report}" download="report.csv">Download Report</a>
            </div>
        """, unsafe_allow_html=True)
        # st.download_button(
        #     label="Download Report",
        #     data=csv_report,
        #     file_name="report.csv",
        #     mime="text/csv"
        # )
