import streamlit as st

# Title
st.title('My Streamlit App')

# Header
st.header('Welcome!')

# Text
st.text('This is a simple Streamlit app.')

# Sidebar
st.sidebar.title('Sidebar')
st.sidebar.text('This is the sidebar.')

# Button
if st.button('Click me'):
    st.write('Button clicked!')

# Checkbox
checkbox = st.checkbox('Check me')
if checkbox:
    st.write('Checkbox checked!')

# Selectbox
option = st.selectbox('Choose an option', ['Option 1', 'Option 2', 'Option 3'])
st.write('You selected:', option)

# Slider
number = st.slider('Select a number', 0, 10, 5)
st.write('Selected number:', number)
