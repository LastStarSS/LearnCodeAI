# Annotation Tools Setup Guide

This guide provides step-by-step instructions to install and set up three popular annotation tools: **CVAT.ai**, **Labelme**, and **AnyLabeling**.

## CVAT.ai

1. Go to [https://cvat.ai](https://cvat.ai).
2. **Sign Up** or **Log In** using your credentials.
3. Go to **Projects**
4. Click on the **"+"** button and **"Create a New Project"** and enter a name and description.
5. Click **"Submit & Open"**
6. Click **"Constructor"** and **"Add label"**, give it a name, shape, and a color, and click **"Continue"**
7. In the project, click **"Create Task"**, enter  **Name**, choose a **Subset (train, test, or validation)** and upload images/videos for annotation.
8. Select an annotation format (e.g., **Bounding Boxes, Polygons, or Keypoints**) and annotate.
9. Once done, click **Save** or press **Ctrl + S** to save.
10. (Optional) Export the labeled dataset in formats like COCO, YOLO, or Pascal VOC.

## Labelme

### **Installation (Python)**

1. Install Python (3.5+).
2. Install Labelme via pip:
   ```sh
   pip install labelme
3. Run Labelme
   ```sh
   labelme
4. Choose a file and annotate

## Anylabelling

### **Installation (Python)**

1. Create conda environment (Python 3.10+, 3.12 is reccomended):
   ```sh
   conda create -n anylabeling python=3.12
   conda activate anylabeling
2. Install Anylabeling:
   ```sh
   pip install anylabeling
3. Install packages:
   ```sh
   pip install -r requirements-dev.txt
4. Generate resources:
   ```sh
   pyrcc5 -o anylabeling/resources/resources.py anylabeling/resources/resources.qrc
5. Run anylabeling:
   ```sh
   python anylabeling/app.py
