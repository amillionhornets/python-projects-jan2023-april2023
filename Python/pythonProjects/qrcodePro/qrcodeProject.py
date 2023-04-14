import qrcode
import cv2

# Makes a qrcode
def makeQrCode():
    features = qrcode.QRCode(version=1, box_size=40, border=3)
    features.add_data('cool qrcode')
    features.make(fit=True)

    generate_image = features.make_image(fill_color="black", back_color="white")
    generate_image.save('myQrCode2.png')

# Decodes the qrcode with a abs path
def decodeQrCode(qrName):
    image = cv2.imread(qrName)
    detector = cv2.QRCodeDetector()
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
    if vertices_array == None:
        print(data)
    else:
        print("Error")

def main():
    imgPath = "C:\\Users\\Dylan Clark\\Desktop\\Python\\pythonProjects\\qrcodePro\\myQrCode2.png"
    decodeQrCode(imgPath)
    # makeQrCode()

if __name__ == "__main__":
    main()