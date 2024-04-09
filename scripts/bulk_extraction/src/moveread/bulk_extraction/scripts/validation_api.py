import os
from argparse import ArgumentParser
from moveread.sdk import MovereadAPI
from ..api import make_app

def local_app(base_path: str):
  api = MovereadAPI.at(base_path)
  blobs = os.path.join(base_path, 'blobs')
  return make_app(api, blobs_path=blobs)

def main():
  import uvicorn

  parser = ArgumentParser(description='Local Driver for the Moveread API')
  parser.add_argument('--base-path', type=str, required=True)
  parser.add_argument('--port', type=int, default=8000)
  parser.add_argument('--host', type=str, default='0.0.0.0')

  args = parser.parse_args()
  base_path = os.path.abspath(args.base_path)
  
  print(f"Starting Validation API at '{base_path}'")

  uvicorn.run(local_app(base_path), host=args.host, port=args.port)

if __name__ == '__main__':
  main()