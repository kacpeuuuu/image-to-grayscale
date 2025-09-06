from PIL import Image
import sys
import os


def to_grayscale(path_to_file, path_output):
    im = Image.open(path_to_file)
    width, height = im.size

    im = im.convert("RGB")

    new_img = Image.new("RGB", (width, height))
    src_pixels = im.load()
    dst_pixels = new_img.load()

    for x in range(width):
        for y in range(height):
            r, g, b = src_pixels[x, y]
            gray = int(r * 0.299 + g * 0.587 + b * 0.114)
            dst_pixels[x, y] = (gray, gray, gray)

    new_img.save(path_output)
    print(f"Saved grayscale image to {path_output}")


def main():
    if len(sys.argv) != 3:
        print("USAGE:")
        print("  python main.py <input_image> <output_basename>")
        print("\nExample:")
        print("  python main.py input.png output")
        print("  - creates output.jpg in the current folder")
        
        sys.exit(1)

    input_file = sys.argv[1]
    output_base = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Error: input file '{input_file}' not found.")
        print("\nUSAGE: python main.py <input_image> <output_basename>")
        sys.exit(1)

    to_grayscale(input_file, output_base)


if __name__ == "__main__":
    main()