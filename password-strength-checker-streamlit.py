import streamlit as st

def check_strength_password(input):
    has_upper = any(c.isupper() for c in input)
    has_lower = any(c.islower() for c in input)
    has_digit = any(c.isdigit() for c in input)
    has_special = any(not c.isalnum() for c in input)
    length = len(input)
    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length >= 8 and ((has_upper and has_lower) or (has_lower and has_digit) or (has_upper and has_digit)):
        return "Medium"
    else:
        return "Weak"
def main():
    st.title("🔒Password strength checker")
    st.write("This app checks the strength of your password.")
    password = st.text_input("Enter your password:", type="password")
    if st.button("Check Strength"):
        if not password:
            st.warning("Please enter a password.")
        else:
            strength = check_strength_password(password)
            st.write(f"Your password strength is: **{strength}**")
            if strength == "Strong":
                st.success("Great job! Your password is strong.")
                st.balloons()
            elif strength == "Medium":
                st.warning("Your password is medium strength. Consider adding more characters or a mix of character types.")
            else:
                st.error("Your password is weak. Try using a longer password with a mix of uppercase, lowercase, numbers, and special characters.")