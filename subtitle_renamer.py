import argparse
from os import listdir, path
import os
from pprint import pprint
import re
from typing import List


subtitle_language_code = "chi"
#subtitle_language_code is defined by the ISO-639-1 (2-letter) or ISO-639-2/B (3-letter) standard.
#ISO-639-1 (2-letter):http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
#ISO-639-2/B (3-letter):https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes

file_path = None

supprt_subtitle_format = ["srt", "ass"]

def subtile_renamer():
    files = []
    for f in listdir(file_path):
        if path.isfile(path.join(file_path, f)) and path.splitext(f)[1] != "":
            files.append(f)


    #identify subtitile files and video files
    subtitle_file_list: List[dict] = []
    video_file_list: List[dict] = []

    for file in files:
        file_extention = path.splitext(file)[1]
        file_name = path.splitext(file)[0]
        t_file_extention = re.findall(r".([a-zA-z]*)", file_extention)[0]
        episode = re.findall(r"(?i)S[0-9][0-9]E[0-9][0-9]", file)

        if t_file_extention in supprt_subtitle_format:
            subtitle_file_list.append(
                {"episode": episode[0], "file_name": file_name, "file_extention": file_extention, "new_name": ""})
        else:
            video_file_list.append(
                {"episode": episode[0], "file_name": file_name, "file_extention": file_extention})

    print(f"number of subtitle files:{len(subtitle_file_list)}")
    print(f"number of video files:{len(video_file_list)}")
    video_file_count = video_file_list.__len__()

    match_count = 0

    #rename subtitle files
    for subtitle_file in subtitle_file_list:
        for video_file in video_file_list:
            if subtitle_file['episode'] == video_file['episode'] :
                match_count += 1
                subtitle_file['new_name'] = video_file['file_name']
                video_file_list.remove(video_file)
                break

    if match_count == video_file_count:
        print(f"find ALL!")
    else:
        print(
            f"find {match_count} subtitle file(s),{video_file_list.__len__()} not found:")
        for video_file in video_file_list:
            print(video_file["file_name"]+video_file["file_extention"])

    # test before rename
    # pprint(subtitle_file_list)

    for subtitle_file in subtitle_file_list:
        os.rename(path.join(file_path, subtitle_file["file_name"]+subtitle_file["file_extention"]), path.join(
            file_path, subtitle_file["new_name"]+"."+subtitle_language_code+subtitle_file["file_extention"]))



if __name__ == "__main__":
    paser=argparse.ArgumentParser("subtitle renamer by wheheo")
    paser.add_argument('-filePath','-fP',required=True,help="file path to subtitle files and video files(they should locate at the same path)")
    paser.add_argument('-language','-L',default='chi',help="subtitle language (default is chi for chinese) is defined by the ISO-639-1 (2-letter) or ISO-639-2/B (3-letter) standard")
    
    args=paser.parse_args()
    

    file_path=args.filePath
    subtitle_language_code=args.language
    subtile_renamer()
    
    
    