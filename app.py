import streamlit as st

st.set_page_config(page_title="SBI Bank", page_icon="🏦", layout="wide")

class BankApplication:
    bank_name = "SBI"

    def __init__(self, name, account_number, age, mobile_number, balance):
        self.name = name
        self.account_number = account_number
        self.age = age
        self.mobile_number = mobile_number
        self.balance = balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return f"₹{amount} Withdrawn Successfully"
        else:
            return "Insufficient Balance"

    def deposit(self, amount):
        self.balance += amount
        return f"₹{amount} Deposited Successfully"

    def update_mobile(self, new_number):
        self.mobile_number = new_number
        return "Mobile Number Updated"

    def check_balance(self):
        return self.balance


# CSS Styling
st.markdown("""
<style>

.main {
    background-color:#f5f7fa;
}

.stButton>button {
    width:100%;
    border-radius:10px;
    height:45px;
    font-size:16px;
}

.card {
    padding:20px;
    border-radius:10px;
    background:white;
    box-shadow:0 4px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)


st.title("🏦 SBI Digital Banking")

# Session state
if "account" not in st.session_state:
    st.session_state.account = None


# Sidebar Account Creation
st.sidebar.title("Create Account")

name = st.sidebar.text_input("Name")
acc = st.sidebar.text_input("Account Number")
age = st.sidebar.number_input("Age", min_value=18)
mobile = st.sidebar.text_input("Mobile Number")
balance = st.sidebar.number_input("Initial Balance", min_value=0)

if st.sidebar.button("Create Account"):

    st.session_state.account = BankApplication(
        name, acc, age, mobile, balance
    )

    st.sidebar.success("Account Created Successfully")


if st.session_state.account:

    account = st.session_state.account

    st.subheader(f"Welcome {account.name}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Account Number", account.account_number)

    with col2:
        st.metric("Mobile", account.mobile_number)

    with col3:
        st.metric("Balance", f"₹{account.balance}")

    st.divider()

    option = st.selectbox(
        "Select Banking Service",
        ["Deposit", "Withdraw", "Check Balance", "Update Mobile"]
    )

    if option == "Deposit":

        amount = st.number_input("Deposit Amount", min_value=1)

        if st.button("Deposit Money"):
            msg = account.deposit(amount)
            st.success(msg)

    elif option == "Withdraw":

        amount = st.number_input("Withdraw Amount", min_value=1)

        if st.button("Withdraw Money"):
            msg = account.withdraw(amount)
            st.success(msg)

    elif option == "Check Balance":

        if st.button("Show Balance"):
            st.info(f"Your Balance is ₹{account.check_balance()}")

    elif option == "Update Mobile":

        new = st.text_input("New Mobile Number")

        if st.button("Update Number"):
            msg = account.update_mobile(new)
            st.success(msg)

else:

    st.info("👈 Create an account from the sidebar to start banking.")