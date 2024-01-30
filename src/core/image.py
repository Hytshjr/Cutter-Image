from tkinter import filedialog
import cv2

class Editor():
    def __init__(self):
        pass
    

    def cut_image(self):
        file_path = filedialog.askopenfilename()
        name =  file_path[file_path.rfind('/')+1::]
        if name:
            image = cv2.imread(file_path)


        print(image)
    
    
    