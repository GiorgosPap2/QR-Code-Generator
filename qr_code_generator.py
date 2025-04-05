import qrcode

# Base URL for the index.html file
base_url = "index.html"

# Generate QR codes for each team
for i in range(1, 11):
    # Create URL with team parameter
    url = f"{base_url}?team=team{i}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    qr_image = qr.make_image(fill_color="black", back_color="white")
    filename = f"qr_code_{i}.png"
    qr_image.save(filename)
    print(f"Generated QR code {i} for URL: {url}")
    print(f"Saved as {filename}")

print("\nAll QR codes have been generated!") 