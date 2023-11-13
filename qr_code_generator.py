import qrcode

# Dati da codificare nel QR code (un URL in questo caso)
data = "https://drive.google.com/file/d/1BUB8HPHxYLz-33kCKuJnWBsa4QFVcM4Q/view?usp=share_link"
# Creazione di un'istanza di QR code
qr = qrcode.QRCode(
    version=1,  # Versione del QR code (da 1 a 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # # Livello di correzione degli errori
    box_size=10,  # Dimensione di ogni blocco/pixel
    border=4,  # Dimensione del bordo attorno al QR code
)

# Aggiunta dei dati al QR code e generazione del QR code
qr.add_data(data)
qr.make(fit=True)

# Creazione di un oggetto immagine a partire dall'istanza del QR code
img = qr.make_image(fill_color="black", back_color="white")

# Salvataggio del QR code come file immagine PNG
img.save("example_qr.png")

# Visualizzazione del qr code
img.show()

