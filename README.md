# WIDER_FACE_data_conversion_for_YOLOv3
- 我个人喜欢写东西的时候把中间结果存成文件。。。
- -这样的话我可以把工作分成一段一段的。。。不容易弄混。。。如果不习惯的话可以把它改成一个文件。

---
- data_conversion.py 是将 wider_faced的标注数据集转成yolov3所需要的labels
- 每个图片转成对应名称的label
- 由于yolov3需要的是归一化之后的中心坐标和w，h所以在convert方法中进行了归一化和数据转换
- train_list.py将标注文件转成yolov3所需要的train_list,valid_list也是用这个
- modle_out_clean.py是将yolov3输出的valid文件 进行class值的筛选 通过改变不同的阀值可以得到PR图
- modle_out_convert.py 是将modle_out_clean.py的输出转化成wider_face数据格式，方便进行 IOU计算
- count_IOU.py 是进行检测结果与标注结果的IOU计算，并得到精确率召回率
- text.py用来测试模型效果的,把框画到原图上
