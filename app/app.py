from flask import Flask, jsonify, request
from PIL import Image
from backend import transform


app = Flask(__name__)
'''
Tested on Postman using form-data body post request.
'''


@app.route('/', methods = ['GET', 'POST'])
def greeting():
    default_output = ['The app is online and can be accessed at the /transformer endpoint. ',
                        'Be sure to use a post request with your image file.']
    return '\n'.join(default_output)


@app.post('/transformer')
def engine():
    
    img_file = request.files['image']
    img = Image.open(img_file.stream)
    transformer_output= transform(img)

    try:
        result = jsonify(transformer_output)
    except TypeError as e:
        result = jsonify({'The following error has occured':
         str(e)})
    return result

'''
For running locally with flask:
if __name__ == '__main__':
    app.run(host = '127.0.0.1',  debug = False)
'''