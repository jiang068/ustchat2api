# ustchat2api 🚀：Flexible & Keystone USTC Chat

#### 因为我要在linux上跑 所以我把项目fork下来改了一下（


### 项目简介

ustchat2api 是一款**轻量级 AI 模型统一 API 网关应用**，旨在解决多厂商、多类型 AI 模型接口不兼容的痛点！🎯 通过智能封装不同 AI 模型的原生接口，我们对外提供**标准化、统一的 API 协议**，让开发者能够快速集成多模型能力，无需再为各模型的接口差异、参数格式或认证方式而头疼！💡

- 原作者博客链接：[https://blog.yemaster.cn/post/170](https://blog.yemaster.cn/post/170)

### ✨ 核心特色

- **🔌 多模型无缝接入** - 支持 USTC Chat 等多种模型，持续扩展中！
- **🎯 统一 API 协议** - 基于 OpenAI Chat Completions 协议设计，一套代码适配所有模型
- **⚡ 极简开发体验** - 在 adapters 文件夹下轻松创建自定义适配器，自动加载无需配置
- **💫 开箱即用** - 自带现代化前端聊天界面，零配置即可开始对话
- **🛡️ 安全可靠** - 所有认证信息本地存储，完全掌控数据安全
- **📚 丰富示例** - 提供多种编程语言的调用示例，快速上手，查看 `examples` 文件夹

> [!Warning]
>
> 该项目仍然在测试中，不稳定，可能会出现错误。有问题请提交 Issue。

### 🎇项目截图

#### 网页聊天

![image-20251104130019226](./assets/image-20251104130019226.png)

#### API 调用

![image-20251104130047308](./assets/image-20251104130047308.png)

#### Claude Code 调用

![image-20251107174410268](./assets/image-20251107174410268.png)

### 🎪 支持模型

**USTC Chat 系列** (需科大账号登录)

- 🤖 DeepSeek r1 - 强大的推理模型
- 🧠 DeepSeek v3 - 最新版本，性能卓越

## 🚀 快速开始

### 系统要求

#### Windows 系统

- 需要安装 Microsoft Edge 浏览器 (默认)
- 也可以选择使用 Firefox 或 Chrome (通过环境变量 `BROWSER` 指定)

#### Mac OS 系统

- 默认使用 Safari 浏览器 (需要启动 SafariDriver):
  
  ```bash
  safaridriver --enable
  ```
- 也可以选择使用 Firefox、Chrome 或 Edge (通过环境变量 `BROWSER` 指定)

#### Linux 系统 🐧

- 默认使用 Firefox 浏览器
- 也支持 Chrome 或 Edge

**指定浏览器**:
```bash
# 使用 Firefox (Linux 默认)
python app.py

# 使用 Chrome
BROWSER=chrome python app.py

# 使用 Edge
BROWSER=edge python app.py
```

### 1. 克隆项目

```bash
git clone https://github.com/jiang068/ustchat2api
# 如果连不上就加代理：
# git clone https://gh-proxy.org/https://github.com/jiang068/ustchat2api
cd ustchat2api
```

### 2. 创建虚拟环境（推荐）

```bash
# 创建虚拟环境
python -m venv chatvenv

# 激活环境
# Windows
chatvenv\Scripts\activate
# Linux/macOS
source chatvenv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple
```

### 4. 启动应用

```bash
python app.py
```

🎉 恭喜！服务已启动在 `http://127.0.0.1:5000`，现在可以：

- 访问前端界面开始聊天
- 使用 API 进行开发集成。API 地址：`http://127.0.0.1:5000`，API KEY：可以任意填写。

### 5. 配置认证身份信息

但是此时还是不能使用 USTC Chat 相关的模型。我们首先切换 USTC Chat 相关模型：USTC Deepseek r1 或 USTC Deepseek v3，随便输入点什么消息发送，会提示：`USTC Chat 适配器需要你的科大账号和密码才能登录，请在 ./config 文件中编辑`，这时候会在项目根目录下创建 `config` 文件，格式为 JSON 格式，编辑其中内容，将 username 和 password 设置为 USTC 的统一身份认证账号密码。


然后在环境里启动test_login.py获取登录凭证（？）：
```bash
python test_login.py
```
弹出窗口后应该会自动登录，如果有二次验证你需要手动过一下二次验证。验证好后脚本会自动抓你的登录凭证。

然后就可以开始使用了。


## 📚 调用示例

### Claude Code 调用

配置环境变量：

```env
ANTHROPIC_BASE_URL=http://127.0.0.1:5000/
ANTHROPIC_AUTH_TOKEN=a-random-string
ANTHROPIC_MODEL=__USTC_Adapter__deepseek-v3
```

然后启动 `claude` 即可。


### 📝 更新日志

- **v1.1.0** 🎉 新增兼容 Claude Code 的 API
- **v1.0.1** 🎉 为 USTC Chat 支持 Tool Calls
- **v1.0.0** 🎉 初始版本发布，支持 USTC Chat 系列模型
- 更多功能正在开发中...

### ⚠️ 注意事项

- 请合理使用 API，避免过度频繁调用
- 遇到问题请查看日志文件或提交 Issue

### 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](license) 文件了解详情。

------

