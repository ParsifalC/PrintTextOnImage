from PIL import Image, ImageDraw, ImageFont
import time, os, sys, imghdr

def printDateOnImage(imagePath):
    timeStr = time.strftime('%Y%m%d-%H:%M:%S', time.localtime(time.time()))
    printTextOnImage(imagePath, timeStr)

def printTextOnImage(imagePath, textList=[]):
    imgType = imghdr.what(imagePath)
    if imgType == 'png':
        oriImage = Image.open(imagePath).convert('RGBA')
        width,height = oriImage.size
        fontPath = resource_path(resource_path(os.path.join("res", "Roboto-Bold.ttf")))
        fontHeight = height/9
        font = ImageFont.truetype(fontPath, size=int(fontHeight))
        txtImage = Image.new('RGBA', (width, height), (255, 255, 255, 0))
        # 时间
        draw = ImageDraw.Draw(txtImage)
        timeStr = time.strftime('%Y%m%d-%H:%M:%S', time.localtime(time.time()))
        draw.text((0, height/10), timeStr, fill=(0, 0, 0), font=font, align='center')

        for text in textList:
            draw.text((0, height/3 + textList.index(text) * fontHeight), text, fill=(0, 0, 0), font=font, align='center')
        
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
    textList = []
    if len(argv) > 2:
        dirPath = argv[1]
        for str in argv[2:]:
            textList.append(str)
    else:
        dirPath = os.getcwd()

    imageList = os.listdir(dirPath)

    for path in imageList:
        if os.path.isfile(os.path.join(dirPath, path)):
            if dirPath:
                absolutePath = dirPath+'/'+path
            else:
                absolutePath = path

            printTextOnImage(imagePath=absolutePath, textList=textList)
            print('添加'+absolutePath+'日期成功')
        else:
            print('不需要添加'+path)


getDirPath(sys.argv)
