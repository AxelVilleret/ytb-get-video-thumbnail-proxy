from flask import Flask, request, send_file
from io import BytesIO
import requests

app = Flask(__name__)


@app.route('/proxy')
def proxy_image():
    image_url = request.args.get('image_url')
    if not image_url:
        return "Aucune URL d'image fournie.", 400

    response = requests.get(image_url)
    if response.status_code != 200:
        return "Impossible de récupérer l'image.", 502

    image_bytes = BytesIO(response.content)
    # Créer une réponse à partir de l'objet BytesIO
    flask_response = send_file(image_bytes, mimetype='image/png')
    # Ajouter les en-têtes CORS à la réponse
    flask_response.headers['Access-Control-Allow-Origin'] = '*'
    return flask_response


if __name__ == '__main__':
    app.run(port=5000)
