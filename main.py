import os
import pathlib

from data_load import DataLoad

DataLoad = DataLoad()

PATH = 'dados'


def import_dataset():
    for dir in os.scandir(PATH):
        if dir.is_dir():
            for file in os.scandir(PATH + "/" + dir.name):
                DataLoad.read_file(file.name, file.path, dir.name, pathlib.Path(file.name).suffix)

    DataLoad.close_conn()


if __name__ == '__main__':
    import_dataset()
