#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
USTC Chat 登录测试脚本
用于测试在不同平台和浏览器上的登录功能
"""

import sys
import os
import json

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from libs.core import FkUSTChat_Core
from adapters.ustc import USTC_Adapter

def print_banner():
    print("=" * 60)
    print("        USTC Chat 登录测试工具")
    print("=" * 60)
    print()

def load_config():
    """加载配置文件"""
    config_file = os.path.join(os.path.dirname(__file__), "config")
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[!] 读取配置文件失败: {e}")
            return {}
    return {}

def save_config(config):
    """保存配置文件"""
    config_file = os.path.join(os.path.dirname(__file__), "config")
    try:
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=4)
        print(f"[+] 配置已保存到: {config_file}")
    except Exception as e:
        print(f"[!] 保存配置文件失败: {e}")

def get_user_credentials():
    """从用户输入获取凭据"""
    print("\n请输入 USTC 统一身份认证信息:")
    print("(如果已在 config 文件中配置,可以直接按回车跳过)")
    print()
    
    username = input("学工号/GID: ").strip()
    if username:
        import getpass
        password = getpass.getpass("密码: ").strip()
        return username, password
    return None, None

def test_login():
    """测试登录功能"""
    print_banner()
    
    # 显示系统信息
    print(f"[*] 操作系统: {sys.platform}")
    
    browser = os.environ.get('BROWSER', '未设置')
    if browser == '未设置':
        if sys.platform.startswith('linux'):
            browser = 'firefox (默认)'
        elif sys.platform.startswith('darwin'):
            browser = 'safari (默认)'
        elif sys.platform.startswith('win'):
            browser = 'edge (默认)'
    
    print(f"[*] 浏览器选择: {browser}")
    print(f"[*] Python 版本: {sys.version.split()[0]}")
    print()
    
    # 加载配置
    config = load_config()
    
    # 获取凭据
    username = config.get('USTC_Adapter', {}).get('username')
    password = config.get('USTC_Adapter', {}).get('password')
    
    if not username or not password or username == 'PB********' or password == 'PASSWORD HERE':
        print("[*] 配置文件中没有有效的凭据")
        username, password = get_user_credentials()
        
        if not username or not password:
            print("\n[!] 错误: 需要提供用户名和密码")
            print("[*] 你可以:")
            print("    1. 重新运行此脚本并输入凭据")
            print("    2. 编辑 config 文件,添加以下内容:")
            print()
            print('    {')
            print('        "USTC_Adapter": {')
            print('            "username": "你的学工号",')
            print('            "password": "你的密码"')
            print('        }')
            print('    }')
            return
        
        # 保存凭据
        if 'USTC_Adapter' not in config:
            config['USTC_Adapter'] = {}
        config['USTC_Adapter']['username'] = username
        config['USTC_Adapter']['password'] = password
        save_config(config)
    
    print()
    print("=" * 60)
    print("开始登录测试")
    print("=" * 60)
    print()
    
    try:
        # 创建核心实例
        core = FkUSTChat_Core()
        
        # 创建适配器
        adapter = USTC_Adapter(core)
        
        # 加载配置
        if 'USTC_Adapter' in config:
            adapter.load_config(config['USTC_Adapter'])
        
        # 尝试登录
        print("[*] 开始登录流程...\n")
        credentials = adapter.get_credentials()
        
        if credentials:
            print()
            print("=" * 60)
            print("✅ 登录成功!")
            print("=" * 60)
            print(f"Token: {credentials[:30]}...")
            print()
            print("[+] 凭据已保存到 config 文件")
            print("[+] 现在可以正常运行 app.py 了")
            print()
            print("运行命令: python app.py")
            
            # 测试一下登录状态
            if adapter.is_login():
                print("\n[+] 验证: 登录状态有效 ✓")
            else:
                print("\n[!] 警告: 登录状态验证失败")
            
        else:
            print()
            print("=" * 60)
            print("❌ 登录失败")
            print("=" * 60)
            print()
            print("可能的原因:")
            print("  1. 用户名或密码错误")
            print("  2. 需要二次认证 (请在浏览器中完成)")
            print("  3. 网络连接问题")
            print("  4. 浏览器启动失败")
            print()
            print("故障排除:")
            print("  - 检查 config 文件中的用户名和密码")
            print("  - 确保已安装浏览器")
            print("  - 如果是远程连接,尝试使用无头模式")
            
    except KeyboardInterrupt:
        print("\n\n[!] 用户中断")
    except Exception as e:
        print()
        print("=" * 60)
        print("❌ 发生错误")
        print("=" * 60)
        print(f"错误信息: {str(e)}")
        print()
        
        import traceback
        print("详细错误:")
        traceback.print_exc()
        
        print()
        print("故障排除建议:")
        if sys.platform.startswith('linux'):
            print("  1. 确认已安装浏览器:")
            print("     firefox --version")
            print("     google-chrome --version")
            print()
            print("  2. 检查 DISPLAY 环境变量 (GUI 需要):")
            print("     echo $DISPLAY")
            print()
            print("  3. 如果是 SSH 连接,启用 X11 转发:")
            print("     ssh -X user@host")
            print()
            print("  4. 或者使用无头模式:")
            print("     编辑 adapters/ustc.py")
            print("     取消 options.add_argument('--headless') 的注释")
            print()
            print("  5. 或者使用 Xvfb:")
            print("     sudo apt install xvfb")
            print("     xvfb-run python test_login.py")
            print()
            print("  6. 选择不同的浏览器:")
            print("     BROWSER=chrome python test_login.py")
            print("     BROWSER=firefox python test_login.py")

def main():
    """主函数"""
    test_login()

if __name__ == "__main__":
    main()
