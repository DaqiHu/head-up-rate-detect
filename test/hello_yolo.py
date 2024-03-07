from ultralytics import YOLO, settings
import json

json_settings = json.dumps(settings, indent=4)

print(json_settings)


model = YOLO("yolov8n.pt")
results = model(source="bus.jpg")

print(type(results[0]))

for result in results:
    boxes = result.boxes
    masks = result.masks
    keypoints = result.keypoints
    probs = result.probs
    print(boxes, masks, keypoints, probs)
    result.show()
    result.save(filename="runs/result.jpg")