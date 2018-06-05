"""
modle_out_convert 是将modle_out_clean的输出转化成wider_face数据格式，方便进行 IOU计算
@author: XP
"""
def num_arr(filename):
    fo = open(filename, "r")  # 读入标注结果集
    key = next(fo, -1)
    key = key.split(" ")
    num_array = []
    num = 1
    while True:

        if key[0] == -1:
            break;
        next_line = next(fo, -1)
        if next_line != -1:
            next_line = next_line.split(" ")
        else:
            next_line = [-1]
        if next_line[0] == key[0]:
            num = num + 1
            key = next_line
        else:
            key = next_line
            num_array.append(num)
            num = 1
    fo.close()
    return num_array

def data_convert(filename, list, num_array):
    fo = open(filename, "r")  # 读入标注结果集

    sum = 0
    # print(num_array)
    sum_arr = 0
    # for i in range(len(num_array)):
    #     sum_arr = sum_arr + num_array[i]
    # print(sum_arr)
    for i in range(len(num_array)):
        key = next(fo, -1)
        if key == -1:
            print(i)
            break
        key = key.split(" ")
        list.write(key[0] + ".jpg"+"\n")
        list.write(str(num_array[i]) + "\n")
        sum = sum + 1
        for j in range(num_array[i]):
            list.write("{0} {1} {2} {3}\n".format(int(float(key[2])),int(float(key[3])),int(float(key[4]) - float(key[2])),int(float(key[5]) - float(key[3]))))
            if j == num_array[i] - 1:
                continue
            key = next(fo, -1)
            key = key.split(" ")
            sum  = sum + 1
    print(sum)
    fo.close()


filename = "modle_out_clean.txt"
list = open('label.txt', 'w')
num_array = num_arr(filename)
data_convert(filename, list, num_array)