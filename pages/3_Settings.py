import streamlit as st
st.set_page_config(layout="wide")
st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://upload.wikimedia.org/wikipedia/commons/1/15/Deloitte_Logo.png);
                background-repeat: no-repeat;
                padding-top: 20px;
                background-position: 30px 40px;
                width : 200px;
                background-size: 150px 60px;
                
            }
            section[data-testid="stSidebar"] {
                width: 200px !important; 
                min-width: 200px;
                background-color : #FAFAFB;
                
            }
            
            [data-testid="stSidebarContent"]{
                width:200px;
                
            }
            
            [data-testid="block-container"]{
                padding-left : 2rem;
                padding-right : 2rem;
            }

            [data-testid="baseButton-secondary"]{
                border-radius : 5px;
                color : white;
                background-color :green;
                font-family : Manrope;
                width : 100px;
                font-weight : bold;
                margin-top : 10px;
            }

            [data-testid="stImage"]{
                height : 100px;
                width : 100px;
                margin-bottom :-40px;
            }
            [data-testid="stVerticalBlock"]{
                gap:0rem;
            }
            [data-testid="stTextArea"]{
                margin-top : 10px;
                margin-bottom : 10px;
            }

            [data-testid="stWidgetLabel"]{
                min-height : 1rem;
            }
            
            [data-testid="stCodeBlock"] .st-emotion-cache-1hskohh{
                height : 400px;
            }
            [data-testid="stVerticalBlockBorderWrapper"]{
                height : 270px;
                width : 800px;
                margin-left : 50px;
                padding : 20px;
            }
            [data-testid="element-container"]{
                margin-bottom : 20px;
            }
            .st-emotion-cache-nziaof{
                background-color : #FAFAFB;
                color : #F5F1FE;
            }
            .st-emotion-cache-pkbazv{
                color : #6D31ED;

            }
            
            .Header{
                margin-top : -70px;
                font-size : 48px;
                margin-left : 0px;
                padding-bottom : 30px;
                font-family : Lexend;
            }

            
            .st-cq{
                background-color : #F3F4F6;
            }
            

            .h1{
                color : yellow;
                font-size : 15px;
            }

            .container{
                background-color :black;
            }
        </style>
        
        """,
        unsafe_allow_html=True,
    )

container = st.container(border=True)
with container:
    st.title("Access Token")
    api_key = st.text_input("What's your API key?",type="password")
    st.warning("Make sure to never post your tokens publicly!")
    Save_Button = st.button("Save")
    if Save_Button:
        if api_key:
            st.success("API Key Added Successfully")
        else:
            st.error("Please Enter API Key")
    
       
