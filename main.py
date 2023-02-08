import streamlit as st
import time

st.title("Streamlit 超入門")

st.write("Show Progress Bar")
"Start"

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.001)

"Done"
    
left_column, right_column=st.beta_columns(2)
button=left_column.button("右カラム")
if button:
    right_column.write("ここは右カラム")

expander1=st.beta_expander("問い合わせ1")
expander1.write("問い合わせ1")
expander2=st.beta_expander("問い合わせ2")
expander2.write("問い合わせ2")
