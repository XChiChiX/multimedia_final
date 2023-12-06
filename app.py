from flask import Flask, request, send_file
from flask import render_template
import os

import Image_processing

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/img.png')
def get_image():
    img_path = os.path.join(os.getcwd(), "gojo.jpg")
    return send_file(img_path, mimetype='image/jpeg')

@app.route('/merge.png')
def get_mergeImage():
    img_path = os.path.join(os.getcwd(), "merge.png")
    return send_file(img_path, mimetype='image/jpeg')

@app.route('/api/upload', methods=['POST'])
def upload_file():
    uploaded_img1 = request.files['img1']
    uploaded_img2 = request.files['img2']

    if uploaded_img1 and uploaded_img2:
        # 指定儲存路徑
        save_path = os.getcwd()
        print(save_path)

        img1_path = os.path.join(save_path, uploaded_img1.filename)
        img2_path = os.path.join(save_path, uploaded_img2.filename)
        print("48763 ", img1_path)

        # 儲存檔案
        uploaded_img1.save(uploaded_img1.filename)
        uploaded_img2.save(uploaded_img2.filename)

        Image_processing.start(img1_path, img2_path)
        
        os.remove(img1_path)
        os.remove(img2_path)

        return {'message': '上傳成功', 'img1_path': img1_path, 'img2_path': img2_path}
    else:
        return {'message': '未選擇檔案'}
    
@app.route('/api/download', methods=['POST'])
def download():
    fileName = "merge.png"
    file_path = os.path.join(os.getcwd(), fileName)

    # 返回文件
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.debug = True
    app.run()

