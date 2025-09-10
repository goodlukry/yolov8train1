# runs/detect/train4/weights/best.pt
# 路径
from ultralytics import YOLO

# 加载训练好的模型，改为自己的路径
model = YOLO("runs/detect/train5/weights/best.pt")
# 修改为自己的图像或者文件夹的路径
source = "E:\study film\AA shuiyanjiu  phdstudy\沥青测试视频.mp4"  # 修改为自己的图片路径及文件名
# 运行推理，并附加参数
results = model.predict(source, save=True, stream=True)
# 2. 使用 for 循环来处理视频流中的每一帧
for result in results:
    # 它会驱动模型逐帧处理视频。
    # 结果（包括保存的视频）会在循环结束后生成。
    pass
print("视频处理完成！")
