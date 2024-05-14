import streamlit as st
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
