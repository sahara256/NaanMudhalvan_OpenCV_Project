# Naan Mudhalvan Project
# PROJECT OVERVIEW 

This repository contains OpenCV-based computer vision projects developed as part of the **Naan Mudhalvan** training program. Each project demonstrates real-world applications of image processing and AI in fields like e-commerce, drone vision, and environmental conservation.

### **Virtual Try-On System for E-Commerce**
**Description:**  
Allows customers to digitally try on clothing, accessories, or makeup on their own photo or live video feed, enhancing their online shopping experience.

- **Input:**  
  - User photo or webcam stream  
  - RGB front-facing images  

- **Output:**  
  - Rendered image/video with realistically overlaid clothes/accessories  
  - Dynamic positioning, scaling, and alignment with face or upper body  

**Applications:**  
- Virtual fitting rooms  
- Makeup or eyewear previews  
- Real-time AR shopping solutions  

---

### **Wildlife Monitoring and Conservation System**
**Description:**  
Tracks and detects animals in their natural habitats using camera trap footage and simple computer vision, aiding conservation efforts.

- **Input:**  
  - Images or videos from drones, traps, or field cameras  

- **Output:**  
  - Motion-based animal detection with bounding boxes  
  - Basic species labeling if integrated with classifiers

---

### **Capstone Project – Autonomous Drone Vision System**
**Description:**  
Enables drones to navigate and detect objects/obstacles autonomously using onboard cameras and computer vision algorithms.

- **Input:**  
  - Live drone video feed (RGB or IR)  

- **Output:**  
  - Object detection (people, obstacles, targets) with bounding boxes or segmentation  
  - Real-time decision support for navigation

---

##  Requirements

Ensure the following packages are installed:

```bash
pip install opencv-python numpy matplotlib
