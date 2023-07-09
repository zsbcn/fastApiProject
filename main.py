import time

import anyio
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from load_config import global_config
from router import all_router
from utils.logger import MyLogger

logger = MyLogger(__name__, global_config.load("log.level")).setConsole().getLogger()

# app对象
app = FastAPI(title="Test", docs_url=None, redoc_url=None)

# 静态文件位置
app.mount("/static", StaticFiles(directory="static"), name="static")

# 配置文件中docs=True，则启用接口文档，否则关闭接口文档
if global_config.load("docs"):
    docs_route = __import__("docs")
    app.include_router(getattr(docs_route, "route"))


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    t_start = time.time()
    response = await call_next(request)
    time_cost = time.time() - t_start
    logger.info(f"接口耗时{time_cost}")
    return response


@app.get("/")
async def root():
    await anyio.sleep(5)
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
    return {"message": f"Hello World{time.time()}"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# 导入所有的路由
app.include_router(all_router)
