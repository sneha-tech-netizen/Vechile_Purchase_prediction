import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Car Recommendation System", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #F9FAFB;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(135deg, #4F46E5, #6366F1);
    color: white;
    font-size: 16px;
    border-radius: 10px;
    height: 50px;
    border: none;
}

.result-box {
    background: #EEF2FF;
    padding: 25px;
    border-radius: 12px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<h1 style='text-align: center;'>🚗 Car Recommendation System</h1>
<p style='text-align: center; color: gray;'>
Find the best car type based on your profile & budget
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- IMAGE ----------------
st.image("car.jpeg", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- INPUT SECTIONS ----------------

#  Personal Info
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("👤 Personal Information")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 70, 30)

with col2:
    gender = st.radio("Gender", ["Male", "Female"])

st.markdown('</div>', unsafe_allow_html=True)


# 🎓 Education & Family
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🎓 Education & Family")

col1, col2 = st.columns(2)

with col1:
    education = st.selectbox("Education", ["Graduate", "Post-Graduate"])

with col2:
    dependents = st.number_input("No. of Dependents", 0, 5, 0)

marital_status = st.selectbox("Marital Status", ["Single", "Married"])

st.markdown('</div>', unsafe_allow_html=True)


# 💼 Financial Details
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("💼 Financial Details")

col1, col2 = st.columns(2)

with col1:
    salary = st.number_input("Your Salary (₹)", 0)

with col2:
    partner_salary = st.number_input("Partner Salary (₹)", 0)

partner_working = st.radio("Is Partner Working?", ["Yes", "No"])

st.markdown('</div>', unsafe_allow_html=True)


# 🏦 Loan Details
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🏦 Loan Details")

col1, col2 = st.columns(2)

with col1:
    personal_loan = st.radio("Personal Loan", ["Yes", "No"])

with col2:
    house_loan = st.radio("House Loan", ["Yes", "No"])

st.markdown('</div>', unsafe_allow_html=True)


# 💰 Car Budget (NEW INPUT)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("💰 Car Budget")

price = st.slider("Select Your Budget (₹)", 300000, 2000000, 800000)

st.markdown('</div>', unsafe_allow_html=True)


# ---------------- SIMPLE LOGIC (REPLACE WITH MODEL LATER) ----------------
def recommend_car(price):
    if price < 600000:
        return "Hatchback 🚙"
    elif price < 1200000:
        return "Sedan 🚗"
    else:
        return "SUV 🚘"


# ---------------- BUTTON ----------------
predict = st.button("🚀 Recommend Car Type")

# ---------------- RESULT ----------------
if predict:
    car_type = recommend_car(price)

    st.markdown(f"""
    <div class="result-box">
        <h3>Recommended Car Type</h3>
        <h1 style='color:#4F46E5;'>{car_type}</h1>
    </div>
    """, unsafe_allow_html=True)