# Smart Lender - Project Documentation

## 1. Project Overview
**Smart Lender** is a machine learning-powered web application designed to predict the creditworthiness of loan applicants. The platform enables banks and financial institutions to make faster, data-driven loan approval decisions, reducing manual overhead and non-performing assets.

### Team Members
*   **Team Lead:** Tejaswini Maddireddy
*   **Team Members:** Lahari Lakkireddy, Pavan Kumar Reddy

### Skills & Tech Stack
*   **Core Language:** Python
*   **Web Framework:** Flask (HTML/CSS Frontend)
*   **Data Processing:** Pandas, NumPy, SciPy
*   **Data Visualization:** Matplotlib, Seaborn
*   **Machine Learning:** Scikit-learn, XGBoost
*   **Deployment Target:** IBM Cloud

---

## 2. Project Architecture & Setup

### Pre-Requisites
To run this application locally, install Python 3.x and the required libraries:
```bash
pip install flask pandas numpy scipy matplotlib seaborn scikit-learn xgboost
```

### System Architecture
The application follows a simple web-client architecture:
1. **Frontend:** HTML web forms capture user information.
2. **Backend:** Flask routes handle input data and feed it to the trained model.
3. **ML Engine:** The saved XGBoost model calculates risk and returns a real-time prediction.

---

## 3. Core Development Phases (Epics 1 - 5)

### Epic 1: Data Collection and Architecture Design
*   **Download the Dataset:** Sourced structured credit data containing applicant demographics, income parameters, and historical credit records.
*   **Defining the Application Architecture:** Designed the structural data flow from the web UI form fields to the predictive model back-end.

### Epic 2: Visualizing and Analysing the Data
*   **Import and Read Dataset:** Loaded the target CSV into Python dataframes using Pandas.
*   **Univariate Analysis:** Analyzed independent feature spreads (such as credit history, applicant income, and loan distributions) using histograms and count plots.
*   **Bivariate Analysis:** Explored links between two specific variables at a time to trace how individual factors affect loan status.
*   **Multivariate Analysis:** Generated Seaborn correlation heatmaps to observe complex column interactions and eliminate redundant data dependencies.

### Epic 3: Data Pre-processing
*   **Checking and Handling Values:** Fixed missing cells via statistical imputation (mean/median/mode) and managed feature outliers.
*   **Balancing the Dataset:** Implemented resampling techniques to equalize unbalanced target data classes (`Loan_Status`), protecting the model from biased predictions.
*   **Scaling the Data:** Normalized wide-ranging numerical fields using scaling utilities like `StandardScaler`.
*   **Splitting Data:** Separated processed records into specialized subsets for training and testing validation.

### Epic 4: Model Building
*   **Algorithms Evaluated:** Trained and compared Decision Tree, Random Forest, KNN, and XGBoost structures.
*   **Evaluating Performance and Saving:** Identified **XGBoost** as the top performer, delivering **94.7% training accuracy** and **81.1% testing accuracy**. Saved the final production-ready model parameters to disk.

### Epic 5: Application Building
*   **Building HTML Pages:** Structured clean, intuitive frontend interfaces allowing seamless form data entry for applicants and agents.
*   **Building the Python Script:** Developed core Flask application files (`app.py`) to manage page routing and serve model outcomes.
*   **Run the Application:** Implemented local hosting runtime protocols to test systemic end-to-end functionality.

---

## 4. Application Workflows & Scenarios

### Scenario 1: Fast-Track Approval for Low-Risk Applicants
*   **Workflow:** A salaried client with robust credit history and steady income submits an inquiry. 
*   **Outcome:** The model identifies high creditworthiness and fast-tracks the approval status automatically without needing manual officer intervention.

### Scenario 2: High-Risk Applicant Detection
*   **Workflow:** An applicant with irregular self-employment income and missing credit history files an entry.
*   **Outcome:** The platform instantly flags the record as a high-risk application, holding processing until further verification documents are evaluated.

### Scenario 3: High-Volume Batch Evaluation
*   **Workflow:** An institutional analyst loads large batches of client request queries during peak cycles.
*   **Outcome:** The XGBoost engine processes multiple candidate records simultaneously, drastically saving operational time while upholding accurate risk standards.

---

## 5. Conclusion
Smart Lender securely bridges advanced machine learning capabilities with consumer-facing financial operations. By scaling analytical workflows across automated layers, the system reduces human error while strictly maintaining institutional risk management compliance.
