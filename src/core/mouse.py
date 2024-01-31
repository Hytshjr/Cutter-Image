import cv2

class MouseTracker:
    def __init__(self, image, name):
        self.img = image
        self.name = name
        self.img_pos = 0
        self.imgsize = image.shape


    def main_track(self,event,x,y,flags, param):

        self._set_var(event, x, y, flags)
        self._scroll_track()
        self._click_track()


        cv2.imshow(self.name,self.img[self.img_pos:self.img_pos+1080,:])


    def _set_var(self,event, x, y, flags):
        self.x = x
        self.y = y
        self.event = event
        self.flags = flags


    def _scroll_track(self):
        if self.event == cv2.EVENT_MOUSEWHEEL:
            if self.flags > 0:
                self.img_pos -= 50
            else:
                self.img_pos += 50


    def _click_track(self):
        if self.event == cv2.EVENT_LBUTTONDOWN:

            rect_pts = self._rect_pts()

            cv2.rectangle(
                self.img,
                rect_pts[0],
                rect_pts[1],
                (0, 255, 0)
                )


    def _rect_pts(self):
        if self.img_pos == 0:
            height_slct = (0,self.y)
        else:
            height_slct = (0,self.y+self.img_pos)

        with_slct = (self.imgsize[0],0)
        return (height_slct, with_slct)

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


