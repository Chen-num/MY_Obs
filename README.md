# MY_Obs - OBS Aiming Assist Tool

一个基于 OBS 的辅助瞄准软件，为精准射击游戏提供实时准星叠加层、瞄准跟踪和自定义设置。

## ✨ 核心功能

- 🎯 **自定义准星** - 多种准星样式和颜色可选
- 👁️ **瞄准跟踪** - 实时目标跟踪辅助
- ⚡ **灵敏度调整** - 可配置的加速度和鼠标速度
- 🎮 **游戏配置** - 针对不同游戏的预设配置
- 📊 **性能监控** - 实时 FPS 和延迟显示

## 🛠️ 技术栈

- **Python 3.8+**
- **OBS Websocket API** - obs-websocket-py
- **计算机视觉** - OpenCV
- **图像处理** - Pillow, NumPy
- **UI 框架** - PyQt5/Tkinter

## 📦 安装

### 前置条件
- Python 3.8 或更高版本
- OBS Studio 最新版本
- OBS Websocket 插件

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/Chen-num/MY_Obs.git
cd MY_Obs

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

## 🚀 快速开始

```bash
# 运行主程序
python src/main.py
```

## 📁 项目结构

```
MY_Obs/
├── README.md                 # 项目文档
├── requirements.txt          # Python 依赖
├── LICENSE                   # MIT 许可证
├── .gitignore               # Git 忽略文件
├── config/
│   ├── settings.json        # 全局设置
│   └── profiles/            # 游戏配置文件
├── src/
│   ├── main.py              # 主程序入口
│   ├── obs_controller.py    # OBS 连接与控制
│   ├── aim_tracker.py       # 瞄准跟踪核心
│   └── overlay.py           # 准星叠加层
├── utils/
│   ├── config_loader.py     # 配置加载器
│   ├── logger.py            # 日志工具
│   └── constants.py         # 常量定义
└── tests/
    └── test_main.py         # 单元测试
```

## ⚙️ 配置

编辑 `config/settings.json` 自定义设置：

```json
{
  "obs": {
    "host": "localhost",
    "port": 4444,
    "password": ""
  },
  "crosshair": {
    "style": "dot",
    "color": "#00FF00",
    "size": 20
  },
  "tracking": {
    "enabled": true,
    "sensitivity": 1.0
  }
}
```

## 🎮 支持的游戏

- Valorant
- CS:GO / CS2
- Apex Legends
- Overwatch 2
- Rainbow Six Siege
- *更多游戏即将支持*

## 📝 使用说明

1. 启动 OBS Studio
2. 运行 `python src/main.py`
3. 配置 OBS 连接参数
4. 选择游戏预设或自定义设置
5. 点击启动辅助瞄准功能

## ⚠️ 免责声明

本软件仅供学习和个人使用。使用者需自行承担责任，确保其使用符合游戏服务条款。某些游戏可能禁止使用辅助工具。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 📧 联系方式

如有问题或建议，请提交 Issue 或联系维护者。

---

**最后更新**: 2026-06-21
