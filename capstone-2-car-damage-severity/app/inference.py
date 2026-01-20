import numpy as np
import tensorflow as tf
from PIL import Image
from app.labels import CLASS_NAMES

# Load TFLite model ONCE
interpreter = tf.lite.Interpreter(
    model_path="model/car_damage_model.tflite"
)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


def preprocess(image: Image.Image) -> np.ndarray:
    image = image.resize((224, 224))
    x = np.array(image, dtype=np.float32)

    # MobileNetV2 preprocessing
    x = (x / 127.5) - 1.0
    return np.expand_dims(x, axis=0) # This adds batch dimension


def predict(image: Image.Image, threshold: float = 0.6) -> dict:
    x = preprocess(image)

    interpreter.set_tensor(input_details[0]["index"], x)
    interpreter.invoke()

    probs = interpreter.get_tensor(
        output_details[0]["index"]
    )[0]

    confidence = float(np.max(probs))
    idx = int(np.argmax(probs))

    """
    # Testing logic here, will update in subsequent sprints 
    if confidence < threshold:
        return {
            "status": "reject",
            "reason": "low_confidence_or_not_a_car",
            "confidence": confidence,
        }
    """

    return {
        "status": "ok",
        "severity": CLASS_NAMES[idx],
        "confidence": confidence,
        "scores": {
            CLASS_NAMES[i]: float(probs[i])
            for i in range(len(CLASS_NAMES))
        },
    }
