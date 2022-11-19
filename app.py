from robyn import Robyn, static_file
from dotenv import load_dotenv
import os

app = Robyn(__file__)

load_dotenv()

PORT = os.environ.get('PORT')

@app.get("/hello")
async def h(request):
    print(request)
    return "Hello, world!"

@app.get("/")
async def get_page(request):
    return static_file("./index.html")


app.start(url="0.0.0.0",port=PORT)    