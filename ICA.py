import argparse
from PIL import Image

def compress_image(input_image_path, output_compressed_path):
    try:
        # Read the image
        image = Image.open(input_image_path)
        image = image.convert("RGB")  # Convert image to RGB mode if not already in RGB mode
        width, height = image.size

        # Open the output file
        with open(output_compressed_path, 'w') as f:
            # Write width and height to the file
            f.write(f"{width} {height}\n")

            # Iterate over each pixel and write its location and color
            for y in range(height):
                for x in range(width):
                    # Get the RGB values of the pixel
                    r, g, b = image.getpixel((x, y))
                    # Write pixel location (x, y) and color (R, G, B) to the file
                    f.write(f"{x} {y} {r} {g} {b}\n")

        print("Image compressed and saved as", output_compressed_path)
    except Exception as e:
        print("Error compressing image:", e)

def decompress_image(input_compressed_path, output_image_path):
    try:
        # Open the input compressed file
        with open(input_compressed_path, 'r') as f:
            # Read width and height from the file
            width, height = map(int, f.readline().split())

            # Create a new image with the specified width and height
            new_image = Image.new("RGB", (width, height))

            # Iterate over each line in the file
            for line in f:
                # Extract pixel location (x, y) and color (R, G, B)
                x, y, r, g, b = map(int, line.split())
                # Set the pixel color in the new image
                new_image.putpixel((x, y), (r, g, b))

        # Save the decompressed image
        new_image.save(output_image_path)
        print("Image decompressed and saved as", output_image_path)
    except Exception as e:
        print("Error decompressing image:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compress or decompress an image file")
    parser.add_argument("mode", choices=["compress", "decompress"], help="Mode: 'compress' or 'decompress'")
    parser.add_argument("input_image", help="Path to the input image file")
    parser.add_argument("output", help="Path to the output file (compressed or decompressed)")
    args = parser.parse_args()

    if args.mode == "compress":
        compress_image(args.input_image, args.output)
    elif args.mode == "decompress":
        decompress_image(args.input_image, args.output)
