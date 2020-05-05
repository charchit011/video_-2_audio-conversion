#python code to convert video file to audio
import moviepy.editor as mp
#selection of video file
clip = mp.VideoFileClip(r"video file path")
#select audio extract path
#must add file name+.mp3 
clip.audio.write_audiofile(r"audio file path\audio file name.mp3")
