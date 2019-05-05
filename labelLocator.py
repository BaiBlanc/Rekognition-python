from PIL import Image, ImageDraw, ImageFont


def labellizeImage(imagePath, labels):
    font = ImageFont.truetype('Arial.ttf', 10)
    image = Image.open(imagePath)
    draw = ImageDraw.Draw(image)
    size = image.size
    for label in labels:
        name = label["Name"]
        if label["Instances"]:
            for instance in label["Instances"]:
                bounds = instance["BoundingBox"]
                confidence = instance["Confidence"]
                startX = bounds["Left"]*size[0]
                startY = bounds["Top"]*size[1]
                endX = startX + bounds["Width"]*size[0]
                endY = startY + bounds["Height"]*size[1]
                draw.rectangle(((startX, startY), (endX, endY)),
                               outline="black", width=2)
                draw.text(((startX+endX)/2, startY), name +
                          "\n"+str(round(confidence,2)), font=font)
    return image
