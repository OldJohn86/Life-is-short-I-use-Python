#!/usr/bin/env python3
#-*- coding: utf-8 -*-

__author__ = 'Jonathan Chen'
__date__   = '2019-10-21'
'''
async web application
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', headers={'content-type':'text/html'})

async def init(event_loop):
    app = web.Application(loop=event_loop)
    app.router.add_route("GET", "/", index)
    app_runner = web.AppRunner(app)
    await app_runner.setup()
    srv = await event_loop.create_server(app_runner.server, '127.0.0.1', 9000)
    logging.info("server started at http://127.0.0.1:9000...")
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

