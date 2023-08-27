import os


def remove_temp_files():
            
    for file in os.listdir("images/"):
        os.remove(os.path.join("images/",file))

    for file in os.listdir("images_color/"):
        os.remove(os.path.join("images_color/",file))

    for file in os.listdir("images_small/"):
        os.remove(os.path.join("images_small/",file))