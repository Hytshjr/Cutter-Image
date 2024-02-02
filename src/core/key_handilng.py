import cv2

class KeyPress:
    def __init__(self, editor_instance):
        self.editor = editor_instance

    def main_key(self):
         while cv2.waitKey(1) != -1:
            k = cv2.waitKey(1)

            if k != -1:
                print(k)

                if k == ord('l'):
                    print('l')

                elif k == 27:
                    print('esq')

                elif k == ord('s'):
                    print('s')

