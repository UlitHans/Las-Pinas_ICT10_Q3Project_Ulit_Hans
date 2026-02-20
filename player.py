from pyscript import document

players = [
    "ABACA","ALAVADO","ARENAL","AVENTAJADO","BUHAIN",
    "CARPIO","CENON","CRUZ","DE LEON","DE PERALTA",
    "DEL BARRIO","DIDA-AGUN","DUMLAO","ESTAPIA",
    "GALOPE","GALURA","GUEVARRA","GURANGO","LAZO",
    "LIWAG","MAGPANTAY","MOYAEN","PANUNCIALMAN",
    "PROWEL","RAMOS","SANNINO","TECSON","ULIT"
]

def showPlayers(event=None):
    output = document.getElementById("players")
    if not output:
        print("Error: #players element not found")
        return
    html_content = "<h3>Players List</h3><hr>"
    for i, player in enumerate(players, 1):
        html_content += f"{i}) {player}<br>"
    output.innerHTML = html_content