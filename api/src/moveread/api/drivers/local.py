import os
from argparse import ArgumentParser

def main():
  import uvicorn
  from moveread.local import LocalAPI
  from moveread.sdk import MovereadAPI
  from ..api import app

  parser = ArgumentParser(description='Local Driver for the Moveread API')
  parser.add_argument('--base-path', type=str, required=True)
  parser.add_argument('--port', type=int, default=8000)
  parser.add_argument('--host', type=str, default='0.0.0.0')

  args = parser.parse_args()
  base_path = os.path.abspath(args.base_path)
  print(f"Starting Moveread API at '{base_path}'")

  core = LocalAPI.at(base_path)
  api = MovereadAPI(core)
  uvicorn.run(app(api), host=args.host, port=args.port)


if __name__ == '__main__':
  main()