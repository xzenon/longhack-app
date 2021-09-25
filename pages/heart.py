import streamlit as st
import numpy as np
import pickle
import time

def write():
    with st.spinner("Loading..."):
        st.title("Heart Disease")
        st.subheader("Fill the following values to predict whether the patient has heart disease or not")
        st.markdown(
            """
            Prediction model is based on dataset from the UCI ML Repository - [Heart Disease Data Set](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)
            """,
            unsafe_allow_html=True)

        # prepare input values
        # gender
        gender_choices = {0: "Female", 1: "Male"}
        def gender_choices_format(option):
            return gender_choices[option]

        # chest pain type
        cp_choices = {0: "Typical angina", 1: "Atypical angina", 2: "Non-anginal pain", 3: "Asymptomatic"}
        def cp_choices_format(option):
            return cp_choices[option]

        # fasting blood sugar
        fbs_choices = {0: "No", 1: "Yes"}
        def fbs_choices_format(option):
            return fbs_choices[option]

        # chest pain type
        restecg_choices = {0: "Normal", 1: "ST-T wave abnormality (T wave inversions and/or ST elevation or depression > 0.05 mV)", 2: "Showing probable or definite left ventricular hypertrophy by Estes' criteria"}
        def restecg_choices_format(option):
            return restecg_choices[option]

        # exercise induced angina
        exang_choices = {0: "No", 1: "Yes"}
        def exang_choices_format(option):
            return exang_choices[option]

        # the slope of the peak exercise ST segment
        slp_choices = {0: "Upsloping", 1: "Flat", 2: "Downsloping"}
        def slp_choices_format(option):
            return slp_choices[option]

        # thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
        thal_choices = {1: "Normal", 2: "Fixed defect", 3: "Reversable defect"}
        def thal_choices_format(option):
            return thal_choices[option]

        # build the input form
        with st.form("values_form"):
            gender_value = st.selectbox("Gender", options=list(gender_choices.keys()), format_func=gender_choices_format)
            age_value = st.slider("Age", value=25, min_value=16, max_value=90)
            cp_value = st.selectbox("Chest pain type", options=list(cp_choices.keys()), format_func=cp_choices_format)
            trestbps_value = st.number_input("Resting blood pressure (in mm Hg on admission to the hospital)", value=120, min_value=10, max_value=300, step=1)
            chol_value = st.number_input("Serum cholesterol (in mg/dl)", value=175, min_value=1, max_value=1000, step=1)
            fbs_value = st.selectbox("Is fasting blood sugar > 120 mg/dl?", options=list(fbs_choices.keys()), format_func=fbs_choices_format)
            restecg_value = st.selectbox("Resting electrocardiographic results", options=list(restecg_choices.keys()), format_func=restecg_choices_format)
            thalach_value = st.number_input("Maximum heart rate achieved", value=175, min_value=1, max_value=500, step=1)
            exang_value = st.selectbox("Exercise induced angina", options=list(exang_choices.keys()), format_func=exang_choices_format)
            oldpeak_value = st.number_input("ST depression induced by exercise relative to rest", value=1.5, min_value=0.0, max_value=5.0, step=0.1)
            slp_value = st.selectbox("The slope of the peak exercise ST segment", options=list(slp_choices.keys()), format_func=slp_choices_format)
            ca_value = st.slider("Number of major vessels (0-3) colored by flourosopy", value=1, min_value=0, max_value=3)
            thal_value = st.selectbox("Thal value", options=list(thal_choices.keys()), format_func=thal_choices_format)

            is_submitted = st.form_submit_button("Submit patient data")

            # process submitted data
            if is_submitted:
                with st.spinner(text="Please wait"):
                    # get the inputs, convert to float, and store in a list
                    submitted_values = [age_value, gender_value, cp_value, trestbps_value, chol_value, fbs_value, restecg_value,
                                        thalach_value, exang_value, oldpeak_value, slp_value, ca_value, thal_value]
                    features_list = [float(i) for i in submitted_values]

                    # converting the list to an array, reshaping into a 2D array
                    features_array = np.array(features_list)
                    features_array = features_array.reshape(-1, len(features_array))

                    # open the pickle file in the read mode
                    clf = pickle.load(open("pages/models/heart_disease_logistic_reg.pkl", "rb"))
                    # make predictions on our new test data
                    prediction = clf.predict(features_array)

                    # show prediction results
                    time.sleep(2)
                    if prediction[0] == 1:
                        st.error("This patient has heart disease.")
                    else:
                        st.success("This patient does not have heart disease.")

                    with st.expander("Details"):
                        st.write("Prediction score:", prediction[0])
                        #st.write("Features list:", features_list)

                    # print("Features list:", features_list)
                    # print("Prediction score:", prediction[0])