import streamlit as st
import time



st.title('Streamlit 超入門')

st.write('プログレスバーの表示\nSTART!!')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

left_columu, right_columu = st.columns(2)

button = left_columu.button('右カラムにボタンを追加')
if button:
    right_columu.write('ここは右カラム')

expander = st.expander('お問合せ')
expander.write('お問合せ内容をかく')