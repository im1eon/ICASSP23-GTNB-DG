import os

video_dir = '/cfs/user/zhuanghaolin/mine/icassp22/a_a_page/video_r_20'
dance_names = sorted(os.listdir(video_dir))
audio_dir = '/cfs/user/zhuanghaolin/data/aistpp/wav'
music_names = sorted(os.listdir(audio_dir))
out_dir = '/cfs/user/zhuanghaolin/mine/icassp22/a_a_page/video_r_20_m'
print(music_names)

for dance in dance_names:
    #pdb.set_trace()
    name = dance.split(".")[0]
    print(name)

    if 'cAll' in name:
        music_name = name[-13:-9] + '.wav'
        print(music_name)
    else:
        music_name = name + '.mp3'
        audio_dir = 'extra/'
        music_names = sorted(os.listdir(audio_dir))
    #exit()
    
    if music_name in music_names:
        audio_dir_ = os.path.join(audio_dir, music_name)
        name_w_audio = name + "_audio"
        print(audio_dir_, name_w_audio)
        #exit()
        cmd_audio = f"ffmpeg -i {video_dir}/{name}.mp4 -i {audio_dir_} -map 0:v -map 1:a -c:v copy -shortest -y {out_dir}/{name_w_audio}.mp4 -loglevel quiet"
        os.system(cmd_audio)
        print("hi")