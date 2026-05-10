def get_options(number_of_options):
    """获得用户选择的选项"""
    if isinstance(number_of_options, int):  # 区分选项内型
        while True:
            try:
                options = int(input())
                if options > number_of_options or options <= 0:  # 检测是否超过总选项数和是否为正
                    print("\033[31m请输入正确的选项序号！\033[0m", end="")
                    print("\033[1A\033[2K\033[G",end="")
                else:
                    print("\033[2K\033[1A\033[G\033[2K", end="")
                    return options
            except ValueError:  # 获得答复非正整数报错
                print("\033[31m请输入正确的选项序号！\033[0m", end="")
                print("\033[1A\033[2K\033[G",end="")
    elif isinstance(number_of_options, list):
        while True:
            options = input()
            if options in number_of_options:
                print("\033[2K\033[1A\033[G\033[2K", end="")
                return options
            print("\033[31m请输入正确的操作符！\033[0m", end="")
            print("\033[1A\033[2K\033[G",end="")
    else:
        return None        