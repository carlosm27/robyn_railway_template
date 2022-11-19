from robyn import Robyn, static_file
from dotenv import load_dotenv
import os

load_dotenv()
PORT = os.environ.get("PORT")

app = Robyn(__file__)


@app.get("/hello")
async def h(request):
    print(request)
    return "Hello, world!"


@app.get("/")
async def get_page(request):
    return static_file("./index.html")


app.start(port=PORT, url="0.0.0.0")    