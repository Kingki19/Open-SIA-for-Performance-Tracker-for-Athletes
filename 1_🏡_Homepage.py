import streamlit as st

logo_col, title_col = st.columns([1, 4])

with logo_col:
    link_logo = 'https://static.vecteezy.com/system/resources/previews/009/096/945/original/monitor-screen-computer-with-football-sports-illustration-logo-design-vector.jpg'
    st.image(link_logo)

university = 'UNNES'
with title_col:
    st.title(f'Open SIA (System Information Apps) Performance Tracker for Athletes - {university}')

# Function to create container in column that contain button to move to another pages
def create_container_in_column(col, label_button, label_explanation):
    '''
    params:
    col: column to be used
    label_button: name to label button
    label_explanation: give explanation for related label
    '''
    with col:
        with st.container(border=True):
            if st.button(label=label_button, use_container_width=True):
                return True
            with st.expander("See explanation:"):
                st.write(label_explanation)

profile_data_col, input_data_col, image_center_location_col = st.columns(3)
facilities_col, activities_preview_col, monitoring_evaluation_col = st.columns(3)

# Homepage
if create_container_in_column(profile_data_col, '👤 profiles data', 'Contain profiles data from athletes, coaches, and others'):
  st.switch_page("pages/3_👥_Profiles Data.py")
if create_container_in_column(input_data_col, '🗃️ input data', 'Input athlete performance data every day here'):
  st.switch_page("pages/4_🗃️_Input Data.py")
if create_container_in_column(image_center_location_col, '🗺️ image of center location', 'I don\'t know what is this'):
  st.switch_page("pages/5_🗺️_Image of Center Location.py")
if create_container_in_column(facilities_col, '⛳ facilities', 'facilities provided by the relevant training site (university)'):
  st.switch_page("pages/6_⛳_Facilities.py")
if create_container_in_column(activities_preview_col, '⌛ activities preview', 'Plan of activities to be implemented'):
  st.switch_page("pages/7_⌛_Activities Preview.py")
if create_container_in_column(monitoring_evaluation_col, '🖥️ monitoring evaluation', 'Monitor athletes\'s performance based on their daily data and competition results'):
  st.switch_page("pages/8_🖥️_Monitoring Evaluation.py")

st.caption('it just a prototype, made to finish final project of software development course')
