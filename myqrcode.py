import qrcode
# Get user input
text = input("Enter the data you want to encode: ")
dest = input("Enter the full path destination of where you want your QR code to be saved: ")
qr_name = input('Enter the name to save the image: ')


# Format destination path
dest = dest.replace("\\", "/") 
dest = dest + '/' + qr_name + ".png"

# Create QR code
qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_H, 
    box_size=10, 
    border=4,
)

qr.add_data(text)
qr.make(fit=True)

# Define color options
color_options = {
    "1": "Purple",
    "2": "White",
    "3": "Blue",
    "4": "Black",
    "5": "Cyan",
    "6": "Yellow"
}

# Get fill color
while True:
    print("\nList of fill_colours available:")
    for key, value in color_options.items():
        print(f"{key}. {value}")
    
    choice = input("Enter the fill color you desire (number or name): ")
    
    if choice.isdigit() and 1 <= int(choice) <= 6:
        choice = color_options[choice]
        break
    elif choice.capitalize() in color_options.values():
        choice = choice.capitalize()
        break
    print("Invalid choice. Please try again.")

# Get background color
while True:
    print("\nList of background_colours available:")
    for key, value in color_options.items():
        print(f"{key}. {value}")
    
    choice2 = input("Enter the background color you desire (number or name): ")
    
    if choice2.isdigit() and 1 <= int(choice2) <= 6:
        choice2 = color_options[choice2]
        break
    elif choice2.capitalize() in color_options.values():
        choice2 = choice2.capitalize()
        break
    print("Invalid choice. Please try again.")

while True:
    if choice2 == choice :
        print("You've re-entered the same colors. Try again! ")
    
        break
       
    else:
        img = qr.make_image(fill_color=choice, back_color=choice2)
        img.save(dest)
        print("Success! Your QR code has been generated.")
        exit()

