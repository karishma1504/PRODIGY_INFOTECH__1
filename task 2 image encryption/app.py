from flask import Flask, render_template, request, send_file
from PIL import Image
import io

app = Flask(__name__)

def encrypt_image(img):
    encrypted = img.copy()
    pixels = encrypted.load()
    for i in range(encrypted.size[0]):
        for j in range(encrypted.size[1]):
            r, g, b = pixels[i, j]
            # Basic encryption: invert colors
            pixels[i, j] = (255 - r, 255 - g, 255 - b)
    return encrypted

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            img = Image.open(file.stream)
            encrypted_img = encrypt_image(img)

            # Convert image to byte stream for download
            img_io = io.BytesIO()
            encrypted_img.save(img_io, 'PNG')
            img_io.seek(0)
            return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='encrypted_image.png')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
