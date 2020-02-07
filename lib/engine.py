import asyncio
import aiohttp
from aiofile import AIOFile
from collections import namedtuple
from M3U8.config.setting import request_config, session_config, storage, tmp
from M3U8.lib import exceptions
import os
import ffmpeg
import logging

class M3U8(object):

    def __init__(self, playlists, output, parse_content):
        self._playlists = playlists
        self._config = {}

        self._output = os.path.join(storage, output)
        self._tmp = tmp
        self._logger = self._config_logger()
        self._parse_content = parse_content

    def _config_logger(self):
        logging.basicConfig()
        logger = logging.getLogger(name = __file__)
        logger.setLevel(logging.INFO)
        return logger

    def start(self):
        self._logger.info("Main engine start.")

        if self._validate() == False:
            raise exceptions.InvalidPlaylists()

        self._logger.info("Cleaning old file.")
        self._clean()

        self._logger.info("Assemble Tasks.")
        tasks = self._assemble(self._playlists)

        self._logger.info("Dump filelists.")
        self._dump_filelists(len(self._playlists))

        self._logger.info("Start download loop.")
        self._logger.info(f"Tasks: [{len(self._playlists)}]")
        asyncio.run(self._loop(tasks))

        self._logger.info("Finished download, start concating ts.")
        self._concat()

        self._logger.info("Almost done, start cleaning tmp files.")
        self._clean()

        self._logger.info("Successed.")

    def _validate(self):
        if self._playlists and (self._output != ''):
            return True
        return False

    def _assemble(self, playlists):
        Task = namedtuple('Task', ['url', 'file_name'])
        Tasks = []
        for index, value in enumerate(playlists):
            t = Task(url = value, file_name = os.path.join(self._tmp, f"{index}.ts"))
            Tasks.append(t)
        return Tasks

    async def _loop(self, tasks):
        async with aiohttp.ClientSession(**session_config) as session:
            tasks = [asyncio.create_task(self._ts_download(t.url, t.file_name, session)) for t in tasks]
            #[await t for t in tasks]
            responses = asyncio.gather(*tasks)
            await responses

    async def _ts_download(self, url, file_name, session):
        status = -1
        while status != 200:
            try:
                async with session.get(url = url, **request_config) as resp:
                    #assert resp.status == 200
                    status = resp.status
                    content = await resp.read()
                    content = self._parse_content(content)
            except Exception as e:
                self._logger.warning(e)
        await self._save_ts(file_name, content)

    async def _save_ts(self, file_name, content):
        async with AIOFile(file_name, "wb") as afp:
            await afp.write(content)
            await afp.fsync()

    def _dump_filelists(self, num_of_file):
        with open(os.path.join(self._tmp, 'filelists.txt'), 'a') as f:
            for i in range(num_of_file):
                f.write(f"file {i}.ts\n")

    def _concat(self):
        try:
            {
                ffmpeg
                .input(os.path.join(self._tmp, 'filelists.txt'), format = 'concat', safe = 0)
                .output(self._output, c = 'copy')
                .run()
            }
        except Exception as e:
            self._logger.warning(e)

    def _clean(self):

        tmp_files = os.listdir(tmp)
        for i in tmp_files:
            os.remove(os.path.join(tmp, i))


