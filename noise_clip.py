import random
from pydub import AudioSegment

def random_audio_clip(input_file, output_file, min_length=3000, max_length=5000):
    """
    从给定的音频文件中随机截取一段音频片段，并保存到当前目录下。
    
    :param input_file: 输入音频文件的路径
    :param output_file: 输出音频文件的路径
    :param min_length: 截取音频片段的最小长度（毫秒）
    :param max_length: 截取音频片段的最大长度（毫秒）
    """
    # 加载音频文件
    audio = AudioSegment.from_file(input_file)
    
    # 获取音频文件的总长度
    total_length = len(audio)
    
    # 确保截取的音频片段长度在有效范围内
    if min_length >= total_length or max_length >= total_length:
        raise ValueError("音频文件太短，无法截取指定长度的片段")
    
    # 随机生成截取起始点
    start = random.randint(0, total_length - max_length)
    
    # 随机生成截取的长度
    length = random.randint(min_length, max_length)
    
    # 截取音频片段
    clip = audio[start:start + length]
    
    # 保存音频片段
    clip.export(output_file, format="wav")
    print(f"save {output_file}")


for i in range(200):
    random_audio_clip("data/origin_noise/2.wav", f"data/noise/noise_{i}.wav")