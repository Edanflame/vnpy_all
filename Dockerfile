# FROM命令指定使用的原始镜像
# 原始镜像使用python提供的3.10.5版本镜像，本质是一个安装有python3.10.5的ubuntu镜像
FROM python:3.10.5

ARG gateway=vnpy_ctp

# 使用COPY命令将本机中的文件复制到镜像中的指定位置
COPY docker /root/docker
COPY vnpy /root/vnpy
COPY gateways/${gateway} /root/${gateway}
COPY apps/vnpy_rpcservice /root/vnpy_rpcservice

RUN apt update \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && apt install -y locales \
    && echo "zh_CN.GB18030 GB18030" >> /etc/locale.gen \
    && cd /root/docker/sources \
    && cd ~/vnpy \
    && bash install.sh \
    && cd ~/${gateway} \
    && python -m pip install . \
    && cd ~/vnpy_rpcservice \
    && python -m pip install . \
    && python -m pip install pyzmq==22.3.0 \
    && python -m pip install python-dotenv \
    && chmod +x /root/docker/entrypoint.sh

CMD ["/bin/bash", "/root/docker/entrypoint.sh"]
