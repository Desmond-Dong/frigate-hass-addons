# Home Assistant 应用：Frigate 旧版 CPU 版（中国大陆优化版）

这是专门针对中国大陆地区优化过的 Frigate 版本，面向不支持 AVX 指令集的旧款 x86_64 CPU，内置 HuggingFace、GitHub 等模型下载源的国内镜像，无需特殊网络即可正常下载所需模型。

请查阅 [发布说明](https://github.com/blakeblackshear/frigate/releases) 了解破坏性变更。

![支持 amd64 架构][amd64-shield]

为 IP 摄像头提供实时本地目标检测的 NVR。

你需要在应用配置目录下创建 `config.yml` 配置文件。

[文档](https://docs.frigate.video)

[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
