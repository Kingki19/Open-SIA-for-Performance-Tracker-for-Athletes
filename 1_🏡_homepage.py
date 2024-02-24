import streamlit as st

st.title('Open SIA (System Information Apps) Performance Tracker for Athletes')

data_profil_col, input_col, gambar_lokasi_sentra_col = st.columns(3)
fasilitas_col, preview_kegiatan_col, monitoring_evaluation_col = st.columns(3)

def create_container_in_column(col, image_link, label_button):
  with col:
    with st.container(border=True):
      st.image(image_link)
      st.button(label=label_button, use_container_width=True)

# with data_profil_col:
#   with st.container(border=True):
#     st.image('https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')
#     st.write('Tekan ini untuk masuk ke data profil')

create_container_in_column(data_profil_col, 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'data_profil')
create_container_in_column(input_col, 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'input')
create_container_in_column(gambar_lokasi_sentra_col, 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'gambar_lokasi_sentra')
create_container_in_column(fasilitas_col, 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'fasilitas')
create_container_in_column(preview_kegiatan_col, 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'preview_kegiatan')
create_container_in_column(monitoring_evaluation_col, 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'monitoring_evaluation')


st.caption('it just a prototype, made to finish final project of software development course')
