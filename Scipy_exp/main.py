import scipy as scp
from scipy.sparse import csr_matrix, csc_matrix
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import breadth_first_order

from scipy import io


def main():
    # constants
    # print(dir(scp.constants))
    # print(vars(scp.constants))

    # csr
    csr_arr = np.array([0, 0, 1, 0, 0, 0, 0, 1])
    print(f'csc_matrix(csc_arr) is  : \n{csc_matrix(csr_arr)}\n')

    # csc
    csc_arr = np.array([[0],
                        [1],
                        [0],
                        [0],
                        [0],
                        [0],
                        ])
    print(f'csc_matrix(csc_arr) is  : \n{csc_matrix(csc_arr)}\n')

    # 获取对应矩阵
    cm_arr = np.array([[1, 0, 6, 0, 7],
                       [0, 2, 0, 0, 0],
                       [0, 0, 3, 0, 0],
                       [0, 0, 0, 4, 0],
                       [0, 0, 0, 0, 5],
                       ])
    print(f'csr_matrix(cm_arr) is  : \n{csr_matrix(cm_arr)}\n')
    print(f'csc_matrix(cm_arr) is  : \n{csc_matrix(cm_arr)}\n')

    # 获取非0元素
    print(f'csc_matrix(cm_arr).data is  : \n{csc_matrix(cm_arr).data}\n')
    print(f'csr_matrix(cm_arr).data is  : \n{csr_matrix(cm_arr).data}\n')

    # 获取非0元素个数
    print(f'csr_matrix(cm_arr).count_nonzero() is  : \n{csr_matrix(cm_arr).count_nonzero()}\n')
    print(f'csc_matrix(cm_arr).count_nonzero() is  : \n{csc_matrix(cm_arr).count_nonzero()}\n')

    # 减少对应矩阵的0数目
    c_m = csc_matrix(cm_arr)
    c_m.eliminate_zeros()
    r_m = csr_matrix(cm_arr)
    r_m.eliminate_zeros()
    print(f'csc_matrix(cm_arr).eliminate_zeros() is  : \n{c_m}\n')
    print(f'csr_matrix(cm_arr).eliminate_zeros() is  : \n{r_m}\n')

    row = [0, 0, 0, 1, 1, 1, 2, 2, 2]  # 行指标
    col = [0, 1, 2, 0, 1, 2, 0, 1, 2]  # 列指标
    data = [1, 0, 1, 0, 1, 1, 1, 1, 0]  # 在行指标列指标下的数字
    team = csr_matrix((data, (row, col)), shape=(3, 3))

    print(f'team is : \n{team}\n')
    print(f'team type is : \n{type(team)}\n')
    print(f'team.shape is : \n{team.shape}\n')

    team.eliminate_zeros()
    print(f'team.eliminate_zeros is : \n{team}\n')

    # csr 2 csc
    print(f'csr_matrix is  : \n{r_m}\n')
    print(f'c_m.tocsr() is  : \n{c_m.tocsr()}\n')

    # graph part
    # 构建了一个正方形的图
    arr = np.array([
        [0, 2, 0, 1],
        [2, 0, 3, 0],
        [0, 3, 0, 4],
        [1, 0, 4, 0],
    ])
    graph = csr_matrix(arr)
    print(f'graph is  : \n{graph}\n')

    # 检测连通区域
    # 计算连通分量
    n_components, labels = connected_components(graph, directed=False, connection='weak', return_labels=True)
    print("连通分量数量:", n_components)
    print("节点标签:", labels)

    # dijkstra
    print(f'dijkstra seq is : \n{dijkstra(graph, indices=0)}\n')

    # Floyd warshall
    print(f'floyd_warshall matrix is : \n{floyd_warshall(graph)}\n')

    # bellman ford
    print(f'bellman_ford matrix is : \n{bellman_ford(graph, indices=0)}\n')

    # depth first order
    print(f'depth_first_order seq is : \n{depth_first_order(graph, 0)}\n')

    # breadth first order
    print(f'breadth_first_order seq is : \n{breadth_first_order(graph, 0)}\n')

    # matlab part
    # 导出matlab 数据 等等
    matlab_output = io.savemat('filename.mat', {'data': arr})
    print(f'matlab_output is \n {matlab_output} \n')

    # 读取 matlab 数据 等等
    matlab_intput = io.loadmat('filename.mat')
    print(f'matlab_input is \n{matlab_intput}\n')
    matlab_intput_data = matlab_intput['data']
    print(f'matlab_input \'s data is \n{matlab_intput_data}\n')
    # 避免外围信息
    matlab_intput_without = io.loadmat('filename.mat', squeeze_me=True)
    print(f'matlab_intput_without is \n{matlab_intput_without}\n')
    matlab_intput_data_without = matlab_intput_without['data']
    print(f'matlab_intput_data_without \'s data is \n{matlab_intput_data_without}\n')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
