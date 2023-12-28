from enum import Enum


class ModelType(str, Enum):
    CLIP = "clip"
    FACIAL_RECOGNITION = "facial-recognition"
    IMAGE_CLASSIFICATION = "image-classification"

    def __str__(self) -> str:
        return str(self.value)
