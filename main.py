from robyn import Robyn, static_file
from dotenv import load_dotenv
import os

load_dotenv()


app = Robyn(__file__)


@app.get("/")
async def h(request):
    print(request)
    return "Hello, world!"



app.start(port=5000)    