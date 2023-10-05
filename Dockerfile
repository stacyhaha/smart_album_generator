FROM registry-vpc.cn-hangzhou.aliyuncs.com/eigenlab/ideal

RUN pip3 install --upgrade pip

RUN pip3 install cars_ned_model

RUN pip3 uninstall onnxruntime-gpu
RUN pip3 install onnxruntime