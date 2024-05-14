import streamlit as st
from Xml_Generation import myfunc,get_file_name
from code_editor import code_editor
st.secrets[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]

st.set_page_config(layout="wide")

if 'data' not in st.session_state:
    st.session_state['data'] = []

if 'theme' not in st.session_state:
    st.session_state['theme'] = []

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

            .st-emotion-cache-nziaof{
                background-color : #FAFAFB;
                color : #F5F1FE;
            }
            .st-emotion-cache-pkbazv{
                color : #6D31ED;

            }
            [data-testid="stText"] {
                margin-left : 250px;
                font-size :20px;
                color :#6F7787;
                font-family : lexend;
                
                

            }
            
            .Header{
                margin-top : -70px;
                font-size : 20px;
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
            .st-emotion-cache-1hskohh e1ycw9pz3{
                background-color:#F3F4F6;

            }
            .ace_editor ace_hidpi ace-streamlit-light{
                height : 300px;
            }
        </style>
        <body>
            <div class="Header">
                <h1>GenX++ D365 Finance and Operation Element Generator ..</h1>
            </div>
        </body>
        """,
        unsafe_allow_html=True,
    )


col1, col2 = st.columns([2,3]) 

with col1:
    st.write("Sample Prompt")
    sub_container = st.container(border=True)
    with sub_container:
        sub_col1, sub_col2 = st.columns([1,3])
        with sub_col1:
            st.image("image (1).png")
        with sub_col2:
            st.markdown("" + "Generate F&O table Creation XML")
            st.markdown(""+ "Table name : 'Customer' ,")
            st.markdown(""+ "Fields : 'Name , Age , Place '")


    object_to_create = st.radio( " ",
        ('Table', 'Form', 'EDT'),
        horizontal=True)

    Left_Container = st.container()
    with Left_Container:
        User_Input = st.text_area("Provide your Instruction for XML Generation :", key='input',height= 120)
        button_col1 ,button_col2 = st.columns([3,1])
        with button_col2:
            generate = st.button(label='Generate')

            

        if generate:
            data = myfunc(User_Input)
            file_name = get_file_name(data)
            st.session_state['data'] = data

            sub_container2 = st.container()
            with sub_container2:
                sub2_col1, sub2_col2 = st.columns([1,6])
                with sub2_col1:
                    st.image("image (2).png")
                with sub2_col2:
                    st.write(file_name)

            col_1 , col_2 = st.columns([1,2])
            with col_1:
                st.download_button(
                            label="Download File",
                            data=data,
                            file_name=file_name,
                            mime='text/xml',
                        )
            with col_2:
                clear = st.button(label="Clear")
with col2:
    
    Right_Container = col2.container()
    with Right_Container:
        st.text("Code Preview")
        #Code_preview = st.code(st.session_state['data'],language="xml", line_numbers=True)
        #Code_preview = st.data_editor(st.session_state['data'])
        #Code_Preview = code_editor(st.session_state['data'])

        editor_btns = [{
            "name": "Theme",
            "feather": "Moon",
            "primary": True,
            "hasText": True,
            "showWithIcon": True,
            "commands": ["submit"],
            "style": {"Top": "0.44rem", "right": "0.4rem"}
        }]
        mycode = st.session_state['data']
        if mycode:
            mycode = mycode
        else:
            mycode = "Your Output will be shown here"

        mytheme = st.session_state['theme']
        if mytheme:
            mytheme = mytheme
        else:
            mytheme = "Default"
        code_editor = code_editor(mycode,lang="XML",theme=mytheme,info="code preview",buttons=editor_btns,options={"wrap": True, "showLineNumbers": True})

        if len(code_editor['id']) != 0 and ( code_editor['type'] == "selection" or code_editor['type'] == "submit" ):
           if st.session_state['theme'] == "dark":
                st.session_state['theme'] = "Default"
           else:
                st.session_state['theme'] = "dark"




