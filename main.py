from js import document  # type: ignore
from pyscript import display  # type: ignore

def create_account(e):
    username = document.getElementById("username").value
    password = document.getElementById("password").value

    document.getElementById("output").innerHTML = ""

    if len(username) < 7:
        display("❗ Username must contain at least 7 characters.", target="output")

    else:
        has_letter = False
        has_number = False

        for char in password:
            if char.isalpha():
                has_letter = True
            elif char.isdigit():
                has_number = True

        if len(password) < 10:
            display("❗ Password must be at least 10 characters long.", target="output")

        elif not has_letter:
            display("❗ Password must contain at least one letter.", target="output")

        elif not has_number:
            display("❗ Password must contain at least one number.", target="output")

        else:
            display("🎉 Account successfully created!", target="output")

def check_team(event=None):
    output = document.getElementById("output")
    image = document.getElementById("image")

    output.innerHTML = ""
    image.innerHTML = ""

    registration_radio = document.querySelector('input[name="registration"]:checked')
    medical_radio = document.querySelector('input[name="medical"]:checked')

    if registration_radio is None or medical_radio is None:
        display("ᴘʟᴇᴀꜱᴇ ᴀɴꜱᴡᴇʀ ᴀʟʟ Qᴜᴇꜱᴛɪᴏɴꜱ.", target="output")
        return

    registration = registration_radio.value
    medical = medical_radio.value
    grade = int(document.getElementById("grade").value)
    section = document.getElementById("section").value

    if registration == "no":
        display("ᴘʟᴇᴀꜱᴇ ᴄᴏᴍᴘʟᴇᴛᴇ ʏᴏᴜʀ ᴏɴʟɪɴᴇ ʀᴇɢɪꜱᴛʀᴀᴛɪᴏɴ ꜰɪʀꜱᴛ. (｡•́︿•̀｡)", target="output")

    elif medical == "no":
        display("ᴘʟᴇᴀꜱᴇ ꜱᴇᴄᴜʀᴇ ᴀ ᴍᴇᴅɪᴄᴀʟ ᴄʟᴇᴀʀᴀɴᴄᴇ ꜰʀᴏᴍ ᴛʜᴇ ᴄʟɪɴɪᴄ. (｡•́︿•̀｡)", target="output")

    elif grade < 7 or grade > 10:
        display("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴇʟɪɢɪʙʟᴇ ꜰᴏʀ ɪɴᴛʀᴀᴍᴜʀᴀʟꜱ. (｡•́︿•̀｡)", target="output")

    elif section == "Ruby":
        display("ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴꜱ! ʏᴏᴜ ᴀʀᴇ ᴘᴀʀᴛ ᴏꜰ ᴛʜᴇ ʙʟᴜᴇ ʙᴇᴀʀꜱ ᵎᵎ (≧∇≦)", target="output")
        image.innerHTML = "<img src='blue_bears.jpg' width='250'>"

    elif section == "Sapphire":
        display("ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴꜱ! ʏᴏᴜ ᴀʀᴇ ᴘᴀʀᴛ ᴏꜰ ᴛʜᴇ ʀᴇᴅ ʙᴜʟʟᴅᴏɢꜱ ᵎᵎ (≧∇≦)", target="output")
        image.innerHTML = "<img src='red_bulldogs.jpg' width='250'>"

    elif section == "Emerald":
        display("Congratulations! You are part of the Green Hornets ᵎᵎ (≧∇≦)", target="output")
        image.innerHTML = "<img src='green_hornets.jpg' width='250'>"

    else: 
        display("Congratulations! You are part of the Yellow Tigers ᵎᵎ (≧∇≦)", target="output")
        image.innerHTML = "<img src='yellow_tigers.jpg' width='250'>"

def show_players(e):
    players = [
        "ᴠᴀᴅᴀ ᴀɢᴇɴᴀ",
        "ᴢɪᴘᴘᴏʀᴀʜ ᴀʟᴀ",
        "ᴊᴀɪʏᴀɴᴀʜ ʙᴀʀɪɴɢ",
        "ᴋᴏʙʏ ʙᴀʏʟᴏɴ",
        "ᴀʟᴇxᴀɴᴅʀɪᴀ ʙʀᴏᴅʜᴀɢᴇɴ",
        "ᴊᴀᴅᴇ ᴄᴀʙᴀᴛɪɴɢᴀɴ",
        "ᴛᴀʀᴄɪꜱɪᴜꜱ ᴄᴀɴ̃ᴇᴛᴇ",
        "ᴢᴀᴋᴀʀɪ ᴅɪᴍᴀᴄᴜʟᴀɴɢᴀɴ",
        "ᴅᴡᴀʏɴᴇ ᴇᴠᴀɴɢᴇʟɪꜱᴛᴀ",
        "ᴄʜᴀʀʟɪᴢᴇ ɢᴀʟᴀɴɢ",
        "ꜱʜᴀʟᴀɴɪᴇ ɢᴀʀᴀʙɪʟᴇꜱ",
        "ᴀᴍᴀɴᴅᴀ ɢᴏɴᴢᴀʟᴇꜱ",
        "ꜰʀᴀɴᴄᴇꜱ ᴊᴀᴍᴇᴛ",
        "ᴀɪꜱʜᴀ ʟᴇᴅᴇꜱᴍᴀ",
        "ɢᴀʙʀɪᴇʟʟᴇ ɴᴀᴄɪɴᴏ",
        "ᴋᴀɪᴛʟʏɴ ɴᴀʀᴅᴏ",
        "ᴊᴏᴀQᴜɪɴ ᴏʟɪᴠᴇʀᴏꜱ",
        "ᴄᴇʀɪɴɴᴇ ᴏʟᴍᴇᴅᴏ",
        "ʀᴀɪᴅᴇɴ ᴏɴɢ",
        "ꜱᴀᴍᴀɴᴛʜᴀ ʀᴇʙᴀᴅᴜʟʟᴀ",
        "ᴅᴀᴠɪᴅ ʀᴇʏᴇꜱ",
        "ᴠᴀɴɴᴀ ꜱᴀɴɢʀᴇᴏ",
        "ʟᴀᴜʀᴇɴ ᴠɪʟʟᴀꜰᴜᴇʀᴛᴇ",
        "ᴇɴᴢᴏ ᴠɪʟʟᴇɢᴀꜱ",
        "ᴀᴍᴀɴᴅᴀ ʏᴀᴏ"
    ]

    for player in players:
        display(player, target="show_players")
