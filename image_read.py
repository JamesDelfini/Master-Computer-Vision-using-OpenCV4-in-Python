## Python v3.7.3
## opencv-python v4.1.0.25
# pip install opencv-python
# https://docs.opencv.org/4.1.0/d1/dfb/intro.html

## Remain the comment configuration below for pylint source-code, bug and quality checker.
# pylint: disable=maybe-no-member

from core.general import showMsg
import cv2

###################################
## Description: Reading the Image
# cv2.imread(<filename>, <flag>)
# Flag 0 - Gray Scale(Reads the Image in Black & White)
# Flag 1 - Colored Format(Reads the Image in RGB/Colored Format)
###################################
pic = 'Images/Black Clover.png' # 1920x1200 Picture

# So, when we are working with OpenCV images, 
# we specify the y coordinate first, then the 
# x coordinate. And, the colors are stored as 
# BGR values – blue in layer 0, green in layer 1, 
# red in layer 2 – instead of RGB triples.

# Gray Scale
img = cv2.imread(pic, 0)
# showMsg(img)
# [[195 186 180 ... 129 133 136]
#  [196 141 149 ... 125 126 127]
#  [178 117 136 ... 146 140 132]
#  ...
#  [175 169 144 ...  66  82  92]
#  [161 169 162 ...  61  66  76]
#  [154 158 167 ...  68  68  68]]
# print(len(img[0])) # 1920 Width
# print(len(img)) # 1200 Height

# Colored Format
img = cv2.imread(pic, 1)
print(img[0][0][0]) # Third [0] Blue Layer, [1] Green Layer, [2] Red Layer 
print(len(img[0])) # 1920 Width
print(len(img)) # 1200 Height

showMsg(img)
# [[195 186 180 ... 129 133 136]
# [[195 186 180 ... 129 133 136]
# [[[ 35 205 209]
#   [ 32 194 199]
#   [ 39 188 193]
#   ...
#   [ 76 118 159]
#   [ 80 123 164]
#   [ 83 126 167]]

#  [[ 27 206 209]
#   [ 39 144 156]
#   [ 48 153 164]
#   ...
#   [ 74 113 156]
#   [ 73 115 156]
#   [ 73 116 157]]

#  [[ 36 186 192]
#   [ 55 116 133]
#   [ 54 137 152]
#   ...
#   [ 92 137 177]
#   [ 86 130 170]
#   [ 78 122 162]]

#  ...

#  [[121 170 200]
#   [115 163 194]
#   [ 94 136 169]
#   ...
#   [ 48  57  88]
#   [ 60  70 105]
#   [ 70  82 116]]

#  [[107 155 187]
#   [114 163 194]
#   [108 156 188]
#   ...
#   [ 43  51  80]
#   [ 48  57  88]
#   [ 55  65  97]]
# [[[ 35 205 209]
#   [ 32 194 199]
#   [ 39 188 193]
#   ...
#   [ 76 118 159]
#   [ 80 123 164]
#   [ 83 126 167]]

#  [[ 27 206 209]
#   [ 39 144 156]
#   [ 48 153 164]
#   ...
#   [ 74 113 156]
#   [ 73 115 156]
#   [ 73 116 157]]

#  [[ 36 186 192]
#   [ 55 116 133]
#   [ 54 137 152]
#   ...
#   [ 92 137 177]
#   [ 86 130 170]
#   [ 78 122 162]]

#  ...

#  [[121 170 200]
#   [115 163 194]
#   [ 94 136 169]
#   ...
#   [ 48  57  88]
#   [ 60  70 105]
#   [ 70  82 116]]

#  [[107 155 187]
#   [114 163 194]
#   [108 156 188]
#   ...
#   [ 43  51  80]
#   [ 48  57  88]
#   [ 55  65  97]]
# [[[ 35 205 209]
#   [ 32 194 199]
#   [ 39 188 193]
#   ...
#   [ 76 118 159]
#   [ 80 123 164]
#   [ 83 126 167]]

#  [[ 27 206 209]
#   [ 39 144 156]
#   [ 48 153 164]
#   ...
#   [ 74 113 156]
#   [ 73 115 156]
#   [ 73 116 157]]

#  [[ 36 186 192]
#   [ 55 116 133]
#   [ 54 137 152]
#   ...
#   [ 92 137 177]
#   [ 86 130 170]
#   [ 78 122 162]]

#  ...

#  [[121 170 200]
#   [115 163 194]
#   [ 94 136 169]
#   ...
#   [ 48  57  88]
#   [ 60  70 105]
#   [ 70  82 116]]

#  [[107 155 187]
#   [114 163 194]
#   [108 156 188]
#   ...
#   [ 43  51  80]
#   [ 48  57  88]
#   [ 55  65  97]]

#  [[ 99 147 180]
#   [103 152 184]
#   [111 161 192]
#   ...
# [[[ 35 205 209]  [ 32 194 199]
#   [ 39 188 193]
#   ...
#   [ 76 118 159]
#   [ 80 123 164]
#   [ 83 126 167]]

#  [[ 27 206 209]
#   [ 39 144 156]
#   [ 48 153 164]
#   ...
#   [ 74 113 156]
#   [ 73 115 156]
#   [ 73 116 157]]

#  [[ 36 186 192]
#   [ 55 116 133]
#   [ 54 137 152]
#   ...
#   [ 92 137 177]
#   [ 86 130 170]
#   [ 78 122 162]]

#  ...

#  [[121 170 200]
#   [115 163 194]
#   [ 94 136 169]
#   ...
#   [ 48  57  88]
#   [ 60  70 105]
#   [ 70  82 116]]

#  [[107 155 187]
#   [114 163 194]
#   [108 156 188]
#   ...
#   [ 43  51  80]
# [[[ 35 205 209]  [ 32 194 199]
#   [ 39 188 193]
#   ...
#   [ 76 118 159]
#   [ 80 123 164]
#   [ 83 126 167]]

#  [[ 27 206 209]
#   [ 39 144 156]
#   [ 48 153 164]
#   ...
#   [ 74 113 156]
#   [ 73 115 156]
#   [ 73 116 157]]

#  [[ 36 186 192]
#   [ 55 116 133]
#   [ 54 137 152]
#   ...
#   [ 92 137 177]
#   [ 86 130 170]
#   [ 78 122 162]]

#  ...

#  [[121 170 200]
#   [115 163 194]
#   [ 94 136 169]
#   ...
#   [ 48  57  88]
#   [ 60  70 105]
#   [ 70  82 116]]

#  [[107 155 187]
#   [114 163 194]
#   [108 156 188]
#   ...
#   [ 43  51  80]
#   [ 48  57  88]
#   [ 55  65  97]]
# [[[ 35 205 209]  [ 32 194 199]
#   [ 39 188 193]
#   ...
#   [ 76 118 159]
#   [ 80 123 164]
#   [ 83 126 167]]

#  [[ 27 206 209]
#   [ 39 144 156]
#   [ 48 153 164]
#   ...
#   [ 74 113 156]
#   [ 73 115 156]
#   [ 73 116 157]]

#  [[ 36 186 192]
#   [ 55 116 133]
#   [ 54 137 152]
#   ...
#   [ 92 137 177]
#   [ 86 130 170]
#   [ 78 122 162]]

#  ...

#  [[121 170 200]
#   [115 163 194]
#   [ 94 136 169]
#   ...
#   [ 48  57  88]
#   [ 60  70 105]
#   [ 70  82 116]]

#  [[107 155 187]
#   [114 163 194]
#   [108 156 188]
#   ...
#   [ 43  51  80]
#   [ 48  57  88]
#   [ 55  65  97]]


#  [[ 99 147 180]

#  [[ 99 147 180]
# [[[ 35 205 209]
#   [ 32 194 199]
#   [ 39 188 193]
#   ...
#   [ 76 118 159]
#   [ 80 123 164]
#   [ 83 126 167]]

#  [[ 27 206 209]
#   [ 39 144 156]
#   [ 48 153 164]
#   ...
#   [ 74 113 156]
#   [ 73 115 156]
#   [ 73 116 157]]

#  [[ 36 186 192]
#   [ 55 116 133]
#   [ 54 137 152]
#   ...
#   [ 92 137 177]
#   [ 86 130 170]
#   [ 78 122 162]]

#  ...

#  [[121 170 200]
#   [115 163 194]
#   [ 94 136 169]
#   ...
#   [ 48  57  88]
#   [ 60  70 105]
#   [ 70  82 116]]

#  [[107 155 187]
#   [114 163 194]
#   [108 156 188]
#   ...
#   [ 43  51  80]
#   [ 48  57  88]
#   [ 55  65  97]]

#  [[ 99 147 180]

#  [[ 99 147 180]

#  [[ 99 147 180]

#  [[ 99 147 180]
#   [103 152 184]
#   [111 161 192]

#  [[ 99 147 180]
#   [103 152 184]
#   [111 161 192]

#  [[ 99 147 180]

#  [[ 99 147 180]

#  [[ 99 147 180]

#  [[ 99 147 180]
#   [103 152 184]
#   [111 161 192]

#  [[ 99 147 180]
# [[[ 35 205 209]
#   [ 32 194 199]
#   [ 39 188 193]
#   ...
#   [ 76 118 159]
#   [ 80 123 164]
#   [ 83 126 167]]

#  [[ 27 206 209]
#   [ 39 144 156]
#   [ 48 153 164]
#   ...
#   [ 74 113 156]
#   [ 73 115 156]
#   [ 73 116 157]]

#  [[ 36 186 192]
#   [ 55 116 133]
#   [ 54 137 152]
#   ...
#   [ 92 137 177]
#   [ 86 130 170]
#   [ 78 122 162]]

#  ...

#  [[121 170 200]
#   [115 163 194]
#   [ 94 136 169]
#   ...
#   [ 48  57  88]
#   [ 60  70 105]
#   [ 70  82 116]]

#  [[107 155 187]
#   [114 163 194]
#   [108 156 188]
#   ...
#   [ 43  51  80]
#   [ 48  57  88]
#   [ 55  65  97]]

#  [[ 99 147 180]
#   [103 152 184]
#   [111 161 192]
#   ...
#   [ 48  58  88]
#   [ 49  59  89]
#   [ 49  59  89]]]