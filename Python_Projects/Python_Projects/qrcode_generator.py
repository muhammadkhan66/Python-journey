# Import the qrcode library to generate QR codes
import qrcode

# Take the URL input from the user
url = input("Enter the URL: ")

# Take the filename input from the user
filename = input("Enter the filename you want to save as: ")

# Check if the filename already ends with ".png"
if (filename.endswith(".png")):
    # If not, add ".png" extension to the filename
    filename = filename + ".png"

# Generate the QR code image from the given URL
img = qrcode.make(url)

# Save the generated QR code image with the given filename
img.save(filename)
