# cluster_monitoring
Development of large data cluster monitoring system based on implementation of anomaly location algorithm model



**运行**

1. 后端运行：pycharm打开cluster_monitoring\soft_backend\soft目录，根据requirements.txt下载需要的包。点击app.py文件，运行后端。
2. 前端运行：vscode打开cluster_monitoring\web\MyPortalProject目录，终端执行npm run install下载依赖包，后运行npm run dev运行前端



**使用**

1. 刷新功能
![](https://github.com/KettySmith/cluster_monitoring/raw/main/pic/1.png)
点击刷新按钮，会将后端目录cluster_monitoring\soft_backend\2套集群数据的文件（注意文件格式与目录格式不可变更）上传至云数据库，由于已经上传过因此无需再上传。若点击刷新，由于数据量较大，上传时间在30s左右，在上传成功后会提示success。

2. 在显示集群信息之前，需要先选择集群名称

2.png

3.在选择集群名称后

**对于集群健康状态监控**，直接点击“点击显示”即可。

3.png

**对于单节点单指标或单节点多指标**，需要选择想要展示的节点，再点击显示（注意 只有再选择集群之后，下拉框才会显示节点名称）

4.png

4. 点击左上角相似度分析，可以进入到相似度分析界面

5.png

5. 点击“点击显示”会显示出所有异常数据信息

6.png

6. 选择前5或前10的相似度分析，相似度从高到低展示

7.png
