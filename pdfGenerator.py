from PIL import Image
import os

def folderToPdf(folder, outputFile):

    obj = os.scandir(folder)

    imageCount = 0

    for entry in obj:
        if entry.is_file() and len(entry.name) > 4 and entry.name[-4:] == ".png":
            imageCount += 1
        
    if imageCount > 0:
        Image.open(folder + "/" + str(0) + ".png").save(outputFile, "PDF" ,resolution=100.0, save_all=True, append_images=(Image.open(folder + "/" + str(f) + ".png") for f in range(1, imageCount)))

if __name__ == "__main__":
    print("name the folder of images")
    folder = ""
    while folder == "":
        folder = input()
    outputFile = os.path.join("output", folder + ".pdf")
    folder = os.path.join("output", folder)

    folderToPdf(folder, outputFile)
