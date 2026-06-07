from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import io
import base64

app = Flask(__name__)

IMG_B64 = "..." # À remplir

@app.route('/')
def countdown():
    # Code...
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
