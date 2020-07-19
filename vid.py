import os
dir = os.listdir("videos")
for x in dir:
	orgfile = "videos/" + x
	converted = "videos_changed/" + x
	cmd = "ffmpeg -y -stream_loop -1 -i \"om.mp3\" -i \"%s\" -map 0:a:0 -map 1:v:0 -c:v copy -c:a aac -ac 2 -shortest \"%s" % (orgfile,converted)
	os.system(cmd)

# merge: ffmpeg -safe 0 -f concat -i list.txt -c copy output.mp4
# compress: ffmpeg -i $infile -vf "scale=iw/2:ih/2" $outfile
# cut video:  ffmpeg -ss 00:01:00 -i input.mp4 -to 00:02:00 -c copy output.mp4