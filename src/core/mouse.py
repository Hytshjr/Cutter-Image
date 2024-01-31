import cv2

class MouseTrack:
    def __init__(self):
        pass

    def main_track(self,event,x,y,flags, param):
        from gui.main_window import img_user

        img      = img_user.img
        name     = img_user.name
        pos      = img_user.img_pos
        size_img = img.shape
        save_pxl = img_user.pxl_save



        if event == cv2.EVENT_MOUSEWHEEL:
            if flags > 0:
                img_user.img_pos -= 50

        if event == cv2.EVENT_MOUSEWHEEL:
            if flags < 0:
                img_user.img_pos += 50

        cv2.imshow(name, img[pos:pos+1080,:])

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


