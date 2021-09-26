import streamlit as st
import awesome_streamlit as ast

def write():
    with st.spinner("Loading About ..."):
        st.markdown(
            """## Information

[<img src="https://static.tildacdn.com/tild6334-3635-4661-b233-373839373665/Longhack_big_lime1.svg?raw=true" style="max-width: 150px">](https://longhack.org/)

This project is developed by **Ageless Partners** team during **Longevity Hackathon** event (24-26 September 2021) for **Biotechnology** track.

Longevity Hackathon is bringing together aging researchers, developers, and entrepreneurs to build new tools, 
raise awareness, and attract talent to the field.

Learn more about the event at [longhack.org](https://longhack.org/).

---

[<img src="https://i1.wp.com/agelesspartners.com/wp-content/uploads/2020/11/age-logo.jpg" style="max-width: 150px">](https://agelesspartners.com/)

  * [Jason C. Mercurio, MFE](https://www.linkedin.com/in/jasonmercurio/)
  * [Daniel Popoola](https://www.linkedin.com/in/daniel-popoola-984233140/)
  * [Diogo Pinto Flórido](https://www.linkedin.com/in/diogopintof/)
  * [Amruth Bhat](https://www.linkedin.com/in/amruth-bhat/)
  * [Snega R](https://www.linkedin.com/in/snega-r-2809a11a9/)
  * [Yevgen Haletskyi](https://www.linkedin.com/in/xzenon/)

## Mentors

  * [Anastasiya Giarletta](https://www.linkedin.com/in/anastasiyakgiarletta/)
  * [Sonali Khanra](https://www.linkedin.com/in/dr-sonali-khanra/)
  * [Collin Y. Ewald](https://www.linkedin.com/in/collin-ewald-b014a019/)

""",
        unsafe_allow_html=True)