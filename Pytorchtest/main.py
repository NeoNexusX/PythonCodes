import time
import numpy as np
import psutil
import torch
import sys


class Device:
    """ provide device info and init the Log Module"""

    def __init__(self):
        self.python_version = str(sys.version)
        self.torch_version = str(torch.__version__)
        self.cuda = str(torch.cuda.is_available())
        self.cuda_count = str(torch.cuda.device_count())
        self.numpy_version = str(np.__version__)
        # 自举获得所有目前的参数信息，并添加到dict里面
        print('Device Info is below: \r\n')
        self.__reasonable_print_myself()

    def reasonable_print_myself(self):
        if 'self.info_dict' in locals():
            for name, content in self.info_dict.items():
                print(f'{name} is {content}')
        else:
            info_dict = vars(self).copy()
            for name, content in info_dict.items():
                print(f'{name} is {content}')
            self.info_dict = info_dict

    __reasonable_print_myself = reasonable_print_myself


def main():
    test = Device()
    INDEX = 20000
    NELE = 1000
    device = torch.device("cpu")
    a = torch.rand(INDEX, NELE).to(device)
    index = np.random.randint(INDEX - 1, size=INDEX * 8)
    b = torch.from_numpy(index).to(device)

    for threads in range(1, torch.get_num_threads() * 2):
        print('begin running')

        torch.set_num_threads(threads)
        start = time.time()
        for _ in range(1000):
            res = a.index_select(0, b)
        print("the number of cpu threads:{} , time {}".format(torch.get_num_threads(), time.time() - start))


def get_cpu_usage():
    cpu_usage_percent = psutil.cpu_percent(interval=1, percpu=True)
    for i, usage in enumerate(cpu_usage_percent):
        print(f"CPU Core {i + 1}: {usage}%")


if __name__ == '__main__':
    main()
