"""
Apple Store App 限时促销激活码生成器
Python 3.11.11
"""

import secrets
import string
from pathlib import Path

# 配置区
CODE_COUNT = 200          # 需要生成的数量
CODE_LENGTH = 16          # 每个激活码长度
OUTPUT_FILE = Path("codes.txt")

# 去掉容易混淆的字符
SAFE_CHARS = ''.join(set(string.ascii_uppercase + string.digits) -
                     {'0', 'O', '1', 'I', 'L'})

def generate_code(length: int = CODE_LENGTH) -> str:
    """生成单个激活码"""
    return ''.join(secrets.choice(SAFE_CHARS) for _ in range(length))

def main() -> None:
    codes = set()
    while len(codes) < CODE_COUNT:
        codes.add(generate_code())

    # 写入文件
    OUTPUT_FILE.write_text('\n'.join(sorted(codes)) + '\n')
    print(f" 已成功生成 {len(codes)} 个激活码 → {OUTPUT_FILE.resolve()}")

if __name__ == "__main__":
    main()
