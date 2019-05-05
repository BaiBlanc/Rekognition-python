import boto3
import glob
import sys
import os
import base64
import json

from labelLocator import labellizeImage

imputFolder = "./photos/"
outputFolder = "./photos_labellized/"
imagesPaths = glob.glob(imputFolder + "*")
for imagePath in imagesPaths:
    client = boto3.client('rekognition')
    print(imagePath)
    outputImage = imagePath.replace(".jpg", "_labellized.jpg").replace(
        ".jpeg", "_labellized.jpeg").replace(".JPG", "_labellized.JPG").replace("./photos/", "")  # Add more replace if more format of image is required
    outputPath = outputFolder+outputImage
    with open(imagePath, 'rb') as f:
        res = f.read()
    print("Start image analyzing")
    response = client.detect_labels(
        Image={
            'Bytes': res
        },
        MaxLabels=123,
        MinConfidence=50
    )
    print("Response got")
    labels = response["Labels"]
    stringData = str(response).replace("\'", "\"").replace(", \"", ",\n\"")
    jsonPath = outputPath.replace("jpg", "json").replace(
        "jpeg", "json").replace("JPG", "json")
    with open(jsonPath, 'w') as f:
        json.dump(response, f)
    image = labellizeImage(imagePath, labels)
    image.save(outputPath)

# for path in imagesPaths:
#     response = client.detect_labels(
#     Image={
#         'Bytes': open(path, mode='br')

#     },
#     MaxLabels=123,
#     MinConfidence=...
# )
