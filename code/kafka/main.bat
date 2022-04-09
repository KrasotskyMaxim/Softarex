:: load models, get images, crop faces, recognize emotions, send result
start python -m service.main
:: send images
start python -m scripts.script
:: get result
start python -m scripts.label_consumer