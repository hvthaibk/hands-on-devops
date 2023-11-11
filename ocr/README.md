# OCR app

## Tesseract

To build a docker image for tesseract v5
```
docker build --progress plain -t tesseract:v5 .
```

Convert an image to text
```
docker run --rm -it --name tesseract5 -v "$PWD":/app -w /app tesseract:v5 tesseract data/image.jpeg stdout
```
