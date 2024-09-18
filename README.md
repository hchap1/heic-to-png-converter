# heic-to-png-converter
Simple python script to convert a directory of .heic images to .png for sharing.

USAGE:
From within the directory where the python file is saved:
python(3) convert_heic_to_png.py path
Path can either be a directory or a singular file.
Uses concurrency, currently no progress meter so you will have to wait.
Takes around a second per file but does them all at once.
