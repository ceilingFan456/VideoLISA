#!/bin/bash

CUDA_VISIBLE_DEVICES=0 python chat_robot.py \
  --version="ZechenBai/VideoLISA-3.8B" \
  --vision_tower="openai/clip-vit-large-patch14-336" \
  --num_frames_dense=4 \
  --num_frames_sparse=32 \
  --save_overlay


# CUDA_VISIBLE_DEVICES=0 python chat.py \
#   --version="ZechenBai/VideoLISA-3.8B" \
#   --vision_tower="openai/clip-vit-large-patch14-336" \
#   --num_frames_dense=4 \
#   --num_frames_sparse=32 \
#   --save_overlay \
#   --vis_save_path="vis_frames"