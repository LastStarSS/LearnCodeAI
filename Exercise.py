import cv2
import os
import argparse
import numpy as np

def resize_padding_image(img,target_size):
    h0, w0, _ = img.shape
    target_h, target_w = target_size
    scale = min(target_h/h0,target_w/w0)
    new_h = int(scale*h0)
    new_w = int(scale*w0)
    resized_img = cv2.resize(img, (new_w, new_h))
    img_out = np.zeros((target_h, target_w, 3), dtype=np.uint8)
    y_offset = (target_h - new_h)//2
    x_offset = (target_w - new_w)//2
    img_out[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized_img
    return img_out

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="Đọc và hiển thị một bức ảnh sử dụng OpenCV.")
    parser.add_argument('--image_path', type=str, help='Đường dẫn đến bức ảnh cần đọc và hiển thị')
    args = parser.parse_args()
    img = cv2.imread(args.image_path)
    output_image = resize_padding_image(img,(960,960))
    print(output_image.shape)
    print(output_image)
    cv2.imshow('Output', output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()