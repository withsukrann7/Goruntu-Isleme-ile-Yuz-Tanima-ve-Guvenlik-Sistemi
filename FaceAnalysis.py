import cv2
from deepface import DeepFace
import numpy as np

cap = cv2.VideoCapture(0)
frame_count = 0

print("🎥 Kamera açıldı!")
print("Yüz landmarkları (işaret noktaları) gösterilecek")
print("'q' tuşuna bas -> Çık\n")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Her 5 frame'de bir analiz yap (daha akıcı olsun)
    if frame_count % 5 == 0:
        try:
            # Yüz landmarklarını çıkar
            face_objs = DeepFace.extract_faces(frame, 
                                               detector_backend='retinaface',  # En iyi landmark tespiti
                                               enforce_detection=False,
                                               align=False)
            
            for face_obj in face_objs:
                # Yüz bölgesi
                facial_area = face_obj['facial_area']
                x, y, w, h = facial_area['x'], facial_area['y'], facial_area['w'], facial_area['h']
                
                # Yüz dikdörtgeni
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                # Landmarklar varsa çiz
                if 'landmarks' in face_obj and face_obj['landmarks']:
                    landmarks = face_obj['landmarks']
                    
                    # Sol göz
                    if 'left_eye' in landmarks:
                        left_eye = landmarks['left_eye']
                        cv2.circle(frame, tuple(left_eye), 3, (0, 255, 255), -1)
                        cv2.putText(frame, "Sol Goz", (left_eye[0]+5, left_eye[1]-5),
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 1)
                    
                    # Sağ göz
                    if 'right_eye' in landmarks:
                        right_eye = landmarks['right_eye']
                        cv2.circle(frame, tuple(right_eye), 3, (0, 255, 255), -1)
                        cv2.putText(frame, "Sag Goz", (right_eye[0]+5, right_eye[1]-5),
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 1)
                    
                    # Burun
                    if 'nose' in landmarks:
                        nose = landmarks['nose']
                        cv2.circle(frame, tuple(nose), 3, (255, 0, 0), -1)
                        cv2.putText(frame, "Burun", (nose[0]+5, nose[1]-5),
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)
                    
                    # Sol ağız köşesi
                    if 'mouth_left' in landmarks:
                        mouth_left = landmarks['mouth_left']
                        cv2.circle(frame, tuple(mouth_left), 3, (255, 0, 255), -1)
                    
                    # Sağ ağız köşesi
                    if 'mouth_right' in landmarks:
                        mouth_right = landmarks['mouth_right']
                        cv2.circle(frame, tuple(mouth_right), 3, (255, 0, 255), -1)
                        
                        # Ağız çizgisi
                        if 'mouth_left' in landmarks:
                            cv2.line(frame, tuple(mouth_left), tuple(mouth_right), (255, 0, 255), 2)
                            cv2.putText(frame, "Agiz", (mouth_right[0]+5, mouth_right[1]),
                                       cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 255), 1)
                    
                    # Göz arası mesafe çizgisi
                    if 'left_eye' in landmarks and 'right_eye' in landmarks:
                        cv2.line(frame, tuple(left_eye), tuple(right_eye), (0, 255, 0), 1)
                        eye_distance = np.linalg.norm(np.array(left_eye) - np.array(right_eye))
                        cv2.putText(frame, f"Goz mesafesi: {int(eye_distance)}px", (10, 30),
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    
                    # Yüz genişliği
                    cv2.putText(frame, f"Yuz genisligi: {w}px", (10, 60),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    
                    # Yüz yüksekliği
                    cv2.putText(frame, f"Yuz yuksekligi: {h}px", (10, 90),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    
        except Exception as e:
            cv2.putText(frame, "Yuz bulunamadi", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    frame_count += 1
    cv2.imshow('Yuz Landmarklari', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("👋 Kamera kapatıldı!")