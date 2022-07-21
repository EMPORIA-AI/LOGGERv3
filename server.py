#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: Elastic-2.0
# Copyright (c) 12020 - 12022 HE, Emporia.AI Pte Ltd

__banner__ = """













""" # __banner__

from cubed4th import FORTH

import os, re, rich, trio, toml, asks, redio, json

import zlib, pickle, sqlite3, pendulum

from hypercorn.trio import serve
from hypercorn.config import Config

from quart import Quart, Blueprint, abort
from quart_trio import QuartTrio
from quart_schema import QuartSchema, validate_request, validate_response

from dotenv import load_dotenv
load_dotenv(verbose=True)

app = QuartTrio("TAIM_LOGGER")
QuartSchema(app, version="0.42.10", title="")

from common import *

#import routes.value
#app.register_blueprint(routes.value.blueprint)

async def app_worker():
    pass
    # while True:
    #     async with trio.open_nursery() as nursery:
    #         for name, emporium in markets.items():
    #             nursery.start_soon(emporium.maintain)

async def app_serve(*args):
    async with trio.open_nursery() as nursery:
        nursery.start_soon(serve, *args)
        nursery.start_soon(app_worker)

config = Config()
config.bind = [os.getenv("TAIM_BIND", "0.0.0.0:10001")]

#from pathlib import Path
#p = Path(f"config_9.txt");
#if p.exists(): p.unlink()
#i = 8
#while i >= 0:
#    p = Path(f"config_{i}.txt")
#    if p.exists():
#        p.rename(Path(f"config_{i+1}.txt"))
#    i -= 1

from loggify import Loggify
with Loggify("config_0.txt"):
    trio.run(app_serve, app, config)

