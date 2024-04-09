from argparse import ArgumentParser
from openapi_ts import generate_client
from ..api import make_app

def main():

  parser = ArgumentParser()
  parser.add_argument('--package-path', help="Path to the typescript package's base folder", required=True)
  args = parser.parse_args()

  app = make_app({}) # type: ignore
  spec = app.openapi()
  generate_client(spec, args.package_path)
