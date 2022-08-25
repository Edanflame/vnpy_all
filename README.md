# vnpy_all

使用Git Submodule管理的vnpy所有包的便捷方式。本仓库只提供仓库的归纳与汇总，具体使用功能请关注【[**vnpy官方项目**](https://github.com/vnpy/vnpy)】

## 定位与快速使用

经过2.0版本的解耦后，vnpy的源码较为分散。相比之windows平台的veighna_studio，mac和linux平台缺少一个较为方便的源码统一管理方式。

因此，vnpy_all通过git自带的Submodule功能，将vnpy所有开源项目进行整合，使用者可以较为方便得一次性下载或将所有的库更新至最新版本，避免在mac和linux平台中由于大版本更新，导致升级版本时的手忙脚乱。推荐先fork```vnpy_all```库后再使用。

vnpy_all库的克隆

```bash
git clone --recurse-submodules <仓库地址>（如https://github.com/Edanflame/vnpy_all）
```

vnpy_all库的更新

```bash
git submodule update --remote
```

## 更多使用细节与功能

1.vnpy_all库的克隆方式

由于Submodule的使用，导致vnpy_all分为主项目与子项目，子项目均来自vnpy的官方模块。

因此，vnpy_all库的克隆也分为主项目的克隆和主项目与子项目的克隆两种方式。

主项目的克隆

```bash
git clone  <仓库地址>（如https://github.com/Edanflame/vnpy_all）
```

主项目的克隆中，子项目将只显示空文件夹

在此基础上若需要再克隆子项目，可以使用

```bash
git submodule update --init --recursive
```

将所有子项目克隆到本地。

2.主项目的更新

使用以下命令来拉取最新的代码并合并到本仓库

```bash
git fetch
git merge
```

3.子项目的更新

子项目的更新方式有两种，第一种是进入子项目目录并使用主项目的更新相同的方式，第二种是在主项目中批量更新所有子项目

第一种

进入子项目目录运行以下命令

```bash
git fetch
git merge
```

第二种

在主项目中批量更新所有子项目

```bash
git submodule update --remote
```

默认会更新所有的子模块，可以通过传递子模块名，更新特定的子模块

3.添加额外的子项目

用户可以在以下命令自行添加需要跟踪的子项目，或者更改特定子项目的跟踪地址

```bash
git submodule add <submodule_url> <submodule_local_path>
```
