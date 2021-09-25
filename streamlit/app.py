import streamlit as st
import awesome_streamlit as ast
import pages.info
import pages.liver
import pages.heart

PAGES = {
    "Liver disease prediction": pages.liver,
    "Heart disease prediction": pages.heart,
    "Information": pages.info
}

def main():
    st.set_page_config(page_title = "LongHack | Disease prediction")
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app is built during **Longevity Hackathon** event by **Ageless Partners** team. Learn more at
        [longhack.org](https://longhack.org/).
        """
    )

if __name__ == "__main__":
    main()