import cv2
import os

video_path = "/users/qiming/code/VideoLISA/examples/RBrZsgy4-SQ.mp4"
save_dir = "/users/qiming/code/VideoLISA/examples/RBrZsgy4-SQ"

# make output folder
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)

frame_idx = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break  # no more frames

    # save frame
    save_path = os.path.join(save_dir, f"{frame_idx:05d}.png")
    cv2.imwrite(save_path, frame)
    frame_idx += 1

cap.release()
print("Done! Saved", frame_idx, "frames.")
