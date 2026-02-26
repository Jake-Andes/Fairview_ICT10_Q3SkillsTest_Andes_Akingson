from pyscript import document, display, alert  # type: ignore



def validate_account(event=None):
    username = document.getElementById("username").value
    password = document.getElementById("password").value

    has_capital = False
    has_special = False

    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    for letter in password:
        if letter.isupper():
            has_capital = True
        elif letter in special_chars:
            has_special = True

    if username == "" or password == "":
        alert("Please fill in all fields.")

    elif has_capital and has_special:
        alert("Account Created Successfully!")

    else:
        alert("Password must contain at least 1 CAPITAL letter and 1 SPECIAL character.")