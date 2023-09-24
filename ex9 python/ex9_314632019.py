''' Exercise #9. Python for Engineers.'''

import numpy as np
import imageio.v2
import pandas as pd
from matplotlib.axes import SubplotBase
import matplotlib.pyplot as plt



#########################################
# Question 1 - do not delete this comment
#########################################

def compute_entropy(img):
    im = imageio.imread_v2(img)
    num_of_pixels = im.shape[0] * im.shape[1]
    res = 0
    for i in range(im.min(), im.max() + 1):
        comp = im == i
        count = comp.sum()
        pi = (count/num_of_pixels)
        res += -pi * np.log2(pi)
        count = 0
    return round(res, 4)

#########################################
# Question 2 - do not delete this comment
#########################################

def load_image_as_matrix(img_path):
    im = imageio.imread_v2(img_path)
    return im

def binarize_matrix(mat):
    mask = (mat >= 128)
    new_mask = (mat < 128)
    mat[mask] = 1
    mat[new_mask] = 0
    return mat

def compress_flatten_rle(mat):
    shape = mat.shape
    mat_flatten = mat.flatten()
    def rle(sequence):
        result = []
        current_value = 0
        current_count = 0
        for value in sequence:
            if value == current_value:
                current_count += 1
            else:
                result.append(current_count)
                current_value = value
                current_count = 1
        result.append(current_count)
        return result
    RLE_v = rle(mat_flatten)
    output = (RLE_v, shape)
    return output

def decompress_flatten_rle(mat_rle_compressed, shape):
    def decode_rle(rle_sequence):
        result = []
        i = 0
        for count in rle_sequence:
            if i == 0:
                result.extend([0] * count)
                i = 1
            elif i == 1:
                result.extend([1] * count)
                i = 0
        return result
    original_v = np.array(decode_rle(mat_rle_compressed))
    original_im = original_v.reshape(shape)
    return original_im

def calc_compression_ratio(mat_rle_compressed, mat):
    num_of_pixels = mat.shape[0] * mat.shape[1]
    num_of_int = len(mat_rle_compressed)
    return round(num_of_int/num_of_pixels, 2)


#########################################
# Question 3 - do not delete this comment
#########################################

# A -----------------------------------------------------------------------------
def read_files(travels_file, missions_file):
    travels = pd.read_csv(travels_file)
    missions = pd.read_csv(missions_file)
    return (travels, missions)
# B.1 -----------------------------------------------------------------------------


def merge_tables(df_travels,df_missions):
    return pd.merge(df_travels,df_missions, on="Universe")

# B.2 -----------------------------------------------------------------------------

def scatter_plot(df_merged):
   return df_merged.plot.scatter(x="Bounty" , y="Expenses", c="Blue")


# C -----------------------------------------------------------------------------

def add_gain_per_monster(df_merged):
    df_merged["Gain"] = df_merged["Bounty"] - df_merged["Expenses"]

# D -----------------------------------------------------------------------------


def daily_gain_per_universe(df_merged):
     return (df_merged.groupby(["Universe"])["Bounty"].sum()-df_merged.groupby(["Universe"])["Expenses"].min())/df_merged.groupby(["Universe"])["Duration"].min()

# E -----------------------------------------------------------------------------

def drop_nonprofitable_universes(df_merged):
    original = daily_gain_per_universe(df_merged)
    new = original[original > 0]
    return (df_merged[df_merged["Universe"].isin(new.index)])

# F -----------------------------------------------------------------------------

def mean_duration(df_5):
    return df_5.groupby(["Universe"])["Duration"].mean().mean()

# G -----------------------------------------------------------------------------

def drop_least_daily_lucrative_universe(df_5):
    daily = daily_gain_per_universe(df_5)
    min_prof = daily.min()
    min_uni = daily[daily == min_prof].index[0]
    new = df_5[df_5["Universe"] != min_uni]
    return (min_uni, min_prof, new)


# H ------------------------------ ----------------------------------------------

def drop_least_daily_lucrative_universe_with_teleporting(df_merged):
    df_merged["Duration"] = np.where(df_merged["Teleporting"], df_merged["Duration"] / 2, df_merged["Duration"])
    df_5 = drop_nonprofitable_universes(df_merged)
    df_7 = drop_least_daily_lucrative_universe(df_5)
    return df_7



if __name__ == '__main__':

    print('==== Q1: Write your sanity check/output here!====')
    print(compute_entropy('rick_and_morty_gray.png'))

    print('==== Q2: Basic output====')

    img_original=load_image_as_matrix('blood_ridge_gray.png')
    img=binarize_matrix(img_original)
    mat_rle_compressed, shape=compress_flatten_rle(img)
    mat_rle_decompressed=decompress_flatten_rle(mat_rle_compressed, shape)

    fig, axs= plt.subplots(1, 3, figsize=(30,10))
    axs[0].set_title("original_image")
    axs[0].imshow(img_original,cmap = plt.cm.gray)
    axs[1].set_title("binarized_image")
    axs[1].imshow(img,cmap = plt.cm.gray)
    axs[2].set_title("decompressed_image")
    axs[2].imshow(mat_rle_decompressed,cmap = plt.cm.gray)
    plt.show()

    print(f'Are decompreseed and original matrices identical? {np.all((img==mat_rle_decompressed))}')
    print(f'calc_compression_ratio: {calc_compression_ratio(mat_rle_compressed, img)}')


    img_original=np.array([[0,0,0,0,200,200,0,0,0,0,0,200,200,0,0,0,0],
                [0,0,0,200,200,200,200,0,0,0,200,201,200,200,0,0,0],
                [0,0,200,1,1,1,1,200,0,200,200,200,1,1,200,0,0],
                [0,200,1,100,1,101,1,200,200,1,1,1,1,101,1,200,0],
                [0,200,1,1,1,200,1,1,1,21,1,101,1,150,1,200,0],
                [0,200,1,101,100,1,100,1,10,1,1,100,100,1,1,200,0],
                [0,200,1,200,1,201,1,1,1,1,201,1,1,100,1,200,0],
                [0,200,1,1,1,1,1,21,1,1,1,1,21,1,1,200,0],
                [0,0,200,1,101,1,1,1,250,1,200,1,1,1,200,0,0],
                [0,0,0,200,200,1,200,1,1,1,1,10,1,200,0,0,0],
                [0,0,0,0,200,1,1,1,1,10,1,1,200,0,0,0,0],
                [0,0,0,0,0,170,1,10,1,1,1,200,0,0,0,0,0],
                [0,0,0,0,0,0,230,1,1,1,200,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,200,1,200,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,200,0,0,0,0,0,0,0,0]])

    img=binarize_matrix(img_original)
    mat_rle_compressed, shape=compress_flatten_rle(img)
    mat_rle_decompressed=decompress_flatten_rle(mat_rle_compressed, shape)
    print(f'Are decompreseed and original matrices identical? {np.all((img==mat_rle_decompressed))}')
    print(f'calc_compression_ratio: {calc_compression_ratio(mat_rle_compressed, img)}')

    fig, axs= plt.subplots(1, 3, figsize=(30,10))
    axs[0].set_title("original_image")
    axs[0].imshow(img_original,cmap = plt.cm.gray)
    axs[1].set_title("binarized_image")
    axs[1].imshow(img,cmap = plt.cm.gray)
    axs[2].set_title("decompressed_image")
    axs[2].imshow(mat_rle_decompressed,cmap = plt.cm.gray)
    plt.show()


    print('==== Q3: Basic output====')
    print("===   A   ===")
    df_travels,df_missions=read_files("travels.csv", "missions.csv")
    print("Travels:")
    print(df_travels)
    print("Missions:")
    print(df_missions)

    print("===   B.1   ===")
    df_merged=merge_tables(df_travels,df_missions)
    print(df_merged)

    print("===   B.2   ===")
    ax=scatter_plot(df_merged)
    print("Is correct return type?", isinstance(ax,SubplotBase))
    plt.show()

    print("===   C   ===")
    df_merged_cpy=df_merged.copy()
    add_gain_per_monster(df_merged_cpy)
    print(df_merged_cpy)

    print("===   D   ===")
    daily_gain=daily_gain_per_universe(df_merged)
    print(daily_gain)

    print("===   E   ===")
    df_5=drop_nonprofitable_universes(df_merged)
    print(df_5)

    print("===   F   ===")
    avg=mean_duration(df_5)
    print(avg)

    print("===   G   ===")
    df_7=drop_least_daily_lucrative_universe(df_5)
    print(df_7)

    print("===   H   ===")
    df_8=drop_least_daily_lucrative_universe_with_teleporting(df_merged)
    print(df_8)


