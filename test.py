"""
用来测试模型效果的
@author: XP
"""


import cv2

# import numpy as np
imagepath = 'F:/WIDER_FACE/WIDER_val/WIDER_val/images/0_Parade_Parade_0_43.jpg'   #图片名称
image = cv2.imread(imagepath)

faces = [[152,509,21,23],            	#valid中对应的数据
[397,510,23,27],
[306,448,24,31],
[134,430,20,24],
[201,450,20,25],
[677,448,18,25],
[498,509,23,30],
[77,451,20,27],
[820,511,23,29],
[655,350,17,23],
[943,521,16,24],
[441,289,16,24],
[601,512,23,26],
[498,391,23,30],
[712,513,22,28],
[264,511,22,28],
[882,459,19,28],
[31,509,20,24],
[770,458,19,27],
[386,341,20,27],
[598,341,19,26],
[754,400,19,26],
[808,433,18,23],
[546,291,16,21],
[547,446,19,27],
[9,482,19,24],
[253,375,21,26],
[701,374,21,26],
[188,387,21,25],
[442,449,19,25],
[493,227,14,20],
[342,233,9,12],
[307,354,20,30],
[200,532,17,17],
[576,200,9,12],
[338,334,16,22],
[989,257,10,13],
[755,258,9,13],
[222,277,9,13],
[614,294,12,15],
[675,256,9,13],
[338,275,10,13],
[636,328,14,19],
[306,312,13,19],
[489,221,15,19],
[927,297,10,14],
[358,291,12,18],
[851,296,10,13],
[241,274,9,12],
[677,277,10,12],
[714,257,8,12],
[953,256,9,13],
[128,534,16,18],
[144,274,8,12],
[162,257,7,10],
[431,350,23,25],
[539,180,9,11],
[636,199,8,11],
[558,250,10,15],
[671,315,12,15],
[303,236,8,11],
[579,271,11,16],
[810,256,9,12],
[435,515,19,20],
[559,240,9,15],
[577,257,10,14],
[921,552,16,21],
[336,292,12,16],
[849,257,8,11],
[301,277,10,13],
[912,276,9,12],
[873,316,10,14],
[707,335,15,17],
[714,275,9,12],
[312,315,14,17],
[636,259,9,13],
[322,292,11,14],
[168,275,8,12],
[391,409,16,21],
[930,274,9,12],
[262,290,11,15],
[262,279,10,13],
[576,237,9,12],
[754,198,7,10],
[731,238,8,11],
[795,391,15,18],
[831,369,13,16],
[600,255,9,13],
[897,296,9,12],
[320,277,10,13],
[615,256,9,13],
[262,258,9,11],
[831,276,9,12],
[108,272,8,11],
[989,235,8,12],
[637,298,11,14],
[868,369,10,15],
[793,277,9,12],
[220,257,8,10],
[616,214,8,12],
[873,236,8,11],
[732,486,16,21],
[66,239,8,12],
[750,318,12,15],
[370,533,16,20],
[757,236,8,11],
[615,275,9,12],
[674,197,8,11],
[363,279,10,14],
[657,237,8,12],
[548,509,16,20],
[747,328,14,18],
[836,356,12,16],
[123,273,8,11],
[675,236,8,11],
[814,218,7,10],
[698,312,11,14],
[756,219,8,11],
[596,293,11,16],
[600,179,7,11],
[710,296,10,13],
[102,219,7,10],
[654,256,9,12],
[279,238,8,10],
[736,292,9,13],
[321,219,8,11],
[870,528,23,24],
[264,238,8,10],
[988,219,8,11],
[875,257,8,11],
[179,276,8,12],
[674,220,8,11],
[893,219,8,10],
[811,238,8,11],
[336,260,10,13],
[206,256,8,10],
[893,277,8,11],
[243,258,8,11],
[71,217,7,11],
[281,257,9,11],
[125,258,7,10],
[898,313,9,14],
[612,239,9,12],
[203,278,9,12],
[766,530,17,19],
[989,179,8,10],
[676,294,10,13],
[71,277,8,12],
[653,275,10,12],
[911,374,10,14],
[526,324,21,28],
[613,180,7,11],
[952,236,8,11],
[310,527,20,20],
[143,199,7,10],
[139,399,14,16],
[711,314,11,13],
[103,237,7,10],
[923,502,14,22],
[600,238,8,12],
[735,319,12,14],
[735,278,9,12],
[757,295,10,13],
[889,258,8,10],
[850,370,11,16],
[715,198,7,10],
[201,241,7,9],
[875,406,14,17],
[243,348,15,20],
[145,259,7,10],
[732,368,16,19],
[697,199,7,10],
[395,296,10,17],
[578,215,8,12],
[810,313,12,17],
[362,525,16,22],
[79,533,19,18],
[812,274,9,12],
[320,234,8,11],
[814,198,7,10],
[659,219,7,11],
[1011,180,6,10],
[952,182,8,9],
[777,237,8,12],
[953,220,7,10],
[989,333,10,14],
[6,159,7,10],
[637,236,8,11],
[854,220,8,11],
[597,198,7,11],
[518,328,16,27],
[360,213,8,13],
[595,217,8,12],
[698,237,8,11],
[225,239,7,9],
[874,278,8,11],
[790,239,8,12],
[324,259,9,12],
[693,276,9,12],
[187,238,7,10],
[556,179,7,10],
[25,258,8,11],
[931,260,8,11],
[104,430,13,17],
[891,370,10,14],
[618,200,8,11],
[906,314,10,14],
[657,198,7,11],
[302,292,11,14],
[282,280,10,13],
[894,199,7,9],
[952,197,7,10],
[814,329,13,17],
[654,297,11,13],
[44,137,7,10],
[637,316,12,14],
[696,217,8,11],
[240,240,8,10],
[795,199,7,10],
[699,334,14,18],
[969,257,8,12],
[909,297,9,12],
[755,273,9,12],
[892,357,10,14],
[838,257,8,12],
[561,214,8,12],
[246,338,14,17],
[733,256,8,12],
[181,199,7,9],
[303,219,8,10],
[639,272,9,12],
[282,289,12,15],
[852,235,8,10],
[5,527,11,19],
[736,217,7,10],
[892,235,8,10],
[850,313,9,13],
[873,295,8,11],
[657,179,7,10],
[930,179,7,9],
[792,217,7,10],
[120,463,18,22],
[872,199,7,10],
[203,200,7,9],
[954,157,8,10],
[796,254,8,12],
[854,199,7,10],
[698,257,8,12],
[144,218,7,9],
[932,331,9,14],
[125,240,7,10],
[597,522,17,19],
[253,451,17,21],
[913,355,9,13],
[4,258,7,11],
[144,238,7,9],
[772,310,11,15],
[126,217,6,9],
[491,291,15,25],
[715,239,8,11],
[990,316,9,12],
[715,217,8,11],
[853,279,8,11],
[731,356,15,16],
[971,200,8,10],
[578,178,8,11],
[775,218,7,10],
[239,537,15,16],
[47,255,7,11],
[715,179,7,9],
[125,201,7,9],
[83,219,7,10],
[775,276,9,12],
[893,180,7,9],
[833,199,7,9],
[1011,315,7,12],
[5,516,11,17],
[203,218,7,9],
[872,218,7,10],
[282,198,7,10],
[658,315,12,15],
[972,217,8,11],
[795,181,7,9],
[534,351,20,26],
[914,180,7,9],
[709,347,15,19],
[737,201,7,10],
[594,276,10,14],
[912,259,8,11],
[970,315,9,12],
[436,522,19,21],
[282,219,8,9],
[814,368,14,17],
[775,179,6,9],
[282,180,7,9],
[931,201,7,10],
[167,199,7,9],
[773,297,10,14],
[911,237,8,10],
[164,238,7,9],
[45,179,8,9],
[262,199,7,9],
[1010,199,7,10],
[238,296,11,13],
[930,216,8,10],
[374,274,10,16]]
print(faces[0])
for i in range(len(faces)):
    x = int(faces[i][0])
    y = int(faces[i][1])
    w = int(faces[i][2])
    h = int(faces[i][3])
    cv2.rectangle(image, (x, y), (x + w, y + w), (0, 255, 0), 2)
cv2.imshow('v3_1.jpg', image)

cv2.waitKey(0)