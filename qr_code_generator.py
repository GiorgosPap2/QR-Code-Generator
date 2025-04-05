import qrcode

# List of word pairs
word_pairs = [
    "Ομάδα: Λεονιντ - Άγγελος",
    "Ομάδα: Ευαγγελία - Πασχαλης",
    "Ομάδα: Τράκας - Ελιζιαννα",
    "Ομάδα: Ευθυμης - Αλέξανδρος",
    "Ομάδα: Σοφία - Γεωργακάκης",
    "Ομάδα: Ιωαννα - Σωτήρης",
    "Ομάδα: Ζωή - Σηφάκης",
    "Ομάδα: Φωτης - Κυνθια",
    "Ομάδα: Ευθυμία - Ειρηνη",
    "Ομάδα: Άγγελος/Ευάγγελος - Διαλεκτη"
]

# Generate 10 QR codes
for i, pair in enumerate(word_pairs, start=1):
    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10,  
        border=4,  
    )
    
    qr.add_data(pair)
    qr.make(fit=True)
    
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    filename = f"qr_code_{i}.png"
    qr_image.save(filename)
    print(f"Generated QR code {i} for '{pair}' and saved as {filename}")

print("All 10 QR codes have been generated!")