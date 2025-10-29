import qrcode



quizesURLs = [
    'https://create.kahoot.it/details/97e20a35-6381-4c1f-94d8-4e1950e5870d',
    'https://create.kahoot.it/details/a74ed8d2-b5e8-48b2-8c5c-4a73e1596c51',
    'https://create.kahoot.it/details/a0022902-3a24-481e-b825-3837706d36b0',
    'https://create.kahoot.it/details/cccc51a0-74db-47fc-bb22-18a3d58ffaf5',
    'https://create.kahoot.it/details/edf82c46-5d00-4724-bd0d-d28609886d2b'
]

# # 1st implementation
# base_url = "https://giorgospap2.github.io/QR-Code-Generator/"
# 
# for i in range(1, 11):
#     url = f"{base_url}?team=team{i}"
#
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#
#     qr.add_data(url)
#     qr.make(fit=True)
    
#     qr_image = qr.make_image(fill_color="black", back_color="white")
#     filename = f"qr_team{i}.png"
#     qr_image.save(filename)
#     print(f"Generated QR code {i} for URL: {url}")
#     print(f"Saved as {filename}")

# print("\nAll QR codes have been generated!") 


# 2nd implementation
for i, url in enumerate(quizesURLs, start=1):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    qr_image = qr.make_image(fill_color="black", back_color="white")
    filename = f"QR_Codes/quiz_{i}.png"
    qr_image.save(filename)
    print(f"Generated QR code {i} for URL: {url}")
    print(f"Saved as {filename}")

print("\nAll quiz QR codes have been generated!")
