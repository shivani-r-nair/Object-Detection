import cv2
import os

video = cv2.VideoCapture("videos/bottle.mp4")
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

os.makedirs("frames", exist_ok=True)

for i in range(120):
    frame_no = int(i * total_frames / 120)
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_no)

    ret, frame = video.read()
    if ret:
        cv2.imwrite(f"frames/frame_{i}.jpg", frame)

video.release()
print("120 frames extracted!")