import time

import os
import shutil


print("Stanley 1.0")

#shutil func and configuration for moving duplicate files
def stan(source, destination):
    name = os.path.basename(source)
    destination_file = os.path.join(destination, name)

    if os.path.exists(destination_file):
        namae, ext = os.path.splitext(name)
        x = 1
        while os.path.exists(destination_file):
            namae = f"{namae} ({x}){ext}"
            destination_file = os.path.join(destination, namae)
            x += 1

    shutil.move(source, destination_file)

#sort files into folders
def sort_files():
    print("Confirm the path of the folder you want to sort...")
    dir = input("Path: ")
    


    #INSTRCUTIONS:
    #Upload to a main folder to be sorted
    executables= os.path.join(dir, "exe")
    zips= os.path.join(dir, "zips")
    gif= os.path.join(dir, "gifs")
    sheets= os.path.join(dir, "sheets")
    twt = os.path.join(dir, "twt")
    pint = os.path.join(dir, "pinterest")
    giasset = os.path.join(dir, "messenger_downloads")
    screenshots = os.path.join(dir, "yt screenshots")
    rdt = os.path.join(dir, "rdt")
    canvadocs = os.path.join(dir, "canvadocs")
    messenger_image_files = os.path.join(dir, "messenger_downloads")
    messenger_videos = os.path.join(dir, "messenger videos")
    images = os.path.join(dir, "images")
    pngs = os.path.join(dir, "png")
    discord_image_files = os.path.join(dir, "dih")
    googleimage = os.path.join(dir, "goog")
    documents = os.path.join(dir, "documents")
    web_files = os.path.join(dir, "code")
    videos = os.path.join(dir, "videos")
    audio= os.path.join(dir, "audio")


    # these folders will be created if they don't exist
    folders = [
        executables,
        zips,
        sheets,
        twt,
        gif,
        pint,
        giasset,
        screenshots,
        rdt,
        canvadocs,
        messenger_image_files,
        messenger_videos,
        images,
        pngs,
        discord_image_files,
        googleimage,
        documents,
        web_files,
        videos, 
        audio
    ]
    print("Making directories...")
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    print("Directories created...")


    print("Sorting your files into folders..")
    time.sleep(1)

    folderlist = os.listdir(dir)
    
    for file in folderlist:
        keys = os.path.join(dir, file)

        if not os.path.isfile(keys):
            continue #script for only files and not folders

        extension = os.path.splitext(file)[1].lower()

        match file:
            case name if name == "stanley.py":
                continue
            #keeps the script in the folder


            case name if "videoframe_" in name:
                stan(keys, screenshots)
                #this is prioritized due to overlap with png 
            case name if "_n" in name:
                stan(keys, messenger_image_files)
            case name if "RDT_" in name:
                stan(keys, rdt)
            case name if "IMG_" in name:
                stan(keys, discord_image_files)
                #this is also prioritized due to overlap with webp
            case name if "image" in name:
                stan(keys, googleimage)
            case name if "removebg-preview" in name or "Untitled design" in name:
                stan(keys, canvadocs)


            case name if extension in (".jpg", ".jpeg") and len(name) == 19:
                stan(keys, twt)
            case name if extension in (".jpg", ".jpeg") and len(name) == 36:
                stan(keys, pint)
            case name if extension in (".jpg", ".jpeg") and len(name) == 40:
                stan(keys, googleimage)
            case name if extension in (".jpg", ".jpeg") and len(name) == 56:
                stan(keys, giasset)


            case name if extension == ".exe":
                stan(keys, executables)
            case name if extension == ".zip":
                stan(keys, zips)
            case name if extension in (".html", ".py"):
                stan(keys, web_files)
            case name if extension in (".xlsx", ".csv"):
                stan(keys, sheets)
            case name if extension in (".pdf", ".pptx", ".docx"):
                stan(keys, documents)
            case name if extension == ".png":
                stan(keys, pngs)
            case name if extension == ".gif":
                stan(keys, gif)
            case name if extension == ".webp":
                stan(keys, rdt)


            case name if extension in (".mp4", ".mov") and len(name) == 16:
                stan(keys, twt)
            case name if extension in (".mp4", ".mov") and len(name) == 110:
                stan(keys, messenger_videos)
            case name if extension in (".mp4", ".mov"):
                stan(keys, videos)
            case name if extension in (".mp3", ".wav"):
                stan(keys, audio)


            case name if extension in (".jpg", ".jpeg", ".heic"):
                stan(keys, images) #least prioritized

            
            case _:
                print(f"Skipped {file}")
        
        
        
            

sort_files()