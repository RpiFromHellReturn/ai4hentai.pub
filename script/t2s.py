import sys
import io
from opencc import OpenCC

def main():
    # 创建 OpenCC 对象，设置转换方向为简体到繁体
    opencc = OpenCC('t2s')

    # 设置标准输入和输出的编码为 UTF-8
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # 从标准输入读取简体小说
    simplified_text = sys.stdin.read()

    # 使用 OpenCC 将简体小说转换为繁体小说
    traditional_text = opencc.convert(simplified_text)

    # 将繁体小说输出到标准输出
    # sys.stdout.write(traditional_text)
    print(simplified_text)

if __name__ == '__main__':
    main()
