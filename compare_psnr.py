import os
import cv2
import math

def compute_psnr(img1, img2):
    mse = ((img1.astype("float") - img2.astype("float")) ** 2).mean()
    if mse == 0:
        return float('inf')
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

folderA = "/users/qiming/code/VideoLISA/vis_frames/video_0000___01_franka___00011_2023-07-07_0011_left"
folderB = "/users/qiming/robot_data/final_test_set/roboengine_test_video_videolisa/mask/video_0000___01_franka___00011_2023-07-07_0011_left/000"

filesA = sorted(os.listdir(folderA))
filesB = sorted(os.listdir(folderB))

psnr_list = []

len_files = min(len(filesA), len(filesB))

for i in range(len_files):
    pathA = os.path.join(folderA, filesA[i])
    pathB = os.path.join(folderB, filesB[i])

    print(f"pathA: {pathA}, pathB: {pathB}")

    if not os.path.exists(pathB):
        print(f"Skip {filesA[i]}, not found in folderB")
        continue

    imgA = cv2.imread(pathA, cv2.IMREAD_COLOR)
    imgB = cv2.imread(pathB, cv2.IMREAD_COLOR)

    if imgA is None or imgB is None:
        print(f"Error reading {filesA[i]}")
        continue

    # ensure same resolution
    if imgA.shape != imgB.shape:
        print(f"Skip {filesA[i]}, size mismatch")
        continue

    psnr = compute_psnr(imgA, imgB)
    psnr_list.append(psnr)
    print(f"{filesA[i]}: {psnr:.4f} dB")

# overall average
if psnr_list:
    print("\nAverage PSNR:", sum(psnr_list) / len(psnr_list))
