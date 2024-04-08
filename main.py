from moveread.api import make_app
from moveread.local import LocalAPI
from moveread.sdk import MovereadAPI

core = LocalAPI.at('.data')
api = MovereadAPI(core)
app = make_app(api)