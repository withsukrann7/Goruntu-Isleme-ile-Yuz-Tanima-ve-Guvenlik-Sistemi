import cv2
import numpy as np
from deepface import DeepFace

MODEL_NAME = "Facenet512"
DETECTOR = "opencv"

def get_embedding(frame):
    reps = DeepFace.represent(
        frame,
        model_name=MODEL_NAME,
        detector_backend=DETECTOR,
        enforce_detection=False
    )
    if not reps:
        return None, None

    # tek yüz var dedin; yine de güvenli olsun diye ilkini alıyoruz
    rep = reps[0]
    emb = rep.get("embedding", None)
    fa = rep.get("facial_area", None)

    if emb is None:
        return None, fa

    return np.asarray(emb, dtype=np.float32), fa

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("🎥 Kamera açıldı")
print("SPACE: embedding yazdir | q: cikis\n")
print(f"Model={MODEL_NAME} Detector={DETECTOR}\n")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # yüz kutusu çizelim (hızlı olsun diye extract_faces yerine represent'in facial_area'sını kullanıyoruz)
    emb_preview, fa = get_embedding(frame)
    if fa:
        x, y, w, h = fa["x"], fa["y"], fa["w"], fa["h"]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f"{w}x{h}px", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.putText(frame, "SPACE=print embedding | q=quit", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow("Embedding Printer", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

    if key == ord(" "):  # SPACE
        emb, fa2 = get_embedding(frame)
        if emb is None:
            print("❌ Yuz bulunamadi / embedding cikmadi. Daha yakin dur veya isik arttir.\n")
            continue

        print("\n" + "=" * 70)
        print("✅ EMBEDDING CIKARILDI")
        print("=" * 70)
        print(f"Boyut (len): {len(emb)}")
        print(f"dtype: {emb.dtype}")
        if fa2:
            print(f"Face area: x={fa2['x']} y={fa2['y']} w={fa2['w']} h={fa2['h']}")
        print(f"Ilk 10:  {emb[:10].tolist()}")
        print(f"Son 10:  {emb[-10:].tolist()}")

        # komple yazdırmak istersen aç:
        print("\nTUM EMBEDDING:")
        print(emb.tolist())
        print("=" * 70 + "\n")

cap.release()
cv2.destroyAllWindows()
print("👋 Kapandi")
