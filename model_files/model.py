from torchvision import models
import torch


class Model:
    def __init__(self, path):
        self.model = models.mobilenet_v2(pretrained=False)
        self.model.classifier[1] = torch.nn.Linear(
            in_features=1280, out_features=2, bias=True
        )
        self.model.load_state_dict(torch.load(path, map_location=torch.device("cpu")))
        self.model.eval()

    def __call__(self, image):
        return self.model(image)
