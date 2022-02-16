from os.path import exists
from os import mkdir
from paddlehub import Module


def seg(filename):
    module = Module(directory="module/deeplabv3p_xception65_humanseg")
    if not exists('../cache'):
        mkdir('../cache')
    res = module.segmentation(paths=[filename], output_dir='../cache', visualization=True)
    outputFilename = res[0]['save_path']
    return outputFilename


if __name__ == '__main__':
    print(seg(filename='../img/demo.jpeg'))
