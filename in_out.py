import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', required=True, type=str, help='Video url: -u https://youtube.com/asdasdasd')
parser.add_argument('-o', required=True, default='pose', type=str, help='Output folder: -o videos')
parser.add_argument('-w', required=True, default='pose', type=str, help='Website of origin: -w <youtube>')
parser.add_argument('--playlist', action='store_true', help='If the specified url is a playlist')

def parse_args():
	args = vars(parser.parse_args())
	return args['u'], args['o'], args['w'], args['playlist']
