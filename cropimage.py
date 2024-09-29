import cv2
import os
import argparse

def crop_image(img, bbox): 
    """ 
    Crop the given image using the provided bounding box. 
    Args: 
        img (numpy.ndarray): The image to crop. 
        bbox (tuple): The bounding box to use for cropping in the form (xmin, ymin, xmax, ymax). 
    Returns: 
        numpy.ndarray: The cropped image. 
    """ 
    xmin, ymin, xmax, ymax = bbox 
    return img[int(ymin):int(ymax), int(xmin):int(xmax)]

def main(args): 
    # Load the input image 
    img = cv2.imread(args.input_image) 
    if img is None: 
        print(f"Error: Unable to load image '{args.input_image}'.") 
        return 
    # Parse bounding box 
    bbox = tuple(args.bbox) 
    # Crop the image 
    cropped_img = crop_image(img, bbox) 
    # Save the cropped image
    cv2.imwrite(args.output_image, cropped_img) 
    print(f"Cropped image saved to {args.output_image}") 
    cv2.imshow('Cropped image', cropped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="Crop an image using a specified bounding box.") 
    parser.add_argument('--input_image', type=str, help="Path to the input image file.") 
    parser.add_argument('--output_image', type=str, help="Path to save the cropped image.") 
    parser.add_argument('--bbox', type=int, nargs=4, help="Bounding box coordinates as xmin ymin xmax ymax.") 
    args = parser.parse_args()
    main(args)