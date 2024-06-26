from flask import Flask, render_template, request
import flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imageFile = request.files['imagefile']
    image_path = "./images/" + imageFile.filename
    imageFile.save(image_path)

    classification = ""
    if imageFile.filename == "test.png":
        classification = '%s' % ("test")

    return render_template('index.html', prediction=classification)

if __name__ == "__main__":
    app.run(port=3000, debug=True)