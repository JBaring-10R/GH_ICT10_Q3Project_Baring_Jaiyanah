from js import document  # type: ignore
from pyscript import display  # type: ignore

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
        image.innerHTML = "<img src='blue_bears.jpg' width='350'>"

    elif section == "Sapphire":
        display("ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴꜱ! ʏᴏᴜ ᴀʀᴇ ᴘᴀʀᴛ ᴏꜰ ᴛʜᴇ ʀᴇᴅ ʙᴜʟʟᴅᴏɢꜱ ᵎᵎ (≧∇≦)", target="output")
        image.innerHTML = "<img src='red_bulldogs.jpg' width='350'>"

    elif section == "Emerald":
        display("Congratulations! You are part of the Green Hornets ᵎᵎ (≧∇≦)", target="output")
        image.innerHTML = "<img src='green_hornets.jpg' width='350'>"

    else: 
        display("Congratulations! You are part of the Yellow Tigers ᵎᵎ (≧∇≦)", target="output")
        image.innerHTML = "<img src='yellow_tigers.jpg' width='350'>"
