import glob


class Consumer:
    def __init__(self, working_directory) -> None:
        self.index = 0
        self.working_directory = working_directory
        self.filenames = []
        
    def check_new_images(self):
        for image_format in ['jpg', 'png']:
            images_list = glob.glob(self.working_directory+"*."+image_format)
            self.filenames += [x for x in images_list if x not in self.filenames]

    def poll(self):
        self.check_new_images() 
        try:
            self.filenames[self.index]
        except IndexError as ie:
            return None 
        index = self.index
        self.index += 1
        return self.filenames[index]
            
    

if __name__ == "__main__":
    pass 