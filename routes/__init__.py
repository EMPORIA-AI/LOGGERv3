#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: Elastic-2.0
# Copyright (c) 12020 - 12022 HE, Emporia.AI Pte Ltd

__banner__ = """













""" # __banner__

import trio, asks, json

from pydantic.json import pydantic_encoder

from quart import abort

async def manage_post(outgoing):
    url = "http://127.0.0.1:10000/api/engine/v1/MANAGE"
    headers = {'Content-Type': 'application/json'}
    encoded = json.dumps(outgoing, default=pydantic_encoder)
    response = await asks.post(url, data=encoded, headers=headers)
    if not response.status_code == 200:
        abort(response.status_code)
    return json.loads(response.content)


