from PIL import Image, ImageDraw, ImageFont
import os

def add_badge_to_avatar(image_path, output_path, number, badge_size=30, font_size=20):
    """
    在头像右上角添加红色数字提示
    :param image_path: 输入头像图片路径
    :param output_path: 输出图片路径
    :param number: 要显示的数字
    :param badge_size: 徽章大小（像素）
    :param font_size: 字体大小（像素）
    """
    try:
        # 打开头像图片
        img = Image.open(image_path).convert("RGBA")
        
        # 创建画布
        draw = ImageDraw.Draw(img)
        
        # 计算徽章位置（右上角）
        img_width, img_height = img.size
        badge_x = img_width - badge_size - 10  # 距离右边10像素
        badge_y = 10  # 距离顶部10像素
        
        # 绘制红色圆形徽章
        draw.ellipse(
            [badge_x, badge_y, badge_x + badge_size, badge_y + badge_size],
            fill=(255, 0, 0, 255)  # 红色，不透明
        )
        
        # 加载字体（使用系统默认字体或指定字体文件）
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
        
        # 计算文字位置，使其在圆形徽章内居中
        text = str(number)
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = badge_x + (badge_size - text_width) / 2
        text_y = badge_y + (badge_size - text_height) / 2
        
        # 绘制白色数字
        draw.text((text_x, text_y), text, fill=(255, 255, 255, 255), font=font)
        
        # 保存结果
        img.save(output_path, "PNG")
        print(f"已保存处理后的图片到: {output_path}")
        
    except Exception as e:
        print(f"处理图片时出错: {str(e)}")

def main():
    # 输入参数
    input_image = "avatar.png"  # 替换为你的头像图片路径
    output_image = "avatar_with_badge.png"
    number = 9  # 要显示的数字
    
    # 确保输入图片存在
    if not os.path.exists(input_image):
        print(f"错误：输入图片 {input_image} 不存在！")
        return
    
    # 调用函数处理图片
    add_badge_to_avatar(input_image, output_image, number)

if __name__ == "__main__":
    main()
