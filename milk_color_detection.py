import cv2
import numpy as np

def detect_defective_milk_packet(image_path):
    """
    Detects if a milk packet is defective based on brightness analysis.
    :param image_path: Path to the milk packet image
    """
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return
    
    # Convert the image to grayscale for brightness analysis
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate mean brightness of the grayscale image
    mean_brightness = np.mean(gray_image)
    print(f"Mean Brightness: {mean_brightness}")
    
    # Define a brightness threshold for defect detection
    # Adjust the threshold based on sample images
    acceptable_threshold = 200  # Typical brightness for non-defective packets
    
    # Determine if the packet is defective
    if mean_brightness < acceptable_threshold:
        print("Result: Defective Milk Packet Detected!")
    else:
        print("Result: Milk Packet is Normal.")
    
    # Display the image with a result title
    result = "Defective" if mean_brightness < acceptable_threshold else "Normal"
    cv2.putText(image, f"Packet: {result}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Milk Packet Analysis", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Test the function
if __name__ == "__main__":
    # Path to the milk packet image
    image_path = "T:\MYTechnicalWorks\Projects\Crion_Assignment\Milk_Color_Detection\milk.jpg"  # Replace with your actual image file path
    
    # Detect defects in the milk packet
    detect_defective_milk_packet(image_path)
