import argparse
from app.img_pipeline import generate_image

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str, required=True, help="Descrição da imagem desejada")
    args = parser.parse_args()
    generate_image(args.prompt)
