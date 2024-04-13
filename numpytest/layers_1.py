# coding=utf-8
import numpy as np
import time


class FullyConnectedLayer(object):
    def __init__(self, num_input, num_output):  # 全连接层初始化
        self.num_input = num_input
        self.num_output = num_output
        self.mul_count = 0
        self.add_count = 0
        print('\tFully connected layer with input %d, output %d.' % (self.num_input, self.num_output))

    def init_param(self, std=0.01):  # 参数初始化
        self.weight = np.random.normal(loc=0.0, scale=std, size=(self.num_input, self.num_output))
        self.bias = np.zeros([1, self.num_output])
        print('self.bias.shape init_param is :')
        print(self.bias.shape)

    def forward(self, input):  # 前向传播计算
        start_time = time.time()
        self.input = input
        # TODO：全连接层的前向传播，计算输出结果
        # print('self.bias.shape forward1 is :')
        # print(self.bias.shape)
        self.output = np.dot(self.input, self.weight) + self.bias

        self.mul_count += self.input.shape[1] * self.weight.shape[0] * self.input.shape[0] * self.weight.shape[1]
        self.add_count += (self.input.shape[1] * self.weight.shape[0] - 1) * (
                    self.input.shape[0] * self.weight.shape[1])
        print('FullyConnectedLayer mul_count is :')
        print(self.mul_count)
        print('FullyConnectedLayer add_count is :')
        print(self.add_count)
        # print('self.bias.shape forward2 is :')
        # print(self.bias.shape)
        return self.output

    def backward(self, top_diff):  # 反向传播的计算
        # TODO：全连接层的反向传播，计算参数梯度和本层损失
        # print('top_diff.shape')
        # print(top_diff.shape)
        # print(self.input.T.shape)
        self.d_weight = np.dot((self.input.T), (top_diff))
        self.d_bias = np.mean(top_diff, axis=0, keepdims=True)
        # print('self.d_bias')
        # print(self.d_bias.shape)
        bottom_diff = np.dot(top_diff, self.weight.T)
        return bottom_diff

    def update_param(self, lr):  # 参数更新
        # TODO：对全连接层参数利用参数进行更新
        # print(self.weight.shape)
        # print(self.d_weight.shape)
        self.weight = self.weight - self.d_weight * lr
        # print('self.bias.shape update_param is :')
        # print(self.bias.shape)
        self.bias = self.bias - self.d_bias
        # print('self.bias.shape update_param is :')
        # print(self.bias.shape)

    def load_param(self, weight, bias):  # 参数加载
        assert self.weight.shape == weight.shape
        # print('self.bias.shape')
        # print(self.bias.shape)
        # print('bias.shape')
        # print(bias.shape)
        assert self.bias.shape == bias.shape
        self.weight = weight
        self.bias = bias

    def save_param(self):  # 参数保存
        return self.weight, self.bias


class ReLULayer(object):
    def __init__(self):
        print('\tReLU layer.')

    def forward(self, input):  # 前向传播的计算
        start_time = time.time()
        self.input = input
        # TODO：ReLU层的前向传播，计算输出结果
        output = np.maximum(self.input, 0)
        return output

    def backward(self, top_diff):  # 反向传播的计算
        # TODO：ReLU层的反向传播，计算本层损失
        rows, cols = self.input.shape
        bottom_diff = np.zeros((rows, cols))
        for x in range(rows):
            for y in range(cols):
                bottom_diff[x, y] = top_diff[x, y] if self.input[x, y] > 0 else 0
        # bottom_diff = top_diff[mask]*0.01
        return bottom_diff


class SoftmaxLossLayer(object):
    def __init__(self):
        print('\tSoftmax loss layer.')

    def forward(self, input):  # 前向传播的计算
        # TODO：softmax 损失层的前向传播，计算输出结果
        input_max = np.max(input, axis=1, keepdims=True)
        input_exp = np.exp(input - input_max)
        sum = np.sum(input_exp, axis=1, keepdims=True)
        self.prob = input_exp / sum
        return self.prob

    def get_loss(self, label):  # 计算损失
        self.batch_size = self.prob.shape[0]
        self.label_onehot = np.zeros_like(self.prob)
        self.label_onehot[np.arange(self.batch_size), label] = 1.0
        loss = -np.sum(np.log(self.prob) * self.label_onehot) / self.batch_size
        return loss

    def backward(self):  # 反向传播的计算
        # TODO：softmax 损失层的反向传播，计算本层损失
        bottom_diff = (self.prob - self.label_onehot) / self.batch_size
        return bottom_diff
