import streamlit as st

st.title("👨‍🦱 About")
st.header('Our core team', divider=True)
our_team = """
- Muhammad Rizqi = Project Manager, Project Initiator (who manage and own apps)
- Raihan Muhammad Rif'at = Database Engineer (who create and handle database, we still search free alternative)
- Nuzulul Barkah Rifai = System Analyst (who create how and why each element works, new feature it's responsible)
- Muhammad Habid Ali = Fullstack Dev (who help me code and create UI)
"""
st.markdown(our_team)

st.header('Reason', divider=True)
reason = '''
We made this app to finish our last project on software development and help ms. Wiga to make app for athletes.
'''
st.markdown(reason)

st.header('Contributors', divider=True)
contributors_html = """
[![contributors](https://contrib.rocks/image?repo=Kingki19/Open-SIA-for-Performance-Tracker-for-Athletes)](https://github.com/Kingki19/Open-SIA-for-Performance-Tracker-for-Athletes/graphs/contributors)
"""
st.markdown(contributors_html)
