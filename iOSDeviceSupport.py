#!/usr/bin/env python
import os
import sys
import requests
import argparse
import zipfile
from os import listdir, path

print('\n')
print('██  ██████  ███████     ██████  ███████ ██    ██ ██  ██████ ███████     ███████ ██    ██ ██████  ██████   ██████  ██████  ████████ ')
print('██ ██    ██ ██          ██   ██ ██      ██    ██ ██ ██      ██          ██      ██    ██ ██   ██ ██   ██ ██    ██ ██   ██    ██')
print('██ ██    ██ ███████     ██   ██ █████   ██    ██ ██ ██      █████       ███████ ██    ██ ██████  ██████  ██    ██ ██████     ██')
print('██ ██    ██      ██     ██   ██ ██       ██  ██  ██ ██      ██               ██ ██    ██ ██      ██      ██    ██ ██   ██    ██')
print('██  ██████  ███████     ██████  ███████   ████   ██  ██████ ███████     ███████  ██████  ██      ██       ██████  ██   ██    ██')
print('--------------------------------------------------------------------------------------------------------------------- for xCode')
print('\n')
print('                                     Mogbil Sourketti, wondtech.com, info[a]wondtech.com')
print('\n')
input('To Continue, Press any Button...')
print('\n')

url = 'http://mog.wondtech.com/DeviceSupport.zip'
file_name = "DeviceSupport.zip"
with open(file_name, "wb") as f:
    print("Downloading %s" % file_name)
    response = requests.get(url, stream=True)
    total_length = response.headers.get('content-length')

    if total_length is None:
        f.write(response.content)
    else:
        dl = 0
        total_length = int(total_length)
        for data in response.iter_content(chunk_size=4096):
            dl += len(data)
            f.write(data)
            done = int(50 * dl / total_length)
            sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
            sys.stdout.flush()

if os.path.exists('DeviceSupport.zip'):
    zip = zipfile.ZipFile('DeviceSupport.zip', 'r')
    zip.extractall()
    zip.close()
else :
    die('DeviceSupport.zip not exists\n')

SRC = path.join(path.dirname(path.abspath(__file__)), 'DeviceSupport')
DEVICE_SUPPORT_PATH='Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport'

def unzip_file(name, target):
  f = path.join(SRC, name + '.zip')
  zip_ref = zipfile.ZipFile(f, 'r')
  zip_ref.extractall(target)
  zip_ref.close()

def process(xcode, version):
  target = path.join(xcode, DEVICE_SUPPORT_PATH)
  exist = listdir(target)
  all_files = [i.replace('.zip', '') for i in listdir(SRC) if i.endswith('.zip')]
  new_files = list(set(all_files) - set(exist))

  if version:
      new_files = list(filter(lambda x : version in x, new_files))

  for i in new_files:
    unzip_file(i, target)
  print ('\nUpdate Successfully\n')

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '-t',
    type=str,
    dest='target',
    default='/Applications/Xcode.app',
    help='The path for Xcode'
  )
  parser.add_argument(
    '-v',
    type=str,
    dest='version',
    default=None,
    help='Specific version (default is all)'
  )
  args = parser.parse_args()
  process(args.target, args.version)