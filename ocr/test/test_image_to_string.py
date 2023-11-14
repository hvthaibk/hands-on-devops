from app_ocr import image_to_string


def test_image_to_string():
    """Test image_to_string()."""
    # arrange
    file_name = "./data/image.jpeg"
    expected = "\n".join(
        [
            "| T how TO WRITE ALT |",
            "TEXT AND IMAGE",
            "DESCRIPTIONS FOR",
            "THE VISUALLY",
            "| IMPAIRED",
            "\x0C",
        ]
    )

    # act
    string = image_to_string(file_name)

    # assert
    assert string == expected
