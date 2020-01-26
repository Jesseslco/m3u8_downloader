import os

# proxy = None
proxy = {"http":"http://127.0.0.1:7890",
         "https":"http://127.0.0.1:7890"}

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
           'method': "GET"}



storage = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "storage"))
tmp = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "tmp"))


# Don't modify if you don't know what you're doing
request_config = {"proxy": proxy["http"],
                  "timeout": 10,
                  "verify_ssl": False} if proxy else {"timeout":10, "verify_ssl":False}

session_config = {"headers": headers,}
# End
