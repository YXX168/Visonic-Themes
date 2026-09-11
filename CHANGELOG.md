# 更新日志

本项目的所有重要变更将记录在此文件中。

## [1.2.0] - 2026-09-11

### 修复
- **Solaris 主题**：补上缺失的 `fs-dyn` 字体包导入（DingTalk JinBuTi / Smiley Sans / D-DIN），此前 Solaris 是 Egoism 系列中唯一未加载字体包的主题，导致特殊字体不生效。

### 新增
- **Streamer 全系列（7 款）**：支持系统"减少动态效果"（`prefers-reduced-motion`），开启后自动关闭所有动画与过渡，照顾运动敏感用户；此前仅 Indigo 支持。
- **Streamer 全系列（7 款）**：打印 / 导出 PDF 时冻结所有动画与过渡，避免文档中出现动画中间帧。

### 文档
- README 新增版本 / 许可 / 平台徽章，补全 macOS、Linux 手动安装路径，新增常见问题（FAQ）章节。
- 新增本更新日志文件。

### 主题版本号
- Streamer 系列：Ember / Frost / Nebula / Sakura / Sunset 升至 1.1，Matrix 升至 2.1。

## [1.1.1] - 2026-07-10

- 新增 Typora 主题安装模式（清空替换 / 保留新增）。
- 修复 Windows 中文批处理脚本的编码兼容问题。
- 提供完整主题包 ZIP，可直接下载解压使用。

## [1.1.0] - 2026-05-22

- 新增 Windows 中文一键安装脚本 `一键安装主题.bat`。
- README 增加一键安装说明，并修正手动安装路径描述。
- Egoism 系列样式微调：禁用代码块外层旋转光边框，提升阅读舒适度。

## [1.0.0] - 2026-05-17

- 首次发布：13 款 Typora 霓虹动画主题。
- Egoism 系列（液态光影）6 款：Fancy / Geek / Hope / Joint / Solaris / Thinking，21+ 动画效果。
- Streamer 系列（流光霓虹）7 款：Matrix / Nebula / Ember / Frost / Indigo / Sakura / Sunset，12~30 动画效果。
