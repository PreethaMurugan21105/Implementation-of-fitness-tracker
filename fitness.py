import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    height_m = height / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

# Function to determine weight category
def weight_category(bmi):
    if bmi < 18.5:
        return "Underweight", "🔵"
    elif 18.5 <= bmi < 24.9:
        return "Normal", "🟢"
    elif 25 <= bmi < 29.9:
        return "Overweight", "🟠"
    else:
        return "Obese", "🔴"

# Function to estimate heart rate
def estimate_heart_rate(age):
    return 70 if age < 40 else 75

# Function to estimate breathing rate
def estimate_breathing_rate():
    return 16  # Average for a healthy adult

# Function to generate diet recommendations
def diet_recommendation(bmi, on_diet):
    if bmi < 18.5:
        return "Increase protein & healthy fats, eat more frequently 🍗🥑"
    elif bmi < 24.9:
        return "Maintain a balanced diet with fruits, veggies, and lean protein 🍎🥗"
    elif bmi < 29.9:
        return "Reduce processed foods, increase fiber & hydration 🚰🥦"
    else:
        return "Consider consulting a nutritionist for a weight-loss diet 🏥"

# Function for doctor visit recommendation
def doctor_recommendation(bmi):
    return "⚠️ Consider seeing a doctor for a check-up." if bmi >= 30 else "✅ No urgent need for a doctor visit."

# Streamlit App
st.set_page_config(page_title="Personal Fitness Tracker", page_icon="💪", layout="wide")

# Sidebar for User Inputs
st.sidebar.title("📝 Enter Your Details")
age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=25, step=1)
height = st.sidebar.number_input("Height (cm)", min_value=100, max_value=250, value=170, step=1)
weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200, value=70, step=1)
workout_time = st.sidebar.number_input("Workout Time (minutes/day)", min_value=0, max_value=300, value=30, step=5)
on_diet = st.sidebar.radio("Are you on a diet?", ["Yes", "No"])

# Main UI
st.title("🏋️ Personal Fitness Tracker")

if st.sidebar.button("🔍 Analyze My Health"):
    bmi = calculate_bmi(weight, height)
    category, emoji = weight_category(bmi)
    heart_rate = estimate_heart_rate(age)
    breathing_rate = estimate_breathing_rate()
    diet_plan = diet_recommendation(bmi, on_diet)
    doctor_visit = doctor_recommendation(bmi)

    # Display Results
    st.subheader("📊 Health Analysis")
    st.metric(label="Body Mass Index (BMI)", value=f"{bmi} {emoji}")
    st.progress(bmi / 40)  # Progress bar for BMI (scaled to 40)
    st.write(f"*Weight Category:* {category}")

    st.subheader("💓 Heart & Breathing Rate")
    st.metric(label="Estimated Resting Heart Rate", value=f"{heart_rate} bpm")
    st.metric(label="Estimated Breathing Rate", value=f"{breathing_rate} breaths/min")

    st.subheader("🍽️ Diet Recommendation")
    st.success(diet_plan)

    st.subheader("🏥 Doctor Visit Recommendation")
    st.warning(doctor_visit if bmi >= 30 else "✅ You're doing well! Keep monitoring your health.")

# Footer
st.markdown("---")
st.markdown("👨‍⚕️ Stay healthy & fit! This app is for informational purposes only.")