from flask import Flask, render_template, request
from cryptography.fernet import Fernet
from stegano import lsb

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    encrypted = decrypted = ""

    if request.method == "POST":
        action = request.form["action"]

        if action == "encrypt":
            message = request.form["message"].encode()

            key = Fernet.generate_key()
            f = Fernet(key)
            encrypted = f.encrypt(message).decode()

            secret_img = lsb.hide("cover.png", key.decode())
            secret_img.save("stego_image.png")

        elif action == "decrypt":
            encrypted_input = request.form["encrypted"].encode()

            key = lsb.reveal("stego_image.png").encode()
            f = Fernet(key)
            decrypted = f.decrypt(encrypted_input).decode()

    return render_template("index.html",
                           encrypted=encrypted,
                           decrypted=decrypted)

if __name__ == "__main__":
    app.run(debug=True)
