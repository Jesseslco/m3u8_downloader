# m3u8_downloader

asynchronous download video via m3u8 url or m3u8 file

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

## Noticed
You may need to overwrite bin.demo.Demo 
   1. if your m3u8 url couldn't download directly

   2. or your m3u8 playlists url is not complete

      ```
         #EXTM3U
         #EXT-X-VERSION:6
         #EXT-X-MEDIA-SEQUENCE:0
         #EXT-X-TARGETDURATION:3
         #EXT-X-PLAYLIST-TYPE:VOD
         #EXT-X-ALLOW-CACHE:YES
         #EXTINF:3.000,
         /ext_tw_video/1234655732777308160/pu/vid/0/3000/480x270/fPisE__pmsx7k4sF.ts
         #EXTINF:3.000,
         /ext_tw_video/1234655732777308160/pu/vid/3000/6000/480x270/r_LS_GPI2BXX39I4.ts
         #EXTINF:3.000,
         /ext_tw_video/1234655732777308160/pu/vid/6000/9000/480x270/yYLlcdzb1XqRXUyc.ts
         #EXTINF:3.000,
         /ext_tw_video/1234655732777308160/pu/vid/9000/12000/480x270/iqaEsBByLBrdZ3IU.ts
         #EXTINF:3.000,
         /ext_tw_video/1234655732777308160/pu/vid/12000/15000/480x270/EGvmP4ThPwelrgHk.ts
         #EXTINF:1.963,
         /ext_tw_video/1234655732777308160/pu/vid/15000/16963/480x270/yh6vdCJRo6N-K_fT.ts
         #EXT-X-ENDLIST
      ```

      pass your own parse_ts_url() function

      ```python
         def parse_ts_url(self, url):
                 from urllib.parse import urljoin
                         url = urljoin("https://video.twimg.com", url)
                                 return url   	
      ```

   3.  your m3u8 ts segments may be decrypted,  pass your own parse_content() function
   
   
      ```python
         def parse_content(self, content):
              ##
              ## ...
              ##
            return content
      ```



Demo:

```python
class Demo(Downloader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def parse_file(self, file):
        with open(file, "r") as f:
            raw = f.read()
        m3u8_obj = m3u8.loads(raw)
        return m3u8_obj.segments.uri

    def parse_url(self, url):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
                   'method': "GET"}

        raw = requests.get(url, headers = headers).content.decode("utf-8")
        m3u8_obj = m3u8.loads(raw)
        playlists = m3u8_obj.segments.uri
        return list(map(self.parse_ts_url, playlists))

    def parse_ts_url(self, url):
        return url

    def parse_content(self, content):
        return content
```



