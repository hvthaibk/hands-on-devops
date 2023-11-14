import click
import cv2
import pytesseract


def image_to_string(file_name):
    """Simple script to run pytesseract."""
    image = cv2.imread(file_name)

    custom_config = r"--oem 3 --psm 6"
    string = pytesseract.image_to_string(image, config=custom_config)

    return string


@click.command()
@click.option("--file_name", default="./data/image.jpeg", help="Input file name.")
def main(file_name):
    """Main function."""
    print(image_to_string(file_name))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
