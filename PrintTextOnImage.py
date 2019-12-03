from PIL import Image, ImageDraw, ImageFont
import time, os, sys, imghdr

def printDateOnImage(imagePath):
    timeStr = time.strftime('%Y%m%d-%H:%M:%S', time.localtime(time.time()))
    printTextOnImage(imagePath, timeStr)

def printTextOnImage(imagePath, text):
    imgType = imghdr.what(imagePath)
    if imgType == 'png':
        oriImage = Image.open(imagePath).convert('RGBA')
        width,height = oriImage.size
        fontPath = resource_path(resource_path(os.path.join("res", "Roboto-Bold.ttf")))
        font = ImageFont.truetype(fontPath, size=int(height/9))
        txtImage = Image.new('RGBA', (width, height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(txtImage)
        draw.text((width/4, height/4), text, fill=(0, 0, 0), font=font, align='center')
        timeStr = time.strftime('%Y%m%d-%H:%M:%S', time.localtime(time.time()))
        draw.text((0, height/4 + height/9 + 10), timeStr, fill=(0, 0, 0), font=font, align='center')
        out = Image.alpha_composite(oriImage, txtImage)
        out.save(imagePath)

def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def getDirPath(argv):
    dirPath = None
    text = ''

    if len(argv) > 2:
        dirPath = argv[1]
        for str in argv[2:]:
            text += str
    else:
        dirPath = os.getcwd()
        text = time.strftime('%Y%m%d-%H:%M:%S', time.localtime(time.time()))

    imageList = os.listdir(dirPath)

    for path in imageList:
        if os.path.isfile(os.path.join(dirPath, path)):
            if dirPath:
                absolutePath = dirPath+'/'+path
            else:
                absolutePath = path

            printTextOnImage(imagePath=absolutePath, text=text)
            print('添加'+absolutePath+'日期成功')
        else:
            print('不需要添加'+path)


getDirPath(sys.argv)
