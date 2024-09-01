


import streamlit as st
# Display the title with center alignment using Markdown and unsafe_allow_html
st.markdown("<h1 style='text-align: center;'> User Registration </h1>", unsafe_allow_html=True)
# Create a form with the name "form 1" and clear the form on submission
with st.form("form 1",clear_on_submit=True):
     # Create two columns for first and last name inputs
     col1,col2=st.columns(2)
     # Create three columns for day, month, year selection
     day,month,year=st.columns(3)
     # Define weekday options for the select box
     weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
     # Define month options for the select box
     months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
      # Get first name input with emoji and placeholder
     First_name = col1.text_input("💫 Enter Your First Name",placeholder="John")
      # Get last name input with emoji and placeholder
     Last_name =  col2.text_input("💫 Enter Your Last Name",placeholder="Doe")
     # Get email input with emoji and placeholder
     Email =      col1.text_input("💌 Enter Your Email ID",placeholder="your@gmail.com")
     # Get password input with "password" type and emoji and placeholder
     Password =   st.text_input("🔐 Enter Your Password",type="password",placeholder="Enter a Strong password")
     # Get confirm password input with "password" type and emoji and placeholder
     Confirm_Password = st.text_input("🛠 Confirm Password",type="password",placeholder="Don't You Forget!")  
     # Create a select box for day selection with weekday options
     day.selectbox("💛 Day", weekdays)
     # Create a select box for month selection with month options
     month.selectbox("💚 Month",months_list)
     # Get year input with emoji and placeholder
     year.text_input("💙 Year",placeholder="Year")
     # Create a submit button with emoji
     submitted=st.form_submit_button(" 💞 Submit ")
     # Check if the form is submitted
     if submitted:
          # Check if required fields are empty
         if First_name == "" and Last_name =="" and Email== "" :
              # Display a warning message with an icon
             st.warning("Please fill above fields!",icon="⚠")
         else:
              # Display a success message with an icon (registration is currently not functional)
             st.success("Registration Successfull!",icon="❤")
