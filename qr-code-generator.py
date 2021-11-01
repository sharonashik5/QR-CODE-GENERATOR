import pyqrcode

# QR Code Generator Function
def qr_Code_Generator():
    inp = input("Enter the text : ")
    res = pyqrcode.create(inp)
    res.png("QR CODE 1.png", scale = 7)
    
    print("Your qr code is successfully generated and is stored as png file")


# Main Driver
if __name__=="__main__":
    qr_Code_Generator()
