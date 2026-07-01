from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load trained model and encoders
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "Models", "loan_model.pkl"))
encoders = joblib.load(os.path.join(BASE_DIR, "Models", "encoders.pkl"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        gender = request.form["Gender"]
        married = request.form["Married"]
        dependents = request.form["Dependents"]
        education = request.form["Education"]
        self_employed = request.form["Self_Employed"]

        applicant_income = float(request.form["ApplicantIncome"])
        coapplicant_income = float(request.form["CoapplicantIncome"])
        loan_amount = float(request.form["LoanAmount"])
        loan_term = float(request.form["Loan_Amount_Term"])
        credit_history = float(request.form["Credit_History"])
        property_area = request.form["Property_Area"]

        # Encode categorical values
        gender = encoders["Gender"].transform([gender])[0]
        married = encoders["Married"].transform([married])[0]
        dependents = encoders["Dependents"].transform([dependents])[0]
        education = encoders["Education"].transform([education])[0]
        self_employed = encoders["Self_Employed"].transform([self_employed])[0]
        property_area = encoders["Property_Area"].transform([property_area])[0]

        input_data = pd.DataFrame([[
            gender,
            married,
            dependents,
            education,
            self_employed,
            applicant_income,
            coapplicant_income,
            loan_amount,
            loan_term,
            credit_history,
            property_area
        ]], columns=[
            "Gender",
            "Married",
            "Dependents",
            "Education",
            "Self_Employed",
            "ApplicantIncome",
            "CoapplicantIncome",
            "LoanAmount",
            "Loan_Amount_Term",
            "Credit_History",
            "Property_Area"
        ])

        prediction = model.predict(input_data)[0]

        if prediction == 1:
            result = "Loan Approved ✅"
        else:
            result = "Loan Rejected ❌"

        return render_template("result.html", result=result)

    return render_template("predict.html")


if __name__ == "__main__":
    app.run(debug=True)