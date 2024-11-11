import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
import json
import requests


cred = credentials.Certificate("grci-app1-3771d455d2f5.json")

from streamlit_option_menu import option_menu


import home, account, chart, pioneer
st.set_page_config(
        page_title="GRCi", page_icon="logo.png", layout="wide"
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
        
            if 'username' not in st.session_state:
                st.session_state.username = ''
            if 'useremail' not in st.session_state:
                st.session_state.useremail = ''


            def get_friendly_error_message(error_code):
                error_messages = {
                    "MISSING_EMAIL": "Please enter your email address.",
                    "EMAIL_EXISTS": "This email is already in use. Please try a different one or sign in.",
                    "INVALID_PASSWORD": "The password you entered is incorrect. Please try again.",
                    "EMAIL_NOT_FOUND": "No account found with this email. Please check your email or sign up.",
                    "USER_DISABLED": "This account has been disabled. Please contact support.",
                    # Add more error codes and messages as needed
                }
                return error_messages.get(error_code, "An unexpected error occurred. Please try again.")

            def sign_up_with_email_and_password(email, password, username=None, return_secure_token=True):
                try:
                    rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
                    payload = {
                        "email": email,
                        "password": password,
                        "returnSecureToken": return_secure_token
                    }
                    if username:
                        payload["displayName"] = username
                    payload = json.dumps(payload)
                    r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
                    response_data = r.json()
                    
                    if "error" in response_data:
                        error_code = response_data["error"]["message"]
                        st.warning(get_friendly_error_message(error_code))
                    else:
                        return response_data['email']
                except Exception as e:
                    st.warning(f'Signup failed: {e}')

            def sign_in_with_email_and_password(email=None, password=None, return_secure_token=True):
                rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
                try:
                    payload = {
                        "email": email,
                        "password": password,
                        "returnSecureToken": return_secure_token
                    }
                    payload = json.dumps(payload)
                    r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
                    response_data = r.json()
                    
                    if "error" in response_data:
                        error_code = response_data["error"]["message"]
                        st.warning(get_friendly_error_message(error_code))
                    else:
                        return {
                            'email': response_data['email'],
                            'username': response_data.get('displayName')
                        }
                except Exception as e:
                    st.warning(f'Signin failed: {e}')

            def reset_password(email):
                try:
                    rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode"
                    payload = {
                        "email": email,
                        "requestType": "PASSWORD_RESET"
                    }
                    payload = json.dumps(payload)
                    r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
                    response_data = r.json()
                    
                    if r.status_code == 200:
                        return True, "A password reset email has been sent."
                    else:
                        error_code = response_data.get('error', {}).get('message')
                        return False, get_friendly_error_message(error_code)
                except Exception as e:
                    return False, str(e)


            # Example usage
            # email = "example@example.com"
                

            def f(): 
                try:
                    # user = auth.get_user_by_email(email)
                    # print(user.uid)
                    # st.session_state.username = user.uid
                    # st.session_state.useremail = user.email

                    userinfo = sign_in_with_email_and_password(st.session_state.email_input,st.session_state.password_input)
                    st.session_state.username = userinfo['username']
                    st.session_state.useremail = userinfo['email']

                    
                    global Usernm
                    Usernm=(userinfo['username'])
                    
                    st.session_state.signedout = True
                    st.session_state.signout = True    
        
                    
                except: 
                    st.warning('Login Failed')

            def t():
                st.session_state.signout = False
                st.session_state.signedout = False   
                st.session_state.username = ''



                
            
                
            if "signedout"  not in st.session_state:
                st.session_state["signedout"] = False
            if 'signout' not in st.session_state:
                st.session_state['signout'] = False    
                

                
            
            if  not st.session_state["signedout"]: # only show if the state is False, hence the button has never been clicked
                st.header('*`Login to continue`*')
                with st.sidebar:    
                    choice = st.selectbox('Login/Signup',['Login','Sign up'])
                    email = st.text_input('Email Address')
                    password = st.text_input('Password',type='password')
                    st.session_state.email_input = email
                    st.session_state.password_input = password

                    

                    
                    if choice == 'Sign up':
                        username = st.text_input("Enter  your unique username")
                        
                        if st.button('Create my account'):
                            # user = auth.create_user(email = email, password = password,uid=username)
                            user = sign_up_with_email_and_password(email=email,password=password,username=username)
                            if user:
                                st.success('Account created successfully!')
                                st.markdown('Please Login using your email and password')
                                st.balloons()
                            
                            else:
                                st.warning('''Account not created! check your data
                                           note: password lenght should be 6 characters or more
                                           ''')
                    else:
                        # st.button('Login', on_click=f)          
                        st.button('Login', on_click=f)
                        # if st.button('Forget'):
                        
                        # st.button('Forget',on_click=forget)

                        
                        
            if st.session_state.signout:
                    with st.sidebar:
                        app = option_menu(
                            menu_title='GRCi ',
                            options=['Home','Account','Chart','Pioneer'],
                            icons=['house-fill','person-circle','info-circle-fill','chat-fill'],
                            menu_icon='chat-text-fill',
                            default_index=0,
                            styles={
                                "container": {"padding": "5!important","background-color":'black'},
                                "icon": {"color": "white", "font-size": "23px"}, 
                                "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                                "nav-link-selected": {"background-color": "#02ab21"},}
                            
                            )

                        st.button('Sign out', on_click=t) 
                        
                    if app == "Home":
                        home.app()
                        
                    if app == "Account":
                        account.app() 
                        
                    if app == 'Chart':
                        chart.app()   
                         
                    if app=='Pioneer':
                        pioneer.app()                  
                        
                        
                            
                            
            

                                    
            def ap():
                st.write('Posts')                    
  
             
          
             
    run()            
         