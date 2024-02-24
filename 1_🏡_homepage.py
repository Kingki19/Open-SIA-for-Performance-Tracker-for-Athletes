import streamlit as st

st.title('Open SIA (System Information Apps) Performance Tracker for Athletes')

data_profil_col, input_col, gambar_lokasi_sentra_col = st.columns(3)
fasilitas_col, preview_kegiatan_col, monitoring_evaluation_col = st.columns(3)

with data_profil_col:
  with st.container(border=True):
    st.image('https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')
    st.write('Tekan ini untuk masuk ke data profil')

st.caption('it just a prototype, made to finish final project of software development course')
