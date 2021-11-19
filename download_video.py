from video_downloader import VideoDownloader
import in_out as io

def on_complete(stream, file_handler):
    print(f'Download complete! {file_handler}')

def print_progress(stream, chunk, bytes_remaining):
    print(f'Downloaded: {int((stream.filesize - bytes_remaining) / stream.filesize * 100)}%', end='\r')

if __name__ == '__main__':
    video_url, output_path, website, is_playlist = io.parse_args()

    video_downloader = VideoDownloader(on_complete_callback=on_complete, on_progress_callback=print_progress)
    
    if is_playlist:
        video_downloader.download_playlist(video_url, output_path)
    else:
        video_downloader.download_video(video_url, website, output_path)
