import streamlit as st
st.markdown('<style>background-color : black;</style>', unsafe_allow_html=True)
#st.sidebar.image("data:image/png;base64,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")

#from streamlit_extras.app_logo import add_logo

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
            .st-aw{
                background-color : #6D31ED;
            }
            [data-testid="block-container"]{
                padding-left : 2rem;
                padding-right : 2rem;
            }

            [data-testid="baseButton-secondary"]{
                border-radius : 5px;
                color : #6D31ED;
                background-color :#F5F1FE;
                font-family : Manrope;
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
