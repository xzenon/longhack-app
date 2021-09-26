import streamlit as st
import awesome_streamlit as ast
import pages.info
import pages.liver
import pages.heart
import pages.drugs

PAGES = {
    "Liver disease prediction": pages.liver,
    "Heart disease prediction": pages.heart,
    "Compounds database": pages.drugs,
    "Information": pages.info
}

def main():
    st.set_page_config(page_title = "LongHack | Disease prediction")
    st.sidebar.markdown(
        """
        [<img src="https://static.tildacdn.com/tild6334-3635-4661-b233-373839373665/Longhack_big_lime1.svg?raw=true" style="max-width: 170px">](https://longhack.org/)
        """,
        unsafe_allow_html=True)
    #st.sidebar.title("Navigation")
    selection = st.sidebar.radio("", list(PAGES.keys()))

    page = PAGES[selection]
    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)

    st.sidebar.title("")
    st.sidebar.info(
        """
        This app is built during **Longevity Hackathon** event by **Ageless Partners** team. Learn more at
        [longhack.org](https://longhack.org/).
        """
    )

if __name__ == "__main__":
    main()