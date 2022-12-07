from PIL  import Image 
import os
downloadsFolder = "/Users/marge/Downloads/"
pictureFolder = "/User/marge/Pictures/"
VideoFolder = "/User/marge/Videos/"
documentFolder = "/Users/marge/Documents/ArchivosZIP/"


if __name__=="__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]: #Compresor de imagenes al 60%
            picture = Image.open(downloadsFolder + filename)
            picture.save(pictureFolder + "compressed_"+filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": "+ extension)

        if extension in [".mp3"]: #Reubica archivos .mp3
            musicFolder = "/Users/marge/Music/"
            os.rename(downloadsFolder + filename, musicFolder + filename)

        if extension in [".mp4"]:  #Reubica archivos .mp4
            videosFolder = "/Users/marge/Videos/"
            os.rename(downloadsFolder + filename, videosFolder + filename)
        
        if extension in [".zip"]:  #Reubica archivos .zip
            documentFolder = "/Users/marge/Documents/ArchivosZIP/"
            os.rename(downloadsFolder + filename, documentFolder + filename)