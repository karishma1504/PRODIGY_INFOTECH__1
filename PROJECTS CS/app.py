from flask import Flask, render_template, request

app = Flask(__name__)


def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        message = request.form['message']
        shift = int(request.form['shift'])
        action = request.form['action']

        if action == 'encrypt':
            result = encrypt(message, shift)
        elif action == 'decrypt':
            result = decrypt(message, shift)

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
