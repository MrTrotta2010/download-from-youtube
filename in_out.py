import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', required=True, type=str, help='Video url: -u https://youtube.com/asdasdasd')
parser.add_argument('--output', required=True, default='pose', type=str, help='Output folder: -o videos')
parser.add_argument('--website', required=True, default='pose', type=str, help='Website of origin: -w <youtube>')
parser.add_argument('--playlist', action='store_true', help='If the specified url is a playlist')

def parse_args():
	args = parser.parse_args()
	return args.url, args.output, args.website, args.playlist
