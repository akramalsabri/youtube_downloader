from pytube import YouTube

#link = 'If you want a specific link only'
link = input("Enter your video URL: ") #to add the link in the run time 

video = YouTube(link)


# information about the channal and the video

print(f"The video title is:\n{video.title} \n--------------------------------------------")
print(f"The video description is:\n{video.description} \n--------------------------------------------")
print(f"The video rating is:\n{video.rating} \n--------------------------------------------")
print(f"The video views is:\n{video.views} \n--------------------------------------------")
print(f"The video duration is:\n{video.length/60} minutes \n--------------------------------------------")


# print(video.streams)

for stream in video.streams:
    print(stream)

# for stream in video.streams.filter(progressive="True"):
#     print(stream)

def finish():
    print("The video has been downloaded successful")

video.streams.get_lowest_resolution().download(output_path="#path to download the video inside")
video.register_on_complete_callback(finish())


# for list download 

# from pytube import Playlist

# playlist_link = 'https://www.youtube.com/watch?v=mv4RfqtKBPs&list=PLJ_rR_mTxaD_UtnOdrZaznEgLOmt-bjbg'
# playlist_link = Playlist(link)

# for video in playlist_link.videos:
#     video.streams.get_lowest_resolution().download(output_path="D:\myWork\youtube downloader\list")
#     video.register_on_complete_callback(finish())