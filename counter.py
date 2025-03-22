import streamlit as st

st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0
st.header("counter")
col1,col2=st.columns(2)
print("count>>>",st.session_state.count)
with col1:
    if st.button('Increment'):
        st.session_state.count +=1
    
    if st.button("decrement"):
        st.session_state.count -= 1

st.write('Count = ', st.session_state.count)