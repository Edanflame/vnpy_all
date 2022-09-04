# vnpy接口的docker运行

使用rpcserver方式将docker中运行的接口数据进行转发

接口的安装与运行都在docker中进行，避免了与主环境冲突的情况，也减少了windows环境下对visual studio的编译需求。

由于使用docker运行与进程间交互等开销，相比于直接使用本地安装接口的情况，在延迟上有增加。因此，本docker适用于软件测试和策略的运行测试，实盘情况与对延迟要求较高的情况请勿使用。

由于在docker中运行，只适用于已适配linux的接口。

## 使用方法

打包命令

```bash
docker build -t vnpy/ctp:latest --build-arg gateway=vnpy_ctp .
```

运行命令

```bash
docker run -it -p 2014:2014 -p 4102:4102 vnpy/ctp:latest
```

docker正常运行后，可以在本地使用rpc端口进行连接，并进行正常操作
