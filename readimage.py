import cv2
import argparse

def main():
    # Tạo đối tượng ArgumentParser
    parser = argparse.ArgumentParser(description="Đọc và hiển thị một bức ảnh sử dụng OpenCV.")
    
    # Thêm đối số đầu vào
    parser.add_argument('--image_path', type=str, help='Đường dẫn đến bức ảnh cần đọc và hiển thị')
    
    # Phân tích đối số
    args = parser.parse_args()
    
    # Đọc bức ảnh từ đường dẫn được cung cấp
    image = cv2.imread(args.image_path)
    
    # Kiểm tra nếu bức ảnh không được đọc thành công
    if image is None:
        print(f"Không thể đọc bức ảnh từ đường dẫn: {args.image_path}")
        return
    
    # Kiểm tra kiểu dữ liệu của image
    print(f"Type of image {type(image)}")

    # Kiểm tra kích thước của image
    height, width, channels = image.shape
    print(f"height = {height} width = {width} channels = {channels}")
    
    # Hiển thị bức ảnh
    cv2.imshow('Image', image)
    
    # Chờ nhấn phím để đóng cửa sổ hiển thị
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()