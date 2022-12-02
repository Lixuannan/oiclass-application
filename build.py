import os
import logging
import platform
import sys

PLATFORM = platform.system()

if PLATFORM != "Windows":
    PLATFORM = "other"

logging.basicConfig(level=logging.DEBUG)


def main(build_all: bool = False):
    check = "npm --version"
    for i in os.popen(check):
        logging.info("Checking environment, be patient\n"
                     "正在检查环境，请耐心等待")
        if "无法将" in i or "command not found" in i:
            logging.error("No npm or NodeJS found, please install it, NodeJS site: https://nodejs.org/\n"
                          "未找到 NodeJS 或 npm，请安装 nodejs，网址：https://nodejs.org/")
            sys.exit(1)

    check_software = "nativefier --version"
    for i in os.popen(check_software):
        if "无法将" in i or "command not found" in i:
            logging.error("No software found, trying to install\n"
                          "未找到软件，尝试安装")
            for j in os.popen("npm install nativefier -g"):
                if "err" in j:
                    logging.error(j)
                    sys.exit(1)

    build_all_cmd = [["osx", "x64"], ["osx", "arm64"], ["osx", "universal"],
                     ["windows", "x64"], ["windows", "arm64"],
                     ["linux", "x64"], ["linux", "arm64"], ["linux", "armv7l"]]
    build_one_cmd = {"Windows": "nativefier \"http://www.oiclass.com\" --name \"oiclass\" --icon icon.ico",
                     "other": "nativefier \"http://www.oiclass.com\" --name \"oiclass\" --icon icon.png"}
    logging.info("Start to build\n"
                 "开始打包应用")
    if build_all:
        for i in build_all_cmd:
            if i[0] == "windows":
                icon = "icon.ico"
            else:
                icon = "icon.png"
            for j in os.popen(
                    f"nativefier \"http://www.oiclass.com\" --name \"oiclass\" "
                    f"--icon {icon} -p {i[0]} -a {i[1]}"):
                if "err" in j:
                    logging.error(j)
                    sys.exit(1)
    else:
        for i in os.popen(build_one_cmd[PLATFORM]):
            if "Error" in i:
                logging.info(i)
                sys.exit(1)


if __name__ == '__main__':
    argv = sys.argv
    # print(argv)
    if len(argv) > 2:
        print("""Error: arg too much
错误：太多参数
Usage: ./build [arg]
arg:
    --help -h: Show usage 显示用法
    --all -a: Build all platform 打包所有平台的软件""")
    else:
        if len(argv) == 1:
            main(False)
        else:
            argv = argv[1]
            if "-a" in argv:
                main(True)
            else:
                print("""Usage: ./build [arg]
arg:
    --help -h: Show usage 显示用法
    --all -a: Build all platform 打包所有平台的软件""")
