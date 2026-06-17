from mode_loader import get_model

model = get_model()

def get_embedding(text):
    return model.encode(text)