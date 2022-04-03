import glob


def get_images_filenames_from_dir(dir_name: str, image_format: str = 'jpg') -> list:
    ''' Return a list of images filemanes from directory '''
    filenames = glob.glob(dir_name+"*."+image_format)
    filenames.sort()
    return filenames



if __name__ == "__main__":
    # Choose an image to detect faces in
    imgs = get_images_filenames_from_dir(dir_name="../face-input/", image_format="jpg")
    print(imgs)