from robyn import Robyn, static_file
from dotenv import load_dotenv
import os

load_dotenv()


app = Robyn(__file__)


@app.get("/hello")
async def h(request):
    print(request)
    return "Hello, world!"


@app.get("/")
async def get_page(request):
    return static_file("./index.html")


app.start(port=5000, url="0.0.0.0")    