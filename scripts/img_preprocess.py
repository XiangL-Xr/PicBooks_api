import os
import re
import shutil
from PIL import Image


def img_crop(img):
    img_new = img.crop((0, 0, img.size[0], (img.size[1] - 10)))
    return img_new

def img_copy(src_path, dst_path):
    shutil.copy(src_path, dst_path)

root_dir = "./data/books/preprocessed"
cover_dir = "./load/cover_imgs"
# pages_dir = "./load/book_pages"
# audio_dir = "./load/book_audios"
# saved_dir = "./load"
books_dir = "./load/books"

if not os.path.exists(cover_dir):
    os.makedirs(cover_dir, exist_ok=True)
# if not os.path.exists(pages_dir):
#     os.makedirs(pages_dir, exist_ok=True)
# if not os.path.exists(audio_dir):
#     os.makedirs(audio_dir, exist_ok=True)
if not os.path.exists(books_dir):
    os.makedirs(books_dir, exist_ok=True)

index = 0
for level in os.listdir(root_dir):
    level_dir = os.path.join(root_dir, level)
    for word in os.listdir(level_dir):
        re_word = word.replace(" ", "_")
        cover_save_dir = os.path.join(cover_dir, level)
        pages_save_dir = os.path.join(books_dir, level, re_word, 'page_imgs')
        audio_save_dir = os.path.join(books_dir, level, re_word, 'page_audios')
        save_dirs = [cover_save_dir, pages_save_dir, audio_save_dir]
        for dir_ in save_dirs:
            if not os.path.isdir(dir_):
                os.makedirs(dir_, exist_ok=True)
        
        img_path = os.path.join(root_dir, level, word, 'page-1.jpg')
        img = Image.open(img_path).convert('RGB')
        w, h = img.size[0], img.size[1]
        if w > h:
            new_img = img_crop(img)
        else:
            new_img = img
        
        index += 1
        print(f'--> level: {level}, word: {word}, index: {index}')
        new_img.save(os.path.join(cover_save_dir, f'{re_word}.jpg'))

        ## save pages and audios
        pages_dir = os.path.join(level_dir, word)
        old_page_idx = 0
        new_page_idx = 0
        audio_idx = 0
        img_count = 0
        for p in os.listdir(pages_dir):
            if p.endswith(".jpg"):
                img_count += 1
        for name in os.listdir(pages_dir):
            if name.endswith(".jpg"):
                old_page_idx += 1
                if old_page_idx < 2 or old_page_idx == img_count:
                    continue
                else:
                    new_page_idx += 1
                    cur_page_path = os.path.join(pages_dir, f"page-{old_page_idx}.jpg")
                    if not os.path.exists(cur_page_path):
                        continue
                    dst_page_path = os.path.join(pages_save_dir, f"{new_page_idx}.jpg") 
                    img_copy(cur_page_path, dst_page_path)
            elif name.endswith(".mp3"):
                pattern = r'\d+'
                audio_idx += 1
                if "title" in name.split('_'):
                    src_path = os.path.join(pages_dir, name)
                    dst_path = os.path.join(audio_save_dir, "1.mp3")
                    img_copy(src_path, dst_path)
                
                # print('-------------')
                # print(f'p{audio_idx+2}')
                # print(name.split('_'))
                else:
                    p_obj = name.split('_')[-2]
                    # print('--p obj: ', p_obj)
                    p_idx = re.findall(pattern, p_obj)[0]
                    # print('p_idx', p_idx)

                    cur_audio_path = os.path.join(pages_dir, name)
                    dst_audio_path = os.path.join(audio_save_dir, f"{int(p_idx)-1}.mp3")
                    img_copy(cur_audio_path, dst_audio_path)
                # if f"p{audio_idx+2}" in name.split('_'):
                #     cur_audio_path = os.path.join(pages_dir, name)
                #     dst_audio_path = os.path.join(audio_save_dir, f"{audio_idx}.mp3")
                #     img_copy(cur_audio_path, dst_audio_path)
            else:
                continue
        