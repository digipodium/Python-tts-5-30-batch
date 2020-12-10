import streamlit as st

## components in streamlit are UI elements that we need
# text > st.title, st.header. st.subheader, st.text, st.write, st.success
# input > st.text_input, st.date_input, st.number_input
# slider > st.slider, st.text_slider
# dropdown > st.selectbox
# button > st.button
# fileuploader > st.fileuploader
# radio button, checkbox > st.checkbox, st.radio
# all of them can be used with st.component style code
# and u can put stuff in sidebar with st.sidebar.component
# like st.sidebar.button

st.title('Components example')
st.header("Heading")
st.subheader("SubHeading")
st.markdown('''
    - one
    - two
    - three :sunglasses:
''')
st.text('text simple')
st.success('text success')
st.error('text error')
st.warning('text warning')
st.write(len) # intelligent output

st.title('user input component')
name = st.text_input('enter name',)
iq = st.number_input('enter IQ value',)
bday = st.date_input('enter your bday')
fav_icecream = st.selectbox('select ur flavor',
                            ['vanilla','chocolate','strawberry'])
ischeck = st.checkbox('click here do check this box')
choice = st.radio('what do u like',['movies','games','reading'])
pxsize = st.slider('select a size of pixel',min_value=10,max_value=100,value=35)
color = st.select_slider('select a color',['red','green','blue','yellow','purple'])
file = st.file_uploader('upload file')
clicked = st.button('are you done ?')

