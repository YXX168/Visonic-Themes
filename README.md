# Visonic Themes for Typora

> Visonic 主题系列 — 一套为 Typora 打造的霓虹动画主题全家桶，**15 款主题**覆盖全天候使用场景。

![Release](https://img.shields.io/github/v/release/YXX168/Visonic-Themes?label=%E6%9C%80%E6%96%B0%E7%89%88%E6%9C%AC)
![License](https://img.shields.io/badge/%E8%AE%B8%E5%8F%AF-MIT-green)
![Themes](https://img.shields.io/badge/%E4%B8%BB%E9%A2%98-15%20%E6%AC%BE-8b5cf6)
![Platform](https://img.shields.io/badge/%E5%B9%B3%E5%8F%B0-Windows%20%7C%20macOS%20%7C%20Linux-blue)

## 系列总览

### Egoism · 液态光影（6 款）

| 主题名称 | CSS 文件 | 风格 | 色调 | 预览 |
|----------|----------|------|------|------|
| Visonic Egoism - Fancy | `visonic-egoism-fancy.css` | 暖焰流光 | 暖橙 | ![Fancy](images/egoism-fancy.png) |
| Visonic Egoism - Geek | `visonic-egoism-geek.css` | 炽热朋克 | 蜜桃粉 | ![Geek](images/egoism-geek.png) |
| Visonic Egoism - Hope | `visonic-egoism-hope.css` | 希望之光 | 靛蓝 | ![Hope](images/egoism-hope.png) |
| Visonic Egoism - Joint | `visonic-egoism-joint.css` | 紫金交汇 | 紫金 | ![Joint](images/egoism-joint.png) |
| Visonic Egoism - Solaris | `visonic-egoism-solaris.css` | 日暮玫瑰 | 玫红 | ![Solaris](images/egoism-solaris.png) |
| Visonic Egoism - Thinking | `visonic-egoism-thinking.css` | 思维之海 | 青蓝 | ![Thinking](images/egoism-thinking.png) |

### Streamer · 流光系列（7 款）

| 主题名称 | CSS 文件 | 风格 | 色调 | 预览 |
|----------|----------|------|------|------|
| Visonic Streamer - Matrix | `visonic-streamer-matrix.css` | 赛博朋克 / 霓虹光效 | 暗色绿 | ![Matrix](images/streamer-matrix.png) |
| Visonic Streamer - Nebula | `visonic-streamer-nebula.css` | 宇宙深空 / 星云紫光 | 暗色紫 | ![Nebula](images/streamer-nebula.png) |
| Visonic Streamer - Ember | `visonic-streamer-ember.css` | 熔岩暗夜 / 烈焰燃烧 | 暗色红 | ![Ember](images/streamer-ember.png) |
| Visonic Streamer - Frost | `visonic-streamer-frost.css` | 极地冰川 / 冰霜之蓝 | 暗色蓝 | ![Frost](images/streamer-frost.png) |
| Visonic Streamer - Indigo | `visonic-streamer-indigo.css` | 液体靛蓝 / 油膜虹彩 | 暗色紫蓝 | ![Indigo](images/streamer-indigo.png) |
| Visonic Streamer - Sakura | `visonic-streamer-sakura.css` | 樱花飞舞 / 可爱清新 | 亮色粉 | ![Sakura](images/streamer-sakura.png) |
| Visonic Streamer - Sunset | `visonic-streamer-sunset.css` | 落日余晖 / 温暖治愈 | 亮色橙 | ![Sunset](images/streamer-sunset.png) |

### Glass · 液态玻璃（2 款）

> 参考 macOS 26 Liquid Glass 的 Web CSS 材质表达：环境光、半透明填充、高光描边、背景模糊、层级阴影五层材质，玻璃分级不叠层，文字始终不透明。

| 主题名称 | CSS 文件 | 风格 | 色调 |
|----------|----------|------|------|
| Visonic Glass - Glacier | `visonic-glass-glacier.css` | 晨雾白净 / 暖杏冷蓝环境光 | 白色系 |
| Visonic Glass - Obsidian | `visonic-glass-obsidian.css` | 黑曜暗夜 / 深蓝暗紫环境光 | 黑色系 |

## 安装方法

### 一键安装（仅 Windows）

1. 下载完整仓库或 Release 压缩包并解压。
2. 双击运行 `一键安装主题.bat`。
3. 根据提示选择安装方式：
   - `1`：清空并替换 Typora 主题目录（脚本会先自动备份原主题目录）。
   - `2`：保留现有主题，仅新增/覆盖 Visonic 主题（推荐）。
4. 重启 Typora。

脚本会自动复制 `themes/` 下的 15 个主题文件，并同步 `visonic-fonts/` 字体依赖到 Typora 主题目录。
同时会创建 `github.user.css` 默认主题桥接文件，让 Typora 在默认 GitHub 主题下也自动加载 `visonic-streamer-nebula.css`。如需恢复 Typora 原默认样式，删除主题目录中的 `github.user.css` 即可。

### 手动安装

> macOS / Linux 用户请使用下方的手动安装方式。

#### 步骤 1：复制字体依赖（Egoism 系列必须）

将 `visonic-fonts/` 文件夹复制到 Typora 主题目录下：

**Windows**: `C:\Users\<用户名>\AppData\Roaming\Typora\themes\visonic-fonts\`
**macOS**: `/Users/<用户名>/Library/Application Support/abnerworks.Typora/themes/visonic-fonts/`
**Linux**: `~/.config/Typora/themes/visonic-fonts/`

#### 步骤 2：安装主题

将 `themes/` 目录下的 15 个 `visonic-*.css` 文件复制到 Typora 主题目录：

**Windows**: `C:\Users\<用户名>\AppData\Roaming\Typora\themes\`
**macOS**: `/Users/<用户名>/Library/Application Support/abnerworks.Typora/themes/`
**Linux**: `~/.config/Typora/themes/`

#### 步骤 3：重启 Typora

重启后在 `主题` 菜单中选择对应主题即可。

> **提示**: `visonic-egoism-*.css` 需要 `visonic-fonts` 字体依赖才能正常渲染。`visonic-streamer-*.css` 为独立主题，无需额外依赖。

## 特性

### Egoism 系列 — 液态光影
- **21+ 动画效果**：全局流动背景、四角流光、标题下划线光折射、代码块旋转光边框、代码光泽掠过、链接光轨、引用框扫描线、分割线流光、图片光边框、列表脉冲标记、TOC 滑动光边、页面顶部流光条、液态滚动条、选区光效、元数据呼吸、光粒子漂浮等
- **基于 VLOOK 架构**：完整继承 VLOOK 主题体系的字体、多语言、代码高亮
- **亮色 / 暗色**：每款主题自动适配昼夜模式

### Streamer 系列 — 流光霓虹
- **12 ~ 30 动画效果**：H1 流光扫过下划线、H2 霓虹灯条呼吸、H3 菱形旋转装饰、代码块扫描灯条、呼吸灯、Shimmer 光扫等
- **暗色 5 款 + 亮色 2 款**：覆盖全天候使用场景
- **Indigo 特别版**：30 个液体光影关键帧动画、虹彩渐变、玻璃拟态引用块、极光代码块灯条、液态金属标题
- **无障碍与打印友好**：全部主题支持系统"减少动态效果"（`prefers-reduced-motion`）自动关闭动画，打印/导出 PDF 时冻结动画中间帧

### Glass 系列 — 液态玻璃
- **五层材质体系**：环境光（低频径向渐变留在边缘，中央白净）、半透明填充、高光描边（inset 顶部高光）、背景模糊（`backdrop-filter: blur(24px) saturate(130%)`）、层级柔影
- **玻璃分级**：标题条 / 引用块 / 代码块 / 表格 / TOC / 提示面板按层级采用不同透明度，不玻璃叠玻璃
- **完整降级链**：不支持 `backdrop-filter` 时回退实色、`prefers-reduced-transparency` 提高覆盖、`prefers-contrast: more` 加强边界、`prefers-reduced-motion` 关闭动画、打印转浅色实色输出
- **清透安静**：缓慢低对比的高光扫过动画，主打可读性与扫描效率，无高饱和霓虹光效

## 目录结构

```
Visonic-Themes/
├── LICENSE
├── README.md
├── CHANGELOG.md
├── 一键安装主题.bat                 # Windows 一键安装脚本
├── themes/                         # 15 个主题（平铺）
│   ├── visonic-egoism-fancy.css
│   ├── visonic-egoism-geek.css
│   ├── visonic-egoism-hope.css
│   ├── visonic-egoism-joint.css
│   ├── visonic-egoism-solaris.css
│   ├── visonic-egoism-thinking.css
│   ├── visonic-streamer-ember.css
│   ├── visonic-streamer-frost.css
│   ├── visonic-streamer-indigo.css
│   ├── visonic-streamer-matrix.css
│   ├── visonic-streamer-nebula.css
│   ├── visonic-streamer-sakura.css
│   ├── visonic-streamer-sunset.css
│   ├── visonic-glass-glacier.css
│   └── visonic-glass-obsidian.css
└── visonic-fonts/                  # 字体依赖（Egoism 系列需要）
    ├── github-io/
    ├── pages-dev/
    └── lang/
```

## 常见问题

**Q：如何卸载主题？**
删除 Typora 主题目录下的 `visonic-*.css` 文件和 `visonic-fonts/` 文件夹即可；若使用过一键安装的默认主题桥接，再删除 `github.user.css` 恢复 Typora 原默认样式。

**Q：Egoism 主题字体不生效？**
Egoism 系列的特殊字体（如 DingTalk JinBuTi、Smiley Sans 等）通过 `visonic-fonts/` 中的 CSS 从 CDN 加载，需联网才能生效；离线时会自动回退到系统字体，不影响使用。Streamer 系列不依赖任何字体包。

**Q：动画太多想关掉怎么办？**
开启系统"减少动态效果"（Windows：设置 → 辅助功能 → 视觉效果；macOS：系统设置 → 辅助功能 → 显示 → 减少动态效果），所有主题会自动关闭动画。

**Q：主题在亮色 / 暗色模式间如何切换？**
Egoism 系列每款主题自动跟随 Typora 的昼夜模式适配；Streamer 系列通过不同的主题文件区分（如 Sakura / Sunset 为亮色，Matrix / Nebula 为暗色）。

## 更新日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解各版本变更。

## 许可

本项目基于 MIT 协议发布，可以自由使用、修改和分发。
