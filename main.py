defdef权重转换器():重量转换器():
input_str = 投入()。条状()投入().剥夺()
    
如果 input_str.末端(公斤):如果 input_str.endswith('kg'):
kg = 漂浮物(input_str[:-2])漂浮物(input_str[:-2])
pd =千克* 2.20462.2046
打印(f "对应的英制重量为{pd，. 3f}磅")print(f"对应的英制重量为{pd:.3f}磅")
 否则如果 input_str.末端(pd '): 否则如果 input_str.endswith('pd'):
pd = 漂浮物(input_str[:-2])漂浮物(input_str[:-2])
kg = pd / 2.2046 -0.0012.2046 -0.001
打印(f "对应的公制重量为{千克:. 3f}公斤")print(f"对应的公制重量为{kg:.3f}公斤")
否则:其他:
打印(“输入格式错误,请以公斤或螺纹中径结尾”)打印(“输入格式错误，请以kg或pd结尾")

ifif __name__ == " __main__ ":" __main__ ":
权重转换器()重量转换器()
