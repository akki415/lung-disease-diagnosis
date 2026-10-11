import torch
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from torchvision import transforms
from xray.model.architecture import NeuralNetwork  # Ensure this path is correct

app = FastAPI()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialize and load model weights
model = NeuralNetwork().to(device)
model.load_state_dict(torch.load("Xray_prediction_model.pth", map_location=device))
model.eval()

# Transformations
transform = transforms.Compose(
    [
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ]
)

# Prediction label mapping
label_map = {0: "Normal", 1: "Pneumonia"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    input_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(input_tensor)
        prediction_index = torch.argmax(output, dim=1).item()
        prediction_label = label_map.get(prediction_index, "Unknown")

    return {"prediction_index": prediction_index, "prediction_label": prediction_label}
