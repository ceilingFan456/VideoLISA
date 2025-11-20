import os
import cv2
import math

def compute_psnr(img1, img2):
    mse = ((img1.astype("float") - img2.astype("float")) ** 2).mean()
    if mse == 0:
        return float('inf')
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

folderA = "/users/qiming/code/VideoLISA/vis/RBrZsgy4-SQ"
folderB = "/users/qiming/code/VideoLISA/vis_frames/RBrZsgy4-SQ"

filesA = sorted(os.listdir(folderA))

psnr_list = []

for name in filesA:
    pathA = os.path.join(folderA, name)
    pathB = os.path.join(folderB, name)

    if not os.path.exists(pathB):
        print(f"Skip {name}, not found in folderB")
        continue

    imgA = cv2.imread(pathA, cv2.IMREAD_COLOR)
    imgB = cv2.imread(pathB, cv2.IMREAD_COLOR)

    if imgA is None or imgB is None:
        print(f"Error reading {name}")
        continue

    # ensure same resolution
    if imgA.shape != imgB.shape:
        print(f"Skip {name}, size mismatch")
        continue

    psnr = compute_psnr(imgA, imgB)
    psnr_list.append(psnr)
    print(f"{name}: {psnr:.4f} dB")

# overall average
if psnr_list:
    print("\nAverage PSNR:", sum(psnr_list) / len(psnr_list))
