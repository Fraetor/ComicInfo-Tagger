# ComicInfo Tagger
Scraps metadata for manga, putting it in a ComicInfo.xml file.
It will also put all of the files into a CBZ archive, and optionally encode images as JPEG XL.

## To Do
- Determine if Cloudflare is going to be an issue, and work around it if it will be.
- Impliment XML output in api_consumer.py
- Make main.py that reads in the directory name and writes ComicInfo.xml.
- Extend so it also zips the files into a CBZ archive.
- Look into python jxl encoder, maybe fall back to cjxl.
