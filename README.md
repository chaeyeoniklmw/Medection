# Medection
GDG on SWU AI/ML solo project

# Pill Detection and Function Explanation System

## 🚀 Service Introduction
Our system is designed to assist individuals who are unfamiliar with their medication. By simply taking a picture of a pill packet, the system detects the type of medication and provides a detailed explanation of its function. Additionally, the system analyzes the combined functionality of the detected pills, offering insights into the overall treatment purpose.




### ✨ Features:
- **Pill Detection**: Automatically identify pills using state-of-the-art detection models.
- **Function Explanation**: Understand what each pill does and the purpose of the prescribed combination.
- **User Benefits**: Reduces the hassle of revisiting the hospital for a repeat prescription by tracking previously prescribed medications.
  

---

## 🎯 Our Goal
- Compare **three cutting-edge object detection models**: YOLOv8, Faster R-CNN, and RetinaNet, to identify the best-performing model for pill detection.
- Achieve accurate detection of individual pills.
- Expand functionality to detect pill packets and infer their purpose in real-world settings.


---

## 🛠️ Tech Stack
| Component                  | Technology/Tool       |
|----------------------------|-----------------------|
| **Object Detection Models**| YOLOv8, Faster R-CNN, RetinaNet |
| **Programming Language**   | Python               |
| **Frameworks**             | PyTorch, TensorFlow  |
| **Frontend**               | Streamlit            |
| **Visualization**          | Matplotlib, OpenCV   |
| **Data Labeling & Dataset Management** | Roboflow            |
| **Deployment**             | Docker, AWS/GCP      |

---

## 🎥 Demo
### Pill Detection in Action
1. **Step 1**: Upload an image of the pill packet.
2. **Step 2**: The system detects individual pills and highlights them with bounding boxes.
3. **Step 3**: Provides detailed descriptions of detected pills and their combined purpose.




Stay tuned for a live demo link! 🚧

---

## 📊 Performance

### Object Detection Model Comparison
| Model              | mAP50    | mAP50-95 |
|--------------------|----------|----------|
| **YOLOv8**         | 0.724    | 0.509    |
| **Faster R-CNN**   | TBD      | TBD      |
| **RetinaNet**      | TBD      | TBD      |

### Model Evaluation
- **YOLOv8** has shown strong results in detecting pills with a higher mAP50 score compared to other models.
- We are currently evaluating Faster R-CNN and RetinaNet for their performance on pill detection tasks.
