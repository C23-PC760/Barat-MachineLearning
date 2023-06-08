import os

class Image_Processor:
    def __init__(self, image_file):
        self.file = image_file
        self.path = ''
    
    def save(self, dst_path, filename):
        dst_directory = os.path.join(os.getcwd(), '{}/{}'.format(dst_path, filename))
        
        self.file.save(dst_directory)
        
        if os.path.exists(dst_directory):
            self.path = dst_directory
    
    def delete(self):
        if os.path.exists(self.path):
            os.remove(self.path)
            self.path = ''
