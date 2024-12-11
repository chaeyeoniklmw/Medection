# Medection
GDG on SWU AI/ML solo project

# Pill Detection and Function Explanation System
![image](https://github.com/user-attachments/assets/91105ea0-9116-4cf0-b0d5-687af01d8c5e)

## 🚀 Service Introduction
Our system is designed to assist individuals who are unfamiliar with their medication. By simply taking a picture of a pill packet, the system detects the type of medication and provides a detailed explanation of its function. Additionally, the system analyzes the combined functionality of the detected pills, offering insights into the overall treatment purpose.
- 약 포장지의 사진을 찍으면, 시스템이 약의 종류를 자동으로 인식하고 해당 약의 기능에 대한 자세한 설명을 제공
- 여러 종류의 약물이 결합된 기능을 분석하여 전체적인 치료 목적에 대한 인사이트도 제공



### ✨ Features:
- **Pill Detection**: Automatically identify pills using state-of-the-art detection models.
- **Function Explanation**: Understand what each pill does and the purpose of the prescribed combination.
- **User Benefits**: Reduces the hassle of revisiting the hospital for a repeat prescription by tracking previously prescribed medications.
  
- **알약 탐지**: 최첨단 탐지 모델을 사용해 알약을 자동으로 인식합니다.
- **기능 설명**: 각 알약이 무엇을 하는지, 처방된 약물 조합의 목적을 이해할 수 있습니다.
- **사용자 혜택**: 이전에 처방된 약물을 추적하여 병원에 다시 방문할 필요를 줄여줍니다.

---

## 🎯 Our Goal
- Compare **three cutting-edge object detection models**: YOLOv8, Faster R-CNN, and RetinaNet, to identify the best-performing model for pill detection.
- Achieve accurate detection of individual pills.
- Expand functionality to detect pill packets and infer their purpose in real-world settings.
  
- **YOLOv8, Faster R-CNN, RetinaNet** 세 가지 최신 객체 탐지 모델을 비교하여 알약 탐지에 가장 적합한 모델을 선정합니다.
- **개별 알약의 정확한 탐지**를 목표로 합니다.
- 실제 환경에서 **알약 포장지 탐지** 및 **약물 목적 추론** 기능을 확장합니다.

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

### 👼 Development (+)
- FasterR-CNN 과 RetinaNet 모델 개발
- 배포까지 ... 
