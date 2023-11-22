import cv2

# Get the path to the DAV file
video_path = "C:\\Users\\hjorquera\\Desktop\\DAV\\NVR_ch1_main_20230131000000_20230131010000.dav"

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video file is opened successfully
if not cap.isOpened():
    print("Error opening video file")
    exit(1)

# Get the frame width and height
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Create a window to display the video frames
cv2.namedWindow("Video")

# Create a while loop to read and display the video frames
while True:
    # Read the next frame from the video file
    ret, frame = cap.read()

    # Check if the end of the video file is reached
    if not ret:
        break

    # Display the frame
    cv2.imshow("Video", frame)

    # Wait for a key press
    key = cv2.waitKey(1)

    # If the key `q` is pressed, break out of the loop
    if key == ord("q"):
        break


# Close the video file
cap.release()

# Destroy the window
cv2.destroyWindow("Video")

