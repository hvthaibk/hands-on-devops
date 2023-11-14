# OCR app

## Tesseract

To build a docker image for tesseract v5
```
docker build --progress plain -t tesseract:v5 ./ocr
```

Convert an image to text
```
docker run --rm -it --name tesseract5 -v "$PWD":/app -w /app tesseract:v5 tesseract ocr/data/image.jpeg stdout
```

## pytesseract

```
python ./ocr/app_ocr.py --file_name=./ocr/data/image.jpeg
```
