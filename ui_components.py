import streamlit as st

def render_sidebar(history):
    st.sidebar.title("Request History")
    if not history:
        st.sidebar.write("No history.")
    for item in history:
        st.sidebar.text(f"[{item['method']}] {item['status']}\n{item['url'][:30]}...")

def render_response_section(response, error):
    st.subheader("Response Data")
    if error:
        st.error(f"Failed: {error}")
        return
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Status", response.status_code)
    c2.metric("Time", f"{response.elapsed.total_seconds():.2f}s")
    c3.metric("Size", f"{len(response.content)} B")
    
    st.text("Headers:")
    st.json(dict(response.headers))
    
    st.text("Body:")
    try:
        st.json(response.json())
    except ValueError:
        st.text(response.text)