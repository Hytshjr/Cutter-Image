import cv2

class MouseTracker:
    def __init__(self, editor_instance):
        self.editor = editor_instance
        self.img_pos = 0
        self.img = self.editor.img
        self.imgsize = self.img.shape
        self.img_show = self.editor.img
        self.coords = {}


    def main_track(self,event,x,y,flags, param):
        if event == 0:
            return
        self._scroll_track(event, flags)
        self._click_track(event, y)


    def _scroll_track(self, event, flags):
        if event == cv2.EVENT_MOUSEWHEEL:
            if flags > 0:
                self.img_pos -= 50
            else:
                self.img_pos += 50

            self.img_show = self._img_show(self.img_pos)
            self.editor._show_image(self.img_show)


    def _click_track(self,event, y):
        if event == cv2.EVENT_LBUTTONDOWN:
            color = (0, 255, 0)
            self._rect_pts(y)

            cv2.rectangle(
                self.img,
                self.coords['height'],
                self.coords['witdh'],
                color
                )

            self.editor._show_image(self.img_show)


            print(self.coords['height'])
            print(self.coords['witdh'])

            immg = self.img[self.coords['height'][0]:self.coords['height'][1],:]
            cv2.imshow('test',immg)


    def _img_show(self, position):
        pos_top = position
        pos_bottom = position+1080
        return self.img[pos_top:pos_bottom,:]



    def _rect_pts(self, y):
        if self.img_pos == 0:
            self.coords['height'] = (0,y)
        else:
            self.coords['height'] = (0,y+self.img_pos)

        self.coords['witdh']=(self.imgsize[1],0)


# def mouse_track(event,x,y,flags,param):
#     from gui.main_window import img_user

#     img      = img_user.img
#     name     = img_user.name
#     pos      = img_user.img_pos
#     size_img = img.shape
#     save_pxl = img_user.pxl_save


#     if event == cv2.EVENT_MOUSEWHEEL:
#         if flags > 0:
#             img_user.img_pos -= 50

#     if event == cv2.EVENT_MOUSEWHEEL:
#         if flags < 0:
#             img_user.img_pos += 50

#     cv2.imshow(name, img[pos:pos+1080,:])

    # if event == cv2.EVENT_LBUTTONDOWN:
    #     rect_pts = [(x, y)]

    #     rect_pts.append((size_img[1],0))
    #     rect_pts[0] = (0,rect_pts[0][1]+pos)

    #     cv2.rectangle(img, rect_pts[0], rect_pts[1], (0, 255, 0))

    #     img_user.pxl_save.append((0,rect_pts[0][1]))
    #     img_user.count += 1

    # else:
    #     if event == cv2.EVENT_LBUTTONDOWN:
    #         bottom_size = rect_pts[0][1]
    #         rect_pts[1] = (size_img[1],bottom_size)

    #         rect_pts[0] = (x, y)
    #         rect_pts[0] = (0,rect_pts[0][1]+pos)
    #         rect_pts[1] = (size_img[1],bottom_size)

    #         cv2.rectangle(img, rect_pts[0], rect_pts[1], (0, 255, 0))

    #         img_user.pxl_save.append((bottom_size,rect_pts[0][1]))

    #         count += 1


