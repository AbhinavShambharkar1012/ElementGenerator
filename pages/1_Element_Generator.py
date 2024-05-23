import streamlit as st
from Xml_Generation import myfunc,get_file_name
from code_editor import code_editor
from streamlit_option_menu import option_menu
from class_generation import myfuncclass,get_class_name
from RDP_generation import myfuncclassRDP
import json
import zipfile
import os
import base64
from io import BytesIO

st.set_page_config(layout="wide")

if 'data' not in st.session_state:
    st.session_state['data'] = []

if 'class1' not in st.session_state:
    st.session_state['class1'] = []

if 'class2' not in st.session_state:
    st.session_state['class2'] = []
    
if 'class3' not in st.session_state:
    st.session_state['class3'] = []

if 'User_Input' not in st.session_state:
    st.session_state['User_Input'] = []

if 'sample_prompt' not in st.session_state:
    st.session_state['sample_prompt'] = []

if 'theme' not in st.session_state:
    st.session_state['theme'] = []

st.markdown(
        """
        <style>
            button[kind="primary"] {
                background: none!important;
                border: none;
                padding: 0!important;
                color: black !important;
                text-decoration: none;
                cursor: pointer;
                border: none !important;
            }
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
javascript_code = """
<script>
document.getElementById("my-link").addEventListener("click", function() {
    // Execute some action when the link is clicked
    
    // You can also call Streamlit functions here using Streamlit's JavaScript API
    Streamlit.setComponentValue("Something is printed when file1Clicked is clicked!");
});
</script>
"""

col1, col2 = st.columns([2,3]) 

with col1:
    st.write("Sample Prompt")
    sub_container = st.container(border=True)
    with sub_container:
        sub_col1, sub_col2 = st.columns([1,3])
        with sub_col1:
            st.image("image (1).png")
        with sub_col2:
            st.markdown("" + "Generate F&O table")
            st.markdown(""+ "Table name : 'Customer' ,")
            st.markdown(""+ "Fields : 'Name , Age , Place '")

    #selected = option_menu("Main Menu", ["Home", 'Settings'], 
        #icons=['house', 'gear'], menu_icon="cast", default_index=1)
    
    option = st.selectbox(
    "",
    ("Select element to create","Table", "Table Extension", "EDT","SysOperations Framework Batch Job","SSRS Report using DP class"))
    #object_to_create = st.radio( " ",('Table', 'Form', 'EDT'),horizontal=True)

    
    Left_Container = st.container()
    with Left_Container:
        
        option_data = {
            'Select element to create': 'Select element to create',
            'Table': "Generate F&O table Table name : 'Customer' , Fields : 'Name , Age , Place '",
            'Table Extension': 'Create an extension of table familydata with field as myfield2',
            'EDT': 'Generate EDT with name TransfID',
            'SysOperations Framework Batch Job': 'Create sysoperation framework with naming convention AASBatchJob and parameters as transferId with EDT TransfID',
            'SSRS Report using DP class' : 'Create  classes for  ssrs report using Report data provide class  with naming convention AASReportJob and parameters as CustomerID with EDT CustId to fetch data from CustTable.The fields in custTable are AccountNum, name ,  address and custGroup the temp table used is tmpCust'
        }
     
        def update_text_area(selected_option):
            selected_data = option_data[selected_option]
            global user_Input 
            user_Input = st.text_area('Provide your Instruction for XML Generation :', selected_data, key = option, height=120)
            st.session_state['User_Input'] = user_Input
            
        if option:
            update_text_area(option) 


        button_col1 ,button_col2 = st.columns([3,1])
        with button_col2:
            generate = st.button(label='Generate')

        
        if generate:
            if option == "Select element to create":
                st.error("Please Select element to create!")
            else:
                if option == "SysOperations Framework Batch Job":
                    data = myfuncclass(st.session_state['User_Input'])
                    file_name = "myfile.zip"
                    
                    if data:
                        pass
                    else:
                        st.error("No data")
                    output_dict = json.loads(data)
                    classes = []
                    class_names = []
                    for key, value in output_dict.items():
                        classes.append(value)
                        class_names.append(key)

                    st.session_state['class1'] = classes[0]
                    st.session_state['class2'] = classes[1]
                    st.session_state['class3'] = classes[2]
                    #class_name = get_class_name(data)
                    
                    sub_container2 = st.container()
                    with sub_container2:
                        sub2_col1, sub2_col2 = st.columns([2,1])
                        with sub2_col1:
                            st.write(class_names)
                    
                    #st.write(output_dict)
                    zip_data = BytesIO()
                    with zipfile.ZipFile(zip_data, "w") as zipf:
                        for filename, content in output_dict.items():
                            # Write content to file in memory
                            file_data = BytesIO()
                            file_data.write(content.encode())
                            file_data.seek(0)
                            # Add file to zip
                            zipf.writestr(filename, file_data.read())


                    col_1 , col_2 = st.columns([1,2])
                    final_data = zip_data.getvalue()
                    #st.write(final_data)
                    with col_1:
                        st.download_button(
                                    label="Download File",
                                    data=final_data,
                                    file_name=file_name,
                                    mime='application/zip',
                                )
                    with col_2:
                        clear = st.button(label="Clear")       
                            
                elif option == "SSRS Report using DP class":
                    #/////rdp
                    data = myfuncclassRDP(st.session_state['User_Input'])
                    file_name = "myfile.xpp"
                    
                    if data:
                        pass
                    else:
                        st.error("No data")
                    output_dict = json.loads(data)
                    classes = []
                    for key, value in output_dict.items():
                        classes.append(value)

                    st.session_state['class1'] = classes[0]
                    st.session_state['class2'] = classes[1]
                    st.session_state['class3'] = classes[2]
                    class_name = get_class_name(data)
                    sub_container2 = st.container()
                    with sub_container2:
                        sub2_col1, sub2_col2 = st.columns([2,1])
                        with sub2_col1:
                            st.write(class_name)
                        
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

                else:
                    data = myfunc(st.session_state['User_Input'])
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
    if option == "SysOperations Framework Batch Job" or option == "SSRS Report using DP class":
        Right_Container1 = col2.container()
        with Right_Container1:
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
            mycode1 = st.session_state['class1']
            mycode2 = st.session_state['class2']
            mycode3 = st.session_state['class3']

            if mycode1:
                mycode1 = mycode1
            else:
                mycode1 = "Your Output class will be shown here"

            if mycode2:
                mycode2 = mycode2
            else:
                mycode2 = "Your Output class will be shown here"

            if mycode3:
                mycode3 = mycode3
            else:
                mycode3 = "Your Output class will be shown here"

            mytheme = st.session_state['theme']
            
            if mytheme:
                mytheme = mytheme
            else:
                mytheme = "Default"


            if 'secondeditor' in st.session_state:
                st.session_state.secondeditor = mycode2

            if 'thirdeditor' in st.session_state:
                st.session_state.thirdeditor = mycode3 
                

            code_editor1 = code_editor(mycode1,lang="xml",theme=mytheme,info="code preview",buttons=editor_btns,options={"wrap": True, "showLineNumbers": True})

            code_editor2 = code_editor(mycode2,lang="xml",theme=mytheme,info="code preview",buttons=editor_btns,options={"wrap": True, "showLineNumbers": True})

            code_editor3 = code_editor(mycode3,lang="xml",theme=mytheme,info="code preview",buttons=editor_btns,options={"wrap": True, "showLineNumbers": True})

            

            if len(code_editor1['id']) != 0 and ( code_editor1['type'] == "selection" or code_editor1['type'] == "submit" ):
                if st.session_state['theme'] == "dark":
                        st.session_state['theme'] = "Default"
                else:
                        st.session_state['theme'] = "dark"
        #st.write(st.session_state)
    else:
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




