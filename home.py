import json
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
#import requests  # pip install requests

    # GitHub: https://github.com/andfanilo/streamlit-lottie
    # Lottie Files: https://lottiefiles.com/


def app():
    with st.container():
        st.title("Welcome to `GRCi` ⚡")
        #st.write('######') 
        
    with st.container():
        #st.write('---')
        left_column,right_column = st.columns((3,2))
        with left_column:
            #st.write('######')   
            st.header('Your Integrated Solution for Governance, Risk and Compliance')   
            st.write('######')  
            st.text('Empower your organization with seamless enterprise risk management, compliance, and cyber resilience through AI-driven insights and real-time dashboards.')   
            st.write('######')  
            #st.button('Request a demo')   
            
            
            
        with right_column:
            def load_lottiefile(filepath: str):
                with open(filepath, "r") as f:
                    return json.load(f)        

            lottie_coding = load_lottiefile("lottiefile.json")  # replace link to local lottie file
            
            #def load_lottieurl(url: str):
            #    r = requests.get(url)
            #    if r.status_code != 200:
            #        return None
            #    return r.json()    
            #lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")

            st_lottie(
                lottie_coding , #lottie_hello
                speed=1,
                reverse=False,
                loop=True,
                quality="low", # medium ; high
                height=None,
                width=None,
                key=None,
            )
            
    with st.container():
        st.write('---')
        st.write('######')  
        left_column,center_column,right_column = st.columns((2,2,3))        
        with left_column:
            #st.write('######')   
            st.subheader('Enterprise Risk Management')   
            st.write('######')  
            st.text('ERM helps organizations identify, assess, and manage risks across all departments in real time. It offers a holistic view of risks, using customizable dashboards, and integrates external data to detect emerging threats.')   
            st.write('######') 
             
        with center_column:
            #st.write('######')   
            st.subheader('Business Continuity Management')   
            st.write('######')  
            st.text('BCM ensures operational resilience by helping organizations prepare for and recover from disruptions like natural disasters or cyber-attacks. It automates incident management and recovery workflows.')   
            st.write('######')  
                      
        with right_column:
            st.subheader('PioNeer+ (GRC Artificial Intelligence)')   
            st.write('######')  
            st.text('Meet PioNeer+, the AI-powered engine at the core of GRCi. PioNeer+ enhances all GRCi modules by providing intelligent risk analysis, automated decision support, and predictive analytics. This advanced AI model is designed to help organizations assess risks, predict future incidents, and recommend proactive actions, all based on real-time data and historical trends.')   
            st.write('######')             
 
    
    with st.container():  
        left_column,center_column,right_column = st.columns((3))        
        with right_column:
            #st.write('######')   
            st.subheader('Governance')   
            st.write('######')  
            st.text('Streamline governance processes to improve decision-making and ensure compliance with regulatory and ethical standards. This module helps manage policies, documentation, and workflows.')   
            st.write('######') 
             
        with left_column:
            #st.write('######')   
            st.subheader('Internal Audit')   
            st.write('######')  
            st.text('Automate and optimize internal audits with risk-based planning, execution, and reporting. The module ensures efficient audit processes across departments.')   
            st.write('######')            
            
        with center_column:
            st.subheader('Compliance Management')   
            st.write('######')  
            st.text('This module automates regulatory compliance processes, ensuring adherence to global and industry regulations. It tracks changes, assesses compliance risks, and generates reports.')   
            st.write('######') 
                         
            
            
    # Use local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/style.css")            
    with st.container():
        st.write('---')
        st.header("Get In Touch With Us!")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/mostafagaber112000@gmail.COM" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()