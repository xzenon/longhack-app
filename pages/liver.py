import streamlit as st
import numpy as np
import pickle
import time

def write():
    with st.spinner("Loading..."):
        st.title("Liver Disease")
        st.subheader("Fill the following values to predict whether the patient has liver disease or not")
        st.markdown(
            """
            Prediction model is based on dataset from the UCI ML Repository - [ILPD (Indian Liver Patient Dataset)](https://archive.ics.uci.edu/ml/datasets/ILPD+%28Indian+Liver+Patient+Dataset%29)
            """,
            unsafe_allow_html=True)

        # prepare input values
        # gender
        gender_choices = {0: "Female", 1: "Male"}
        def gender_choices_format(option):
            return gender_choices[option]

        # build the input form
        with st.form("values_form"):
            #gender_value = st.selectbox("Gender", ["Male", "Female"])
            gender_value = st.selectbox("Gender", options=list(gender_choices.keys()), format_func=gender_choices_format)
            age_value = st.slider("Age", value=25, min_value=16, max_value=90)
            tb_value = st.number_input("Total Bilirubin (Normal: 0.1 - 1.4 mg/dL)", value=1.0, min_value=0.0,
                                       max_value=10.0, step=0.1)
            db_value = st.number_input("Direct Bilirubin (Normal: 0.0 - 0.4 mg/dL)", value=1.0, min_value=0.0, max_value=10.0,
                                       step=0.1)
            alkphos_value = st.number_input("Alkaline Phosphatase (Normal: 20 - 140 IU/L)", value=100, min_value=1,
                                            max_value=10000, step=1)
            sgpt_value = st.number_input("Alanine Aminotransferase (Normal: 7 - 55 U/L)", value=20, min_value=1,
                                         max_value=10000, step=1)
            sgot_value = st.number_input("Aspartate Aminotransferase (Normal for male: 8 - 40 IU/L, female: 6 - 34 IU/L)",
                                         value=10, min_value=1, max_value=10000, step=1)
            tp_value = st.number_input("Total Protiens (Normal: 5.5 - 9.0 g/dL)", value=7.0, min_value=0.0, max_value=20.0,
                                       step=0.1)
            alb_value = st.number_input("Albumin (Normal: 3.5 - 5.5 g/dL)", value=4.0, min_value=0.0, max_value=10.0, step=0.1)
            agratio_value = st.number_input("Albumin and Globulin Ratio (A/G)", value=1.1, min_value=0.1, max_value=5.0,
                                            step=0.1)
            is_submitted = st.form_submit_button("Submit patient data")

            # process submitted data
            if is_submitted:
                with st.spinner(text="Please wait"):
                    # get the inputs, convert to float, and store in a list
                    #numeric_gender_value = 1 if gender_value == "Male" else 0
                    submitted_values = [age_value, tb_value, db_value, alkphos_value, sgpt_value, sgot_value, tp_value,
                                        alb_value, agratio_value, gender_value]
                    features_list = [float(i) for i in submitted_values]

                    # converting the list to an array, reshaping into a 2D array
                    features_array = np.array(features_list)
                    features_array = features_array.reshape(-1, len(features_array))

                    # open the pickle file in the read mode
                    clf = pickle.load(open("pages/models/liver_disease_logistic_reg.pkl", "rb"))
                    # make predictions on our new test data
                    prediction = clf.predict(features_array)

                    # show prediction results
                    time.sleep(2)
                    if prediction[0] == 1:
                        st.error("This patient has liver disease.")
                    else:
                        st.success("This patient does not have liver disease.")

                    with st.expander("Details"):
                        st.write("Prediction score:", prediction[0])
                        #st.write("Features list:", features_list)

                    #print("Features list:", features_list)
                    #print("Prediction score:", prediction)