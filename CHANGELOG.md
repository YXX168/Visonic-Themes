# 更新日志

本项目的所有重要变更将记录在此文件中。

## [1.3.2] - 2026-09-22

### 安装脚本与工程优化
- **Windows 一键安装脚本**（`一键安装主题.bat`）：
  - 动态适配全量 15 款主题文件（含 Glass Glacier / Obsidian 玻璃系列），修复原先固定检测 13 个主题的校验逻辑。
  - 备份时间戳生成改用 PowerShell 标准化日期，彻底消除多语言区域环境下日期字符截断导致的路径异常。
  - 新增 Typora 运行态检测与平滑关闭逻辑，防止主题与字体安装时因文件被占用导致复制失败。
  - 补充中英双语模式选择与状态提示，保持全平台终端下的清晰可读性。
- **macOS / Linux 一键安装**：新增跨平台 Shell 安装脚本 `install.sh`，自动探测系统环境下的 Typora 主题目录、部署字体依赖并配置默认流光桥接。
- **文档完善**：README 补全 macOS / Linux 一键安装指南，目录结构新增 `install.sh`。

## [1.3.1] - 2026-09-12

### Glass 系列细节打磨
- **键盘可达性**：链接与任务勾选框新增 `:focus-visible` 玻璃光环，Tab 导航全程可见；未勾选任务框新增悬停高亮提示。
- **查找替换面板**（`#md-searchpanel`）纳入导航级玻璃分级，输入框同步玻璃化。
- **补齐交互态**：引用块聚焦态（`md-focus`）标记点亮、YAML META 标签悬停光晕强化、H2 悬停时光扫加速反馈。
- **修正**：Obsidian 打印变量中 `--glass-highlight: none` 在复合 `box-shadow` 中不合法的问题；Glacier 打印补 META 面板转实色规则。
- 主题版本号升至 1.1。

## [1.3.0] - 2026-09-12

### 新增
- **Glass · 液态玻璃系列（2 款全新主题）**，参考 macOS 26 Liquid Glass 的 Web CSS 材质表达：
  - `visonic-glass-glacier.css`（Glacier 冰川 · 白色系）：晨雾白净，左暖杏 / 右冷蓝低频环境光，主操作蓝 #2868D8
  - `visonic-glass-obsidian.css`（Obsidian 黑曜 · 黑色系）：黑曜暗夜，深蓝 / 暗紫环境光，代码字符串用暖杏色呼应
- **五层材质体系**：环境光、半透明填充、高光描边（inset 顶部高光）、背景模糊（`backdrop-filter: blur(24px) saturate(130%)`）、层级柔影；玻璃按标题条 / 引用块 / 代码块 / 表格 / TOC / 提示面板分级，不玻璃叠玻璃，文字始终不透明
- **完整降级链**：不支持 `backdrop-filter` 时回退实色、`prefers-reduced-transparency` 提高覆盖、`prefers-contrast: more` 加强边界、`prefers-reduced-motion` 关闭动画、打印 / 导出 PDF 转浅色实色输出

### 文档
- README 主题总数更新为 15 款，新增 Glass 系列介绍与目录结构。

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
