from js import document

def nanamigreen(event=None):
    reg = document.querySelector('input[name="answer1"]:checked')
    med = document.querySelector('input[name="answer3"]:checked')
    grade = document.getElementById("grd").value
    result = document.getElementById("Result")

    if not reg or not med or grade == "":
        result.textContent = "Please complete all the required fields."
        return

    if reg.value != "yes":
        result.textContent = "You are not eligible yet. Please complete the online registration."
        return

    if med.value != "yes":
        result.textContent = "You are not eligible yet. Please secure a medical clearance from the clinic."
        return

    teams = {
        "BB": ("Blue Bears", "blue bears.jpg"),
        "RB": ("Red Bulldogs", "red bulldogs.jpg"),
        "YT": ("Yellow Tigers", "yellow tigers.jpg"),
        "GH": ("Green Hornets", "green hornets.jpg")
    }

    if grade in teams:
        team_name, team_logo = teams[grade]
        result.innerHTML = f"""
        <div style="text-align: center;">
            <h4> Congratulations! You can now join Intramurals!</h4>
            <img src="{team_logo}" style="max-width: 200px; border-radius: 10px;">
            <p style="margin-top: 10px; font-weight: 600;">
                Your Intramurals Team is: <strong>{team_name}</strong>
            </p>
        </div>
        """
    else:
        result.textContent = "Intramurals is only open for Grades 7 to 10."