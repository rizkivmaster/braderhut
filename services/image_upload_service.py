from common.storage import images_storage, thumbnails_storage



def start():
    images_storage.start()
    thumbnails_storage.start()

def stop():
    images_storage.stop()
    thumbnails_storage.stop()

def save_image(image):
