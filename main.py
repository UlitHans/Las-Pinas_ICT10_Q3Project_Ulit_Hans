from js import document

def createAccount(event=None):
    username = document.getElementById("username").value or ""
    password = document.getElementById("password").value or ""
    msg = document.getElementById("message")
    
    if username.strip() and password.strip():
        msg.innerText = "Account created!"
        # Clear inputs after success
        document.getElementById("username").value = ""
        document.getElementById("password").value = ""
    else:
        msg.innerText = "Please fill in all fields."