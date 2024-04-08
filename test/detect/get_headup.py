from ultralytics import YOLO, settings
import json

weights = r"test\weights\raise_hand_best.pt"
source = r"test\source\camera.jpg"

json_settings = json.dumps(settings, indent=4)

print(json_settings)


model = YOLO(weights)
results = model(source=source)

def print_by_name(category, name):
    print(f"{name}:\n {category}")

for result in results:
    boxes = result.boxes
    masks = result.masks
    keypoints = result.keypoints
    probs = result.probs
    print_by_name(boxes, "boxes")
    print_by_name(masks, "masks")
    print_by_name(keypoints, "keypoints")
    print_by_name(probs, "probs")
    result.show()
    result.save(filename="runs/result.jpg")