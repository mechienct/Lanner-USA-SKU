import streamlit as st

st.subheader("Lanner USA config text to SKU number2")
user_input = st.empty()
default_value = " "

user_input = st.text_input("Enter your config text and Press \"Enter\": ", default_value)
if st.button('reset textarea'):
    default_value = " " 
if user_input:
  subtxt = user_input.split(':')
  op =  subtxt[0].split(' - ')[1].split(' ')[0]
  for i in range(1,len(subtxt),1):
    op += '-'
    op += subtxt[i].split('-')[0].strip().split(' ')[0]
  st.text("SKU number: ")
  st.text(op)
