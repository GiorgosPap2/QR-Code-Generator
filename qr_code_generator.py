import qrcode
import re
import os

# Base URL for the index.html file
base_url = "https://giorgospap2.github.io/QR-Code-Generator/"

# Team data dictionary
teamData = {
    'team1': 'Ομάδα: Λεονιντ - Άγγελος',
    'team2': 'Ομάδα: Ευαγγελία - Πασχαλης',
    'team3': 'Ομάδα: Τράκας - Ελιζιαννα',
    'team4': 'Ομάδα: Ευθυμης - Αλέξανδρος',
    'team5': 'Ομάδα: Σοφία - Γεωργακάκης',
    'team6': 'Ομάδα: Ιωαννα - Σωτήρης',
    'team7': 'Ομάδα: Ζωή - Σηφάκης',
    'team8': 'Ομάδα: Φωτης - Κυνθια',
    'team9': 'Ομάδα: Ευθυμία - Ειρηνη',
    'team10': 'Ομάδα: Άγγελος-Ευάγγελος - Διαλεκτη'  # Changed / to - to avoid filename issues
}

# Function to create a safe filename
def create_safe_filename(team_name):
    # Replace problematic characters
    safe_name = team_name.replace('/', '-').replace('\\', '-')
    # Remove any other characters that might cause issues
    safe_name = re.sub(r'[<>:"|?*]', '', safe_name)
    return safe_name

# Generate QR codes for each team
for i in range(1, 11):
    team_key = f'team{i}'
    team_name = teamData[team_key]
    
    # Create URL with team parameter
    url = f"{base_url}?team={team_key}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Create a safe filename with the team name
    safe_filename = f"qr_{create_safe_filename(team_name)}.png"
    qr_image.save(safe_filename)
    
    print(f"Generated QR code {i} for team: {team_name}")
    print(f"URL: {url}")
    print(f"Saved as: {safe_filename}")
    print("-" * 50)

print("\nAll QR codes have been generated!") 