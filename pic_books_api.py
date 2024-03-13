import os, sys
import requests

from flask import Flask, request, make_response, send_file, \
                         render_template, jsonify, Response
from src.configs.api_config import app_config
from PIL import Image
from io import BytesIO

_app = Flask(__name__)

## 配置api相关参数及变量
app = app_config(_app)

@app.route('/')
def index():
    return make_response(render_template('index.html'))

@app.route("/data/cover_pic/<level>/<imgName>.jpg")
def get_cover_frame(level, imgName):
    # 获取图片保存的路径
    imgs_dir = os.path.join(app.config['LOAD_ROOT_COVER'], level)
    img_path = os.path.join(imgs_dir, imgName)
    with open(r'./{}.jpg'.format(img_path), 'rb') as f:
        image = f.read()
        resp = Response(image, mimetype="image/jpg")
        return resp

@app.route("/data/page_pic/<level>/<word>/<imgName>.jpg")
def get_page_frame(level, word, imgName):
    # 获取图片保存的路径
    imgs_dir = os.path.join(app.config['LOAD_ROOT_BOOKS'], level, word, "page_imgs")
    img_path = os.path.join(imgs_dir, imgName)
    with open(r'./{}.jpg'.format(img_path), 'rb') as f:
        image = f.read()
        resp = Response(image, mimetype="image/jpg")
        return resp

@app.route("/data/page_audio/<level>/<word>/<audioName>")
def get_page_audio(level, word, audioName):
    # 获取音频保存的路径
    audios_dir = os.path.join(app.config['LOAD_ROOT_BOOKS'], level, word, "page_audios")
    audio_path = os.path.join(audios_dir, audioName)

    audio_file = open(audio_path, 'rb')
    return send_file(audio_file, mimetype="audio/mpeg")
    
    # with open(r'./{}.mp3'.format(audio_path), 'rb') as fmp3:
    #     audio = fmp3.read()
    #     resp = Response(audio, mimetype="audio/mpeg")

    
################################################################################
### -- 绘本封面图像数据获取接口
### ----------------------------------------------------------------------------
@app.route('/api/data/get_cover/', methods=['POST', 'GET'])
def get_cover():
    if request.method == 'POST':
        # level_name = request.json.get('level')
        level_name = request.args.get('level')
        # img_index  = int(request.json.get('id'))
        # print('--level_name: ', level_name)

        ## cover_image
        cover_dir = os.path.join(app.config['LOAD_ROOT_COVER'], level_name)
        cover_imgs = os.listdir(cover_dir)
        cover_url = os.path.join(app.config['COVER_URL'], level_name)
        final_cover_urls = []
        for img_name in cover_imgs:
            final_cover_urls.append(os.path.join(cover_url, img_name))

        pic_data = {
            "img_name": cover_imgs,
            "img_url": final_cover_urls
        }

        return jsonify(pic_data)

################################################################################
### -- 绘本内容图像数据获取接口
### ----------------------------------------------------------------------------
@app.route('/api/data/get_book/', methods=['POST', 'GET'])
def get_books():
    if request.method == 'POST':
        # level_name = request.json.get('level')
        # word_name  = request.json.get('word')
        level_name = request.args.get('level')
        word_name  = request.args.get('word')
        # img_index  = int(request.json.get('id'))
        # img_index  = int(img_index)

        book_dir  = os.path.join(app.config['LOAD_ROOT_BOOKS'], level_name, word_name, 'page_imgs')
        audio_dir = os.path.join(app.config['LOAD_ROOT_BOOKS'], level_name, word_name, 'page_audios')

        page_imgs = os.listdir(book_dir)
        page_audios = os.listdir(audio_dir)

        page_url  = os.path.join(app.config['PAGE_URL'], level_name, word_name)
        audio_url = os.path.join(app.config['AUDIO_URL'], level_name, word_name)
        
        final_page_urls =[]
        for page_name in page_imgs:
            final_page_urls.append(os.path.join(page_url, page_name))
        
        final_audio_urls = []
        for audio_name in page_audios:
            final_audio_urls.append(os.path.join(audio_url, audio_name))

        page_data = {
            "page_name": page_imgs,
            "audio_name": page_audios,
            # "img_id": img_index,     #  图像对应id，唯一， 可通过对应表实现
            "page_url": final_page_urls,   # list
            "audio_url": final_audio_urls,
        }

        return jsonify(page_data)

@app.route('/api/data/get_level/', methods=['POST', 'GET'])
def get_level():
    if request.method == 'POST':
        lever_names = os.listdir(app.config['LOAD_ROOT_COVER'])

        pic_data = {
            "lever_name": lever_names,
        }

        return jsonify(pic_data)


# 1.新增获层级名list接口，返回给前端 key-value[list]，对应所有层级名
# 2.获取封面接口。返回给前端 key-value[list]，对应每个层级下的所有图片名    
# 3.获取书的每页图片和对应音频list接口，传入层接名称A，AA，返回json 字典，key-value[list]，分别为图片url列表[]和音频url列表[]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug=True)
    # app.run(debug=True)