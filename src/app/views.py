from src.app import app
from src.lib import Foo


@app.route('/')
def index():
    return Foo().bar()
