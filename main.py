if __name__ == "__main__":

    from robyn import Robyn
    from dotenv import load_dotenv
    import os

    load_dotenv()
    PORT = os.environ.get("PORT")
    Robyn.start(url="0.0.0.0", port=PORT)    