"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "27896987")
        self.API_HASH: str = os.environ.get("API_HASH", "0e017f716c49a52a0ba4a8bfa95ccaf7")
        self.SESSION: str = os.environ.get("SESSION", "BQGprJsAbiylno94JMpniyLv-T7g-DBRrgquKU-MRiGeVvjBI1soY2k7hfT-fdAQTIEGvluCHMXdmGMTVsTNpNkWrwSrZjuodfVw5mTrbL5332ALoj3jlz-shHbnGy10nVdv768j_SZ2qSbigawZP9G2BJmGA42pesuMIrWLaDcOdS5Pj1E3BQKnf_cpeytkOLwk-Vk7Qg-B49I871I46V4WK0jVA8USdzdfg7m47H8SIqLKpkGbOH-vHAVLByekaHYzOPhytDak4i3o3FOl6vMgkyIaDRtFYrFI6DTZ6HjGk3QzCZUaSBDfnWGJpGIxYTIigkndzIAKsCOD-CLEscvEKAAAAAGlQmcFAA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "7223926558:AAH-0Z2AIcyI6W3g8F-SuV06gBMzc07G_xM")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", " ").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", "27154e86e4e04c909ad65020dc190fef")
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", "97f9882ce54e47a49d27eab94d580075")


config = Config()
