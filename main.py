from PIL import Image
from numpy import ones, multiply, flip

filename = 'DS1.txt'                                    # Name of dataset file
result_filename = 'result.png'                          # Name of result file
canvas_size = (540, 960)                                # Canvas size of image


def main():
    with open(filename) as file:                        # Work with file
        canvas_size_ext = canvas_size + tuple([3])      # Add RGB-mask part
        mask = ones(canvas_size_ext, dtype='uint8')     # Create numpy array fill with ones

        file_array = file.read()                        # Read all data from file in to array
        file_array = file_array[:-1]                    # Delete last '\n' from array
        file_array = file_array.split('\n')             # Split coordination by '\n'

        coords = [x.split(' ') for x in file_array]     # Split coord from 1d array to 2 2d array
        coords = [[int(y) for y in x] for x in coords]  # Convert str coord to int coord

        for coord_x, coord_y in coords:                 # Work with coordination's
            mask[coord_x, coord_y] = [0, 0, 0]          # Change color of right pixels to black

        image = multiply(mask, 255)                     # Scale data from [0, 1] to [0, 255]
        image = flip(image, 0)                          # Reverse data array (flip image)
        image = Image.fromarray(image)                  # Create image from data array
        image.show()                                    # Show the result image
        image.save(result_filename)                     # Save the result image


if __name__ == '__main__':
    main()
