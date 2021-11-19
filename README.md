# ByteTrack-ONNX-Sample
[ByteTrack(Multi-Object Tracking by Associating Every Detection Box)](https://github.com/ifzhang/ByteTrack)のPythonでのONNX推論サンプルです。<br>
ONNXに変換したモデルも同梱しています。<br>
変換自体を試したい方は[ByteTrack_Convert2ONNX.ipynb](ByteTrack_Convert2ONNX.ipynb)を使用ください。<br>
[ByteTrack_Convert2ONNX.ipynb](ByteTrack_Convert2ONNX.ipynb)はColaboratory上での実行を想定しています。

<!-- 動画が小さい -->
https://user-images.githubusercontent.com/37477845/142471970-2d56c7c4-e4f3-440a-9d5f-e0d0436e01c4.mp4

# Requirement 
opencv-python 4.5.3.56 or later<br>
onnx 1.9.0 or later<br>
onnxruntime-gpu 1.9.0 or later<br>
Cython 0.29.24 or later<br>
torch 1.8.1 or later<br>
torchvision 0.9.1 or later<br>
pycocotools 2.0.2 or later<br>
scipy 1.6.3 or later<br>
loguru 0.5.3 or later<br>
thop 0.0.31.post2005241907 or later<br>
lap 0.4.0 or later<br>
cython_bbox 0.1.3 or later<br>
<br>
※onnxruntime-gpuはonnxruntimeでも動作しますが、推論時間がかかるためGPUを推奨します<br>
※Windowsでcython_bbox のインストールが失敗する場合は、GitHubからのインストールをお試しください(2021/11/19時点)<br>
`pip install -e git+https://github.com/samson-wang/cython_bbox.git#egg=cython-bbox`

# Demo
デモの実行方法は以下です。
#### 動画
```bash
python demo_video_onnx.py
```
<details>
<summary>実行時オプション</summary>


</details>

* --device<br>
カメラデバイス番号の指定<br>
デフォルト：0
* --movie<br>
動画ファイルの指定 ※指定時はカメラデバイスより優先<br>
デフォルト：指定なし
* --image<br>
画像ファイルの指定 ※指定時はカメラデバイスや動画より優先<br>
デフォルト：指定なし
* --width<br>
カメラキャプチャ時の横幅<br>
デフォルト：960
* --height<br>
カメラキャプチャ時の縦幅<br>
デフォルト：540
* --model<br>
ロードするモデルの格納パス<br>
デフォルト：model/nanodet_m_320.onnx
* --input_shape<br>
モデルの入力サイズ<br>
デフォルト：320
* --score_th<br>
クラス判別の閾値<br>
デフォルト：0.35
* --nms_th<br>
NMSの閾値<br>
デフォルト：0.6

#### Webカメラ
```bash
python demo_webcam_onnx.py
```

# Reference
* [ifzhang/ByteTrack](https://github.com/ifzhang/ByteTrack)

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
ByteTrack-ONNX-Sample is under [MIT License](LICENSE).

# License(Movie)
サンプル動画は[NHKクリエイティブ・ライブラリー](https://www.nhk.or.jp/archives/creative/)の[イギリス ウースターのエルガー像](https://www2.nhk.or.jp/archives/creative/material/view.cgi?m=D0002011239_00000)を使用しています。
