from app.replicate_api import run_replicate
from app.utils import load_image

def generate_image(prompt):
    image_path = "./input/input.jpg"
    image = load_image(image_path)
    output = run_replicate(prompt, image)
    with open("output/output.jpg", "wb") as f:
        f.write(output)
    print("Imagem gerada com sucesso!")
