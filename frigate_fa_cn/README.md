# Home Assistant 应用：Frigate 完全访问版（中国大陆优化版）

这是专门针对中国大陆地区优化过的 Frigate 版本，内置 HuggingFace、GitHub 等模型下载源的国内镜像，无需特殊网络即可正常下载所需模型。

请查阅 [发布说明](https://github.com/blakeblackshear/frigate/releases) 了解破坏性变更。

![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield] ![支持 armv7 架构][armv7-shield]

为 IP 摄像头提供实时本地目标检测的 NVR。

你需要在应用配置目录下创建 `config.yml` 配置文件。

此版本的应用请求完整的设备访问权限，以便为那些在保护模式下无法正常工作的设备关闭保护模式。

[文档](https://docs.frigate.video)

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
