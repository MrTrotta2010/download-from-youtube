from pytube import YouTube, Playlist

class VideoDownloader:
    def __init__(self, on_progress_callback=None, on_complete_callback=None):
        self.on_progress_callback = on_progress_callback
        self.on_complete_callback = on_complete_callback

    def download_video(self, url, website, output_folder):
        if website == 'youtube':
            self.download_from_youtube(url, output_folder)
        else:
            print (f'[ERROR] Website {website} not supported')

    def download_playlist(self, url, output_folder):
        playlist = Playlist(url)
        try:
            for video in playlist.videos:
                if self.on_progress_callback:
                    video.register_on_progress_callback(self.on_progress_callback)
                if self.on_complete_callback:
                    video.register_on_complete_callback(self.on_complete_callback)
                
                video.streams.filter(only_video=True, file_extension='mp4')[0].download(output_path=output_folder, filename='_'.join(video.author, video.title))

        except Exception as e:
            print(f'[ERROR] {e}')

    def download_from_youtube(self, url, output_folder):
        print(f'> Downloading {url}')
        try:
            yt = YouTube(url)

            if self.on_progress_callback:
                yt.register_on_progress_callback(self.on_progress_callback)
            if self.on_complete_callback:
                yt.register_on_complete_callback(self.on_complete_callback)

            yt.streams.filter(only_video=True, file_extension='mp4')[0].download(output_folder)

        except Exception as e:
            print(f'[ERROR] {e}')
