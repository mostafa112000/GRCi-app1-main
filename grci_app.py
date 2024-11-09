import streamlit as st

from streamlit_option_menu import option_menu


import home, account, about, pioneer
st.set_page_config(
        page_title="GRCi",
)



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, function):

        self.apps.append({
            "title": title,
            "function": function
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='GRCi ',
                options=['Home','Account','About','Pioneer'],
                icons=['house-fill','person-circle','info-circle-fill','chat-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "Account":
            account.app()    
        if app == 'About':
            about.app()    
        if app=='Pioneer':
            pioneer.app()    
             
          
             
    run()            
         