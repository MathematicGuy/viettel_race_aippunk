from typing import List
import torch
from PIL import Image
import clip


class MultimodalImageEncoder:
    """Encode images and text with CLIP embeddings"""

    def __init__(self, clip_model, clip_preprocess):
        self.clip_model = clip_model
        self.clip_preprocess = clip_preprocess
        self.device = "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"

        # Move model to device
        self.clip_model = self.clip_model.to(self.device)

    def encode_image_multimodal(self, image_path: str) -> List[float]:
        """Encode image into CLIP embedding vector"""
        try:
            image = Image.open(image_path).convert('RGB')
            image_input = self.clip_preprocess(image).unsqueeze(0).to(self.device)

            with torch.no_grad():
                image_features = self.clip_model.encode_image(image_input)
                image_features /= image_features.norm(dim=-1, keepdim=True)

            return image_features.squeeze().cpu().numpy().tolist()
        except Exception as e:
            print(f"Error encoding image {image_path}: {e}")
            # Return zero vector of appropriate dimension
            return [0.0] * 512  # CLIP's standard dimension

    def encode_text_for_image_search(self, text: str) -> List[float]:
        """Encode text into CLIP embedding vector for text-to-image search"""
        try:
            text_tokens = clip.tokenize(text).to(self.device)

            with torch.no_grad():
                text_features = self.clip_model.encode_text(text_tokens)
                text_features /= text_features.norm(dim=-1, keepdim=True)

            return text_features.squeeze().cpu().numpy().tolist()
        except Exception as e:
            print(f"Error encoding text '{text}': {e}")
            # Return zero vector of appropriate dimension
            return [0.0] * 512  # CLIP's standard dimension
