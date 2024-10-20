from pytubefix import YouTube, Playlist


def getoptions(yt, url):
    print("Select the following options")
    print("1. Get Thumbnail\n2. Download audio\n3. Download Video\n4. Download Playlist")
    n = int(input("Enter a number : "))
    if n not in [1,2,3,4]:
        getoptions()
        return
    if (n == 1):
        getThumbnail(yt)
    elif (n == 2):
        downloadAudio(yt)
    elif (n==3):
        downloadVideo(yt)
    elif (n==4):
        downloadPlaylist(url)


def getThumbnail(yt):
    print(yt.thumbnail_url)


def downloadAudio(yt):
    stream = yt.streams.filter(only_audio = True)[-1]
    stream.download()

def downloadVideo(yt):
    stream = yt.streams.filter(progressive = True,file_extension='mp4')[-1]
    stream.download()

def downloadPlaylist(url):
    p = Playlist(url)
    i = 1
    print(len(p))
    for video in p.videos[:3]:
        video.streams.filter(progressive=True).first().download()
        print(i, " Video is Downloaded")
        i+=1





def main():
    print("Welcome to the Downloader")
    url = input("Enter the YouTube link : ")
    try: 
        yt = YouTube(url)

    except:
        try:
            p = Playlist(url)
            print("Downloading Your Playlist...")
            downloadPlaylist(url)
            print("Playlist Downloaded, Thank You")
            return
        except:
            print("Try Again")
            return
    getoptions(yt, url)
    




while True:
    main()