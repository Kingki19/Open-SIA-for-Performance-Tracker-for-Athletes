import streamlit as st

university = 'UNNES'
st.title(f'Open SIA (System Information Apps) Performance Tracker for Athletes - {university}')

profile_data_col, input__data_col, image_center_location_col = st.columns(3)
facilities_col, activities_preview_col, monitoring_evaluation_col = st.columns(3)

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
      st.button(label=label_button, use_container_width=True)
      with st.expander("See explanation:"):
        st.write(label_explanation)
        
    
create_container_in_column(profile_data_col, 'profiles data', 'Contain profiles data from athletes, coaches, and others')
create_container_in_column(input__data_col, 'input data', 'Input athlete performance data every day here')
create_container_in_column(image_center_location_col, 'image of center location', 'I don\'t know what is this')
create_container_in_column(facilities_col, 'facilities', 'facilities provided by the relevant training site (university)')
create_container_in_column(activities_preview_col, 'activities preview', 'Plan of activities to be implemented')
create_container_in_column(monitoring_evaluation_col, 'monitoring evaluation', 'Monitor athletes\'s performance based on their daily data and competition results')


st.caption('it just a prototype, made to finish final project of software development course')
