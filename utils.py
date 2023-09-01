import imageio
import numpy as np
import tifffile as tf

from PIL import Image
from tqdm import tqdm


from pycine.file import read_header
from pycine.raw import read_frames
from pycine.color import color_pipeline

def get_frame_gray(input_file, frame):
    with open(input_file, 'rb') as f:
        raw_images, setup, bpp = read_frames(input_file, start_frame=frame, count=1)
        rgb_images = [color_pipeline(raw_image, setup=setup, bpp=bpp) for raw_image in raw_images]

        image = np.uint8(rgb_images[0] * 255)

        img = Image.fromarray(image)
        gray_img = img.convert("L")
        return gray_img
    
def save_as_tif(input_file, output_file):
    header = read_header(cine_file=input_file)
    frame_count = header["cinefileheader"].ImageCount

    imgs = []
    for i in tqdm(range(frame_count)):
        imgs.append(get_frame_gray(input_file=input_file, frame=i+1))

    # # # Works better with large files but the images lose information
    # f = len(imgs)
    # m, n = imgs[0].size
    # factor = 2.0
    # data = np.zeros((f, m, n), dtype=np.uint8)
    # breakpoint()
    # # exec("for i in tqdm(range(f)): data[i,:,:] = np.clip(np.asarray(imgs[i]) * factor, 0, 255).astype(np.uint8)")
    # for i in tqdm(range(f)):
    #     data[i,:,:] = np.asarray(imgs[i])
    # tf.imwrite(out, data)
    
    with tf.TiffWriter(output_file, bigtiff=True) as tiff_writer:
        for im in imgs:
            tiff_writer.save(im, photometric=tf.PHOTOMETRIC.MINISBLACK)


def save_as_mp4(input_file, output_file, fps):
    header = read_header(cine_file=input_file)
    frame_count = header["cinefileheader"].ImageCount

    imgs = []
    for i in tqdm(range(frame_count)):
        imgs.append(np.asarray(get_frame_gray(input_file=input_file, frame=i+1)))

    imageio.mimwrite(output_file, imgs, fps=fps)