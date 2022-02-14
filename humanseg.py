import os.path

import paddlehub as hub


def seg(filename):
    module = hub.Module(directory="module/deeplabv3p_xception65_humanseg")
    if not os.path.exists('.\cache'):
        os.mkdir('.\cache')
    res = module.segmentation(paths=[filename], output_dir='.\cache', visualization=True)
    outputFilename = res[0]['save_path']
    return outputFilename


if __name__ == '__main__':
    print(seg(filename='img/demo2.jpeg'))
