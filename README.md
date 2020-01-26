# m3u8_downloader
asynchronous download video via m3u8 url or m3u8 file

[![HitCount](http://hits.dwyl.io/Jesseslco/m3u8_downloader.svg)](http://github.com/Jesseslco/m3u8_downloader)
[![HitCount](https://img.shields.io/github/downloads/Jesseslco/m3u8_downloader/total.svg?color=green)](https://github.com/Jesseslco/m3u8_downloader/releases)

 
## Requirments

#### Package
* python3.8 required

* ffmpeg required
> eg: `sudo apt-get update && sudo apt-get install ffmpeg` 

#### Modules
* requests
* m3u8
* asyncio
* aiohttp
* aiofile
* ffmpeg-python
> you can install these modules via `pip install -r requirements.txt`

## How to use
1. clone the project or download directly
> `git clone https://github.com/Jesseslco/m3u8_downloader.git`
2. cd M3U8/
3. `python3.8 manage.py`
4. you may need to overwrite some functions to fit your case
> there are two functions you could overwrite in lib/utils.py
   * parse_content(content)
   > some ts file needs to be decrypted, you should pass your decrption in this function
   * parse_ts_url(url)
   > some m3u8 playlist url may be not complete, like the below
   `/ext_tw_video/1221173105923674112/pu/vid/0/3000/320x568/nJjcKYgw_HuULFgC.ts`
   > in this case you should change this function
   ```
   def parse_ts_url(url):
     from urllib.parse import urljoin
     return urljoin("https://twitter.com", url)
   ```

## Proxy Support
use proxy is quite simple, just go to /config/setting.py
change proxy value (default = None), you are good to go.

## Feed Back
if you got any problem while using it, feel free to raise a issue. Thanks for using it.

