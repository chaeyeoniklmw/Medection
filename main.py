from ultralytics import YOLO
import streamlit as st
from PIL import Image
import numpy as np
import time
import cv2  # OpenCV 사용

# YOLO 모델 로드
model = YOLO("yolov8_pill_model.pt")  # 훈련된 모델 경로로 수정

# 알약 분석 함수
def analyze_pill(image):
    # 이미지를 YOLO 모델에 입력하여 예측 결과 얻기
    results = model(image)
    
    # 결과에서 첫 번째 객체(알약) 정보 추출
    result_image = results[0].plot()  # 결과 이미지에 객체에 대한 박스를 그리기
    pill_info = []
    
    for i, box in enumerate(results[0].boxes.xywh):
        # 각 객체에 대한 정보 추출
        class_id = int(results[0].boxes.cls[i].item())  # 클래스 번호
        pill_name = f"알약 {class_id}"  # 클래스 번호에 따른 알약 이름 설정
        shape = "타원형"  # 예시 모양 (모델에 따라 모양을 추출할 방법 추가 가능)
        probability = results[0].boxes.conf[i] * 100  # 신뢰도
        
        pill_info.append({
            "name": pill_name,
            "shape": shape,
            "probability": probability.item()  # 신뢰도를 백분율로 표시
        })
    
    return result_image, pill_info

# Streamlit 인터페이스
st.title("**YOLOv8기반 알약 탐지 서비스**")
st.markdown("이미지를 업로드하거나 웹캠으로 캡처하여 알약을 분석하세요.")

# 입력 방식 선택을 사이드바에서 수행
st.sidebar.title("Option")
input_option = st.sidebar.radio("이미지 입력 방식 선택", ["이미지 업로드", "웹캠 캡처"])

if input_option == "이미지 업로드":
    # 이미지 업로드
    uploaded_file = st.file_uploader("알약 이미지를 업로드하세요.", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        # 분석 실행
        if st.button("분석 실행"):
            with st.spinner("알약 분석 중입니다. 잠시만 기다려주세요..."):
                time.sleep(2)  # 로딩 애니메이션 (모델 처리 시간 대체)
                result_image, pill_info = analyze_pill(image)

            # 이미지 비교를 위한 열 구성
            col1, col2 = st.columns(2)

            # 원본 이미지
            with col1:
                st.image(image, caption="업로드된 이미지", use_column_width=True)

            # 분석 결과 이미지
            with col2:
                st.image(result_image, caption="감지된 알약", use_column_width=True)

            st.markdown("### 감지된 알약 정보")
            
            # 알약 정보 출력
            for pill in pill_info:
                st.markdown(f"- **이름**: {pill['name']}")
                st.markdown(f"- **모양**: {pill['shape']}")
                st.markdown(f"- **신뢰도**: {pill['probability']:.2f}%")

elif input_option == "웹캠 캡처":
    # 웹캠을 통해 이미지 캡처
    run_camera = st.checkbox("웹캠 실행")
    captured_image = None

    if run_camera:
        st.warning("웹캠을 종료하려면 체크박스를 해제하세요.")
        cam = cv2.VideoCapture(0)
        while True:
            ret, frame = cam.read()
            if not ret:
                st.error("웹캠을 사용할 수 없습니다.")
                break
            # 화면에 현재 웹캠 화면 표시
            st.image(frame, channels="BGR")

            # 캡처 버튼
            if st.button("이미지 캡처"):
                captured_image = frame
                break

        cam.release()
        cv2.destroyAllWindows()

    if captured_image is not None:
        # 분석 실행
        if st.button("분석 실행"):
            with st.spinner("알약 분석 중입니다. 잠시만 기다려주세요..."):
                time.sleep(2)  # 로딩 애니메이션 (모델 처리 시간 대체)
                result_image, pill_info = analyze_pill(captured_image)

            # 이미지 비교를 위한 열 구성
            col1, col2 = st.columns(2)

            # 원본 이미지
            with col1:
                st.image(captured_image, caption="캡처된 이미지", channels="BGR", use_column_width=True)

            # 분석 결과 이미지
            with col2:
                st.image(result_image, caption="감지된 알약", use_column_width=True)

            st.markdown("### 감지된 알약 정보")
            
            # 알약 정보 출력
            for pill in pill_info:
                st.markdown(f"- **이름**: {pill['name']}")
                st.markdown(f"- **모양**: {pill['shape']}")
                st.markdown(f"- **신뢰도**: {pill['probability']:.2f}%")

# 하단 메뉴
st.sidebar.title("💡 도움말 및 피드백")
st.sidebar.info(
    """
    - 서비스를 사용해주셔서 감사합니다!
    - [피드백 남기기](https://docs.google.com/forms/d/e/1FAIpQLSdWsLju8YoCxx_14otWzEtk9derweK7fRqnmaNjJKB2CafD5Q/viewform?usp=dialog)
    """
)
