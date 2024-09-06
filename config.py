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
        self.SESSION: str = os.environ.get("SESSION", "BQBa9TG4pi1R_fPMS7gqzjSsny6EYv70dsx_NiXsdfg8Ou1rpGw7mbt_srQtpw3z7PvWX2YcPnH0QXRMVZesgzy53sKP3Mf-3aeYRi1VazYnUzaO0J0v5fN6kBzi1u_skICRaue2Vj0uwllV5-_NwiRx13GbaKqk8ZbA0NjPwtou-GnMJDj324ZIwqnQrNckbGHvG_H9SdPsJ6D8FdKcoL3Ih2qNffYF8snCAnLdlAcd8iUF0fwc-8oHmAADuCg3TFDSAGwnFGQuQP90q8L0d8kIhEOtdeoNkqVdCgOv62zivKGYs5XL7L0sOSiDUNwiBSRkPnAeo-E6n7ZH8eGL8KOaAAAAAaVCZwUA")
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
