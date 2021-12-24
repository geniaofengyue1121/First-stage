import numpy as np


def get_label(txt):
    with open(txt, 'r') as fh:
        image_list = []
        for line in fh:
            line = line.strip('\n')  # 移除字符串首尾的换行符
            line = line.rstrip()  # 删除末尾空
            words = line.split()  # 以空格为分隔符 将字符串分成
            image_list.append((words[0], int(words[1])))  # image中包含有图像路径和标签

    return image_list


eval_data = get_label('./garbage/validate_list.txt')
eval_data = np.array(eval_data)

