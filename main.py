from pytube import YouTube, Playlist

def video_info(yt):
    print("Title : ", yt.title)
    print("Total Length :", yt.length, "s")
    print("Views : ", yt.views)

def download_video(yt):
    my_streams = yt.streams.filter(file_extension = "mp4", only_video = True)
    for streams in my_streams:
        print(f"Video itag : {streams.itag} Resolution : {streams.resolution}")
    input_itag = input("Enter the itag VAlue : ")
    print("Downloading...")
    video = yt.streams.get_by_itag(input_itag)
    video.download()
    print("Video is Downloading as",yt.title+".mp4")

def download_audio(yt):
    my_streams = yt.streams.filter(only_audio = True)
    for streams in my_streams:
        print(f"Audio itag : {streams.itag} Resolution : {streams.abr} ")
    input_itag = input("Enter the itag VAlue : ")
    print("Downloading...")
    video = yt.streams.get_by_itag(input_itag)
    video.download()
    print("Audio is Downloading as",yt.title+".mp3")

def download_playlist(p):
    print(p.title)
    for video in p.videos:
        try:
            video.streams.first().download(video.title)
        except Exception as e:
            print(e, type(e))
    print("Playlist is Downloaded")

def select():
    print("(1) Download Video")
    print("(2) Download Audio\n")
    print("(3) Download Playlist")


select()

choice = int(input("Enter Number: "))

if choice == 1:
    link = input("Enter Video Link --> ")
    yt = YouTube(link)
    download_video(yt)
elif choice == 2:
    link = input("Enter Video Link --> ")
    yt = YouTube(link)
    download_audio(yt)
elif choice == 3:
    link = input("Enter Video Link --> ")
    p = Playlist(link)
    download_playlist(p)
else:
    print("############ Invalid Number #############\n")
    select()

