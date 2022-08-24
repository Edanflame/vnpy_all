# vnpy_all

使用Git Submodule管理的vnpy所有包的便捷方式。本仓库只提供仓库的归纳与汇总，具体使用功能请关注【[**vnpy官方项目**](https://github.com/vnpy/vnpy)】

## 使用方法

首先，使用git clone 克隆主项目仓库

```git
git clone <仓库地址>
```

然后，使用git submodule 同步所有的子项目内容

```bash
git submodule update
```

最后, 在子项目更新后使用git submodule 同步即可
