import pickle
import os
import numpy as np


def save_data(data, file_name='data', path=os.getcwd()):
    output = open(path + '//' + file_name + '.pkl', 'wb')
    pickle.dump(data, output)
    output.close()


def load_data(file_name, path=os.getcwd()):
    pkl_file = open(path + '//' + file_name + '.pkl', 'rb')
    data = pickle.load(pkl_file)
    pkl_file.close()
    return data


class _MethodTest:
    @staticmethod
    def test_save_data():
        save_data(np.random.rand(3, 2), file_name='test_save_data')

    @staticmethod
    def test_load_dat():
        return load_data(file_name='test_save_data')


if __name__ == "__main__":
    np.random.seed(42)
    _MethodTest().test_save_data()
    print(_MethodTest().test_load_dat())
