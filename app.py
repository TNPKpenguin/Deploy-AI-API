from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, storage
import datetime 

cred_path  = r"C:\Users\LENOVO\Desktop\HCU\summer_4_1\deploy_models_test\imagestestapi-firebase-adminsdk-rthos-548c10df85.json"

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred, {
    'storageBucket': 'imagestestapi.appspot.com'
})

bucket = storage.bucket()

def upload_image(image_path, destination_blob_name):
    """Uploads an image to Firebase Storage."""
    # Create a blob in the bucket
    blob = bucket.blob(destination_blob_name)

    # Upload the image
    blob.upload_from_filename(image_path)

    # Make the blob publicly viewable (optional)
    blob.make_public()

    print(f"File uploaded to {blob.public_url}")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imageFile = request.files['imagefile']
    image_path = "./images/" + imageFile.filename
    # imageFile.save(image_path)
    upload_image(image_path, f"images/{str(datetime.datetime.now())}.png")

    classification = ""
    if imageFile.filename == "test.png":
        classification = '%s' % ("test")

    return render_template('index.html', prediction=classification)

if __name__ == "__main__":
    app.run(port=3000, debug=True)