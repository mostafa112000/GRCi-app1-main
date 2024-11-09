import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
import json
import requests


cred = credentials.Certificate("grci-app1-3771d455d2f5.json")

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
        
            if 'username' not in st.session_state:
                st.session_state.username = ''
            if 'useremail' not in st.session_state:
                st.session_state.useremail = ''


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
                    try:
                        return r.json()['email']
                    except:
                        st.warning(r.json())
                except Exception as e:
                    st.warning(f'Signup failed: {e}')

            def sign_in_with_email_and_password(email=None, password=None, return_secure_token=True):
                rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

                try:
                    payload = {
                        "returnSecureToken": return_secure_token
                    }
                    if email:
                        payload["email"] = email
                    if password:
                        payload["password"] = password
                    payload = json.dumps(payload)
                    print('payload sigin',payload)
                    r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
                    try:
                        data = r.json()
                        user_info = {
                            'email': data['email'],
                            'username': data.get('displayName')  # Retrieve username if available
                        }
                        return user_info
                    except:
                        st.warning(data)
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
                    if r.status_code == 200:
                        return True, "Reset email Sent"
                    else:
                        # Handle error response
                        error_message = r.json().get('error', {}).get('message')
                        return False, error_message
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
                        
                        st.success('Account created successfully!')
                        st.markdown('Please Login using your email and password')
                        st.balloons()
                else:
                    # st.button('Login', on_click=f)          
                    st.button('Login', on_click=f)
                    # if st.button('Forget'):
                    
                    # st.button('Forget',on_click=forget)

                    
                    
            if st.session_state.signout:
                    with st.sidebar:
                        app = option_menu(
                            menu_title='GRCi ',
                            options=['Home','Account','About','Pioneer'],
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
                        st.text('Name: '+st.session_state.username)
                        st.text('Email id: '+st.session_state.useremail)
                    if app == 'About':
                        about.app()    
                    if app=='Pioneer':
                        pioneer.app()                  
                        
                        
                            
                            
            

                                    
            def ap():
                st.write('Posts')                    
  
             
          
             
    run()            
         