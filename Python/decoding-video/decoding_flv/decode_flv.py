#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:          Decoding FLV files via FFVideo
# Purpose:
#
# Author(s):      
# PyPi Official: https://pypi.python.org/pypi/FFVideo
# Edited:        Goel (2016)
# Copyright:     (c) (no need for copyright under MIT license ...)
# Licence:       MIT <Place MIT licence here>
#-------------------------------------------------------------------------------

################################################################################
#def main():
#    pass
################################################################################

# Annotated ffvideo.pyx is avaiable at:
# https://bitbucket.org/zakhar/ffvideo/src/8ab403fc7286b66020814e8e498b0d9f605c3c5c/ffvideo/ffvideo.pyx?at=default&fileviewer=file-view-default

# avcodec_decode_video2 attributes at:
# https://ffmpeg.org/doxygen/2.7/group__lavc__decoding.html#ga99ee61b6dcffb7817a275d39da58cc74

################################################################################
# Some notes:
# Flow of data: VideoStream decodes frame ---> returns VideoFrame function variables
#               which contains other procedures e.g. image/ndarray to convert data further.
# Hence all the frames are decoded individually though returned as VideoFrame function variables.
# Possibility of editing the ffvideo.pyx to return decoded data individually straight away.
################################################################################

import ffvideo

# Possible ideas:
# • Manipulate decode next frame function to allow modify the encoded data which is decoded and returned as
# a VideoFrame attribute.
# • Create blank flv and 'pump' data into it whilst decoding next frame?

# The FLV file we are using resides in the /flvs folder.
file_name = 'flvs/american_football.flv'
video_stream = ffvideo.VideoStream(file_name)

for frame in video_stream:
    # Note: VideoStream frames all return VideoFrame frames where all the data has 
    #       been decoded in VideoStream.
    
    # Need to access VideoStream decoding functions and manipulate it to allow
    # for decoding of a single frame of data.
    
    # Accessible variables returned (from VideoFrame via VideoStream).
    # print frame.data # Prints RGB output. Please use with some caution; may cause interpreter crash. 
    
    # Prints out the basic information from the VideoFrame that was generated, the data inside is
    # decoded and is in RGB format ready to be converted to an image using the PIL library.
    print "Frame dimensions (w/h/s): ", frame.width, frame.height, frame.size
    print "Frame mode:", frame.mode
    print "Frame timestamp:", frame.timestamp
    print "Frame number:", frame.frameno


# Specific frame searches; state seconds elapsed (integer)/frame number/PTS at it will fetch the frame in that position.
# specific_frame = video_stream.get_frame_at_sec(8)
# specific_frame_2 = video_stream.get_frame_at_pts()
# specific_frame_3 = video_stream.get_frame_no()

# custom_data = '\x00\x00\x85R\xa4\x03\xe3\x14\xb5\x19Hr"\x01\x17\xda\x89_V\xad\x8bIb\x87\xc5\xc2Mf\xc77H\x07\xbc\x82\x15l\xd3\x82\xaf\x7f\xd3-\xe22\xa7\xb5\x97\x17u#/W\xb4x#\x9et\x8d\x03\xd5\xd513\x93\xb8\xc7\xc8N\x95H\xe52\xe0;\xd3\x08\xd2\xdf6i\xed\xf1.\x18\xb3\x05\xef\xf2\x8f\xda\xd9\x01\xa5\xf3\xbf\x1e\x1e\n{\xdb\x1a $\xd0\xbbEdh_L\x9d\xb1\x9e\xa1\xf4\xc9\xf616\xb6\xf1{\xc4\xd9\xf7\xf0\x1e\xec\x08@zs\xc5\xc5\xc9\x01\xa1\xfem\x06\x06\x12)\x1f\xab\xa9 \x8e\xf6\x08]\xf5x:\xe2\xefY\xaa\x87\xc5\xc28\xef\xe3Wc\xf1a\xedj\x84\xb5\x7f\xa0hy\x18_\x17{\x0f\xd4X\xa7\xfd\x82\xf6!\x1d^`\x04*\xd5@|\x14Q\xaf\x1bu\x8c\x0fV\x12>:La,~\xa6m\x8da\xa5\x19\xe0;\x92\x01\xc7\x1e\xe2\x98y\xe2$)\xe0\x80\\$\xab/\x96O\xe4\x84\x80\x80\x10\x81\x0c\x0f\xc0:\x93{(\xbc}\xe1*\x17)u\x08\x1cVJ|\xe0\x12\x8f\x84\xa2\xfa\xaf\xdd\x8a+.2D\xf1\xa4\x92\xf0\x83\xe2\xe1\xd7U\xab\x03\x10\xa6\xb4\xe7\xc8\xbd$ON2\t\x10\xa2\xf4\x06\x19\xfa\x8b9\x16\xb5/\xfe6rz\xe4\x8f\xb9\x00\xc4G\xd1\x8f\xf8\x98\x1aH&0\xe1\xca}X\x17\xa9\x1az-\xe8O\x8a\x91m\x90Qa5\x8cO\xfc\r\x96\x80\xf9z\xbe\x06I^\x1f(\xf2\xff\xad\xbd\rW\xa0dp\xf8~\x14\xf38\x1e\xc6\xfd\x0f\x17\xe9\xb6s\x00\x16\x97:\xe7\x87\x06\xc7\x93K\xf275\xc5\xe8*\xce\xff\xc1%\xf0\x90\xf4\x8e\x18\xb3OH|\xea,\xeb\xde\xceo\x8dRd\xf1A\xf9Z\xba\xd59\xdb\xf8\x8f\xa9\xea\xe3D<\xf3\xd0\xb7\x80\x95\xf2p\xf8#\xfe\x03\x84p\xc8\xf5\xc9\x08N\x85?\xfe\x85\xbd\xe9\xef:t2B\xe1\xff\xc7\xa4\xeb\x95\x19\x06\x83\xf5/l\xe2\xc4\xa1\xd4\xcddN\x01\x0c\xf5\x9d]\x02TC\x1a\x0c\x87\xf9\x95\xf6\x040\x18v\xce\xfc\xe5Me\x1c\x8bP\xf3:r\xce-\x1a\xb7\xbf\xf0\x98\xa8} \xfb!r\xb3\xeaN\x8b~K\xd8\xfb\xf0\xcc\xf2|?\r\x1dz]\xe0\xd0\xbf\x00B^\xd0\xce?\xe1\x98\x9f\xa1\x90\x96\r\x10\x1b\xd4\xfb\xb6I\xda3\xe1#\x1e\xdc\x96\xdb\x926\xf6\xb7\xa4\xdf\xad\x15%`f\xe1\x0f\xbb\xb0\x18X"\x98\x15\xa8\xe1[\xbfW\x88\x07\t\x9ey_\xa54\xb5\xc2\x19[\x98\xdfc}\xbd\xfc\x07\xbf\x89\x1f\xc3+\n\xbe~eP\x92\x01\x0e\xe3\xe0\x0f\x00\xa8\xe7=\xa7\xd0\xcf\xc7\xff\xff\xf9\xfe<\x93s\xde\x04\xa5\x00\xc9)\x90K\x12\xc1\tP\xe8\xdc\xb8\xfc~$\x88\xf7\xf7\x038\xd7\xe3\xe1\x91)\x16\x08\x03\x80<\xbcJ/\xf2\xa5\x7fR\xab\xe1\x8a\x0cs\xe8\xc7\x86w\xc0\xd0\xff0\xf94\xf8\xdf\xf8\xf9\xbf\xfc\n\x95\x00@\xf0F\xfd\x0bI\x12~W9@\x99k\x94]T\x81\xe0xF\xb0<\xa7\x15\xc3\xf6)\x06\xcd\x96V\x9e\xbe9\xe6\xb2~\xaaj\xca\xdch\xac\xfa|\xc2\xc1\x19\xf9G\x15a^YR\xf7\x81F\xb1A\x1c\xa1g\xa7\xda\xb8\x883`\x05Y\xfaZ\xc8\xe0\x82\xe2\xcdT(\xc5\xa2>\xf1\x00\xe3\x05\xe7\xd3\xb0x\xfd?\xfd_\x8e\x06\x85\xf8E\xc7\xc0\x85\xe2P`!\xc7\xca\xa52\xe7\x87\xb6\x8f\x84\xb0\tiW\xf3\xd1\xe0\x1c\r\x03\xdb\xe8\x97\xfd\x0c\xa4\x1e\xc0\x9cP\xfcI\xeeJA(\xae/\xe5\x0e\xa2U\xe0C/\xcdh\xec\x7f\xc2\x18\x95\xea\xa3(g\x1b\x02\xf0\'Ew\xdc\xa0\xa4i#\xd4\x04\xa5z%\x17\x01GP\x08\xf4\n\x969\x91P\x92\xab\xca\xa4\xd6\x9d\x1d\xfe\xe1\x1e\x01\xc2H\x93D\x80<\x06\x80\xdfG\xad(G]=\xf8_7\xd6\x7fY\xf0\x9c\x18\x00\xd2\xf5P~%\x8f\xad\x1d\xfb\xfa<L^\xa8\xc8\xf8\x0f\x17Q\x12)\x032e\xa8\xcd\x91\x08{S\xca %\x89\x1f\x12/\xbe\n!\xf9z\xa4\xd6\x81\xf9\xac\xc0Q\xef\xe00\x80t2\x12\x81\x0e\x8f\xa0(\xcb\xaf\x19.\xf2\xb1\xfc\xa8\x95z\xabB\xe3\x88\xb9\xd9SV\x1a@\xf0\x80\x0c\x07\xb0\xfb\x80\xc0\xfet\x180q&\x15\x80P\x94\xa8 \x89\x05\xe0h~>\xa0\xc2>\xcd@m.WQ=\xacN\x96\x9a\x87\xdb\xea\xae@/w\x89x\x80\xf0\xcf\xcd\x96\xb1[?\xfce\x12E\x86\xb8\xbac\x9f\x94\xb7\x94\x059=\x86\xa7(\x80\x11\xfc\xa7\x9447\xc6(\xa7-j\xa1\x1c\x85\x89\xfa\xc8,A\\\x7f\xed\xe2H,\x10\x06\x88\xf7\xbd\xebd\xd62\x1e\x11\xaa\x1f\x8f\x1d[OYW\xdb\xc8\xbf!~pf\x1aWz\x80E\x08!\xd7\xd8VI\xbe\x06*\xa2Z\xfa\xaa\xd9\'\xd6um\xd3\xaah\x04\x85=R\xb0`aA\x83\x84\x1f\x97|]\xc9\xa9\r*\x12\xc1\x81\x88/\x02\xa0\xd0\x02\x05\xba`\x99\x1e\xb7\xd9\x1e4G\xbcW\xb1\x9f`4\x8f\xd5T\x1eM\xffF\x02/\xf5\x0c\xdaqU\xf2\xaf\xc05\x11\xc8\xf5"7\xc4\xc6R\xe2P!O\x01\xab\xf8\x05\x87\xb5B\x0b\xa3\x00\x84\x0c\x0b\xbf\x81\x82\x84/\xf3\x00\xc1\x02|\x18g\xe2\xa7r\xbcg\x97E`f_T\x9a[\x0esA\\D\xb8\xd8\xef\x0f9\x16eg\xfd\xa6;Z\x85$\t;\xfc\x17kI:\x11\xae\x05:6\n\x1b\xef\xd6 B\xde\xf67\xfc^\xf5p\xcc\x02\xc3;\x1a\xda\xfa\xc9\'\xc5w8M\x97\x8f\x83\'\x88\xf5@\x1e\xd8B\x12\x97V|f\x10=AB\x10K\xc4\xbe\xe2\xae\x00Sk\x8dO\x88\xf9\xf6\xfc\x17\x8c\x14\xb6\xdb\xa2:4<#\xe7\xc0\xd5Nb\xf2B]\x0f\x05h\x1exg\xcf\x88\xd8\xcf\xc6\x01\x7f\xbc\x07~\xa5\x81\x10\x8a\xd4\xc3C!O`-\x0cz\xc3\x03\x1c\x05,oC\x03\xe6\x84\x7fq\xbe\x85\x9d\xad\xb0\xe0\xc9R\x96\xbc\xb9\xa4\x83D\xf3\xf72u\x9e\x8b\x19B{BF\xfchh\xde\xf4<U\xa4\x0b\xe1\x8e\x98\xf1\x17\xdb\x18\xf3\xcf\xbd\xe97\x86z\x01\x08\xf5q\xd9f\xea\x94\xe7:\xbf\n\xc6\xc3\x05:\x01\x1f\xc7\x87\xd7\xc3\xb3\x85\xff\x06\x02 H\xe0\x1b\xff!K\xe7\xe2\x81\xf4\x1e\x80^(\xfc\xbf\xe3\xf5u_\xd1MigH\xbc\x87\xe6v.\xech\xdbc\\\xc8\xa4\x1a7\xec\x99\xa2\x99\'\x04\xf8\xb7\\\xd2\xe8 \xa10\xee\x04M\x13\x8c\xf4\xcd\x80\xf1\xef\x01\xa0\x04LoX\xe7\x80s\x84}\xe2\xa1\xd68\x9dr\x12\xca\x11\x1dO\xd6\xda8\xa0u\xd4$\xa3A\x9az\xe3\tf\xa5lS\xa6\x820\xaf\x8f*\x9cM>Y\xca\xeev\xa3D\xd7\x06D\x87\xd7\xde,\x117\xf4\xf5\'xP\xf4\xed\x9f%{\x92a\xdb\xf7\xa6\xb1\xf6q\xa6\x1akr\xb8\x7f\xd1q\xa4\xf1U;u)\x05\xe9(\xcf\xbd\x13\xad{\x1b\\\x8fd\xe8\x1ad\xc8\xc9\xc9\xfe\xc9#t\xc3\tF\x03S\x89\xf8=\x11\x1aNk\xc3\xf0`=T\xa8\xc1\xf2\xa5\xd5\xea\x9f\xa2.\x85o\x06\x01\xc8\x03\x15x\x0e\x841\xf800\x82@\x8d\xe0`\xdf\x01\x82\x04\x16\x89j\x81\x08\xbb\xca\xd5\xdb~\x10D\x9e\x8f\xfe\xd4\xf4\x03\x01\x92xB\x1e_\xab\x03\xe3\xf5uX\x18\x98r\xc8\xbe\x01~\xbb3y\xc8\x03\xf4\tl\x18\x88\xfd\x95g\xa6\xe8\xd7\x94\x1a(!\x93\x93\xd0\xc6\xc2\xaaCQ\xb2\xb7\xc5\x9f\x98\xbb,\t\x93\xdaN\x03\xc6\x85\xa6\xe2\xc0\xd0\xc1\'\xfen\xb2m\xe4\xf9\xa7\x91\xf6b\xc5\xa2\x94\xe7\x02\xc4\xf7\x820\xa4\xfe\x16\x8c\x02\x9e\x02\x92\x13\xaaW(\xf2\xa1!\x9e\xbb\x80_\x1eD\xe1\x8f\xc1[\xf0\xf9\xd5\xb3\t\xfc\xba\x89\xa7\x14\x15hb\xd8\x86\xd8\xa9s\xcb\xe5\x8f{Y\xc5\xb7\xea\xe6\xf4\xd8\xcf\xe1\x11a\xab\x8d4\x85\xca\x12\xc6cnpS\xfe:\x03&\t0\x8e\xf1\xeer<\x10G\xe5\xf2\tC\xe1*\x03\x07\xf8\xac\x0b\xab\x06\x9c\x08\x7fj\x95Z\n\x9bF\xafW.\xf9}\x03\xf0\xb8t\xd7w\x87\x84\x88\xa8\x14e\xfb\x82?\x94$\x00\x84\xf9\x90\x0bf\x93\xf1\xa6\x8d\xa7\xeb\xaa7\x08\xf4 99\xde\xb7\xd3?\\\xeb\x93\xe0\xd5\x01\x96\x93\xbf\xa4I\xff\x8d\xc2\x03\x1f\x93k\x80\xce9<egm\xab\r7\x8f\x03\x11\xa3b<\x8bI\xb7\x187(\xdc\xf3\xc6|]\xe3\xe1*\x8e\xa8\x16WU \x158!\t\x00lKJ\xe2es\xa3D\xf7\xb3C\x81[\xf0\x9cG\xbc/\x05a\x87\xbcB\xde`\xfb\xedo_6\xfa\x1fM\xd1b{D\x8dh\x8e\xeb\x08*7\'\xfd\x18\xd3\xf0\x86\xc6z\xeb\xa4aK\x89s\xc0\xa2\xfd\x11\th\x04\x17\x8f\xf5Ar\xa8\xb0\xc5\xee\x12\xea\x8b\xe74\x0c\x1d\x96l\xb0\x90\xfa{T\x1a\x87\xea\xb8\xb3\xca\xae\x86TpL\x9e\x85\x86\x04\xcd/\xf6\x96\x15\xe0\xb8f\x9fP\x9a\xc2!\x9d\xf5E\xc1\x10\xda\x7f\xf7\x14\xeb\x13A"z`e\x04B\x08\xd4<\x9e\x01\x07\xfd,%*\x19\xa7\x9c\xe8\xc8\x86\n\x06xd%\x17\x03\x03\xf8\xad \x05\x06@\x18\x10\x07tK\xf8\x19V\x0c,\x1b\x89\xa9w\x82E0&\xcf\xbcM\xbd\xe8{\xde\x85\x90\x12\x88{\xf0\x13^\xfaza\xa3#[O\xf2\x9d\n}\\\xd5!\xb1\x11\xaa\x8cd\xf7\x05=\t\x8b\xc4\xf4\xe0\xd6\xf3\x8d\xbd\xee\x13\xe5\xf1P(\x87\xa9\xd4H1\x1f\x83\x04\r\x80\\\x05=\x8d\xe9\xe3\xe2\xe8\xdc\xe7\x0b\xc6\'\x87\xcd+\xa9\xc5\xc4\xe9\xe31\x98\x8e\xb1\xf4g\x93\xe2\xc4j\rKY`\x8bB\xa1\x1f:J\xaa\xfe\xb7\x9d%U\xd3*\xa7l\x05P\xbd\xe8\xfeY<\xa4e\xf0h\x1e\xdc\x9f)\xe9\xab2M\xea\xc0\xbdPd\x07\xcd\x17L\xe34\xdb\x08\x06\x7f4\xb8\x86n6}\xccJ\xf8\xef\xc1\x9c\x97\x8d\xbb\x86q/\xa6F\xe2\xe7\xb1\xbd\x9d\xef\x17\xbcQ\xbd\xe2\x8c\xf3\xd5\xf4\xd9:zA\xa7+d\x94t\x06O\xef\x80X\x8f\xc6:\xec\xa4q\xa2f\xb5\x93o\x11\xe3<`\xdd\xe1/S\x0c\xde\x97\x1f\xc0`a\x15\xc4\xf1\xef\x1f\xaa\xa0o\xcb\x80Tg\x97\x17\xb7\xe5d\xde\xdb\xc3j\x95\xcd\xf3\xcb\xb0\xc9\xe4\xfe4\r\x1c\x17\xb5\xa2!\xf0\xb4H\xdcD\xf0\xf9\x96\x04hZ\xea\x10h!!\xa4\\\x9d\xf4\x10\x8eK9\x07\xcd_\xff\xf9\xd6\x1at8\x06L\x1f\xc0\xab\xfc\x18\x08sN\x01\tP\x1d\x0c\xa5\x9c\x93\xc7\xd5X4/\xc2P\xf42T\xa2\x1eU\xe0B.aM\x06\x89\xf8:\xa3\xc7\xcfG\xd3q\xa0\x11*\xe8\x1f\'\x15i\xd7\xe2\xe6\xcfEM\x84PX\xcb\xa4\xddD=P\xfb\xa5\xde"\x00\xc0\x0eV=\x9f\x94\xc1\x01\xe5rQ[\x19\xf5\xb3\xf5q\n\x0c\xde\xdetU\x9cx'

# Generate Image with PIL library in VideoFrame from this single frame data.
# specific_frame.image().save('specific_frame.jpg')

# individual_frame = video_stream.decode_one(custom_data)

# individual_frame.image().save('individual_frame.jpg')



# numpy.ndarray, required installed numpy
# print frame.ndarray().shape
################################################################################
#if __name__ == '__main__':
#    main()
################################################################################