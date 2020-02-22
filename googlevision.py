import os
from google.cloud import vision

def google_vision_api(image_uri):

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'goooglevision.json'


    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = image_uri

    response = client.label_detection(image=image)

    result = 'Labels:\n'
    for label in response.label_annotations:
        result += f'{label.description} ({label.score*100.:.1f}%)\n'
        print(result)
    return result
