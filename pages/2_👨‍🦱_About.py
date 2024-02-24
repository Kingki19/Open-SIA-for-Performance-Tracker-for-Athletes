import streamlit as st

our_team = """
- Muhammad Rizqi = Project Manager, Project Initiator (who manage and own apps)
- Raihan Muhammad Rif'at = Database Engineer (who create and handle database, we still search free alternative)
- Nuzulul Barkah Rifai = System Analyst (who create how and why each element works, new feature it's responsible)
- Muhammad Habid Ali = Fullstack Dev (who help me code and create UI)
"""
reason = '''
We made this app to finish our last project on software development and help ms. Wiga to make app for athletes.
'''

st.header('Our team', divider=True)
st.markdown(our_team)

st.header('Reason', divider=True)
st.markdown(reason)
