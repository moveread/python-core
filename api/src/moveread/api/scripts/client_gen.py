from moveread.api import make_app
import os
import json
from argparse import ArgumentParser

def main():

  parser = ArgumentParser()
  parser.add_argument('--package-path', help="Path to the typescript package's base folder", required=True)
  args = parser.parse_args()

  app = make_app({}) # type: ignore
  spec = app.openapi()
  file = '/tmp/openapi.json'
  with open(file, 'w') as f:
    json.dump(spec, f)
  os.chdir(args.package_path)
  os.system(f'npx @hey-api/openapi-ts -i {file} -o src/')