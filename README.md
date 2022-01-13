# ByteTrack-ONNX-Sample
[ByteTrack(Multi-Object Tracking by Associating Every Detection Box)](https://github.com/ifzhang/ByteTrack)のPythonでのONNX推論サンプルです。<br>
ONNXに変換したモデルも同梱しています。<br>
変換自体を試したい方は[ByteTrack_Convert2ONNX.ipynb](ByteTrack_Convert2ONNX.ipynb)を使用ください。<br>
[ByteTrack_Convert2ONNX.ipynb](ByteTrack_Convert2ONNX.ipynb)はColaboratory上での実行を想定しています。<br>
以下の動画はWindowsでの実行例です。

https://user-images.githubusercontent.com/37477845/142617492-7fef3f6e-5725-480c-b059-0f2dee1606bc.mp4

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
#### 動画：動画に対しByteTrackで追跡した結果を動画出力します
```bash
python demo_video_onnx.py
```
<details>
<summary>実行時オプション</summary>

* --use_debug_window<br>
動画書き込み時に書き込みフレームをGUI表示するか否か<br>
デフォルト：指定なし
* --model<br>
ByteTrackのONNXモデル格納パス<br>
デフォルト：byte_tracker/model/bytetrack_s.onnx
* --video<br>
入力動画の格納パス<br>
デフォルト：sample.mp4
* --output_dir<br>
動画出力パス<br>
デフォルト：output
* --score_th<br>
人検出のスコア閾値<br>
デフォルト：0.1
* --score_th<br>
人検出のNMS閾値<br>
デフォルト：0.7
* --input_shape<br>
推論時入力サイズ<br>
デフォルト：608,1088
* --with_p6<br>
YOLOXモデルのFPN/PANでp6を含むか否か<br>
デフォルト：指定なし
* --track_thresh<br>
追跡時のスコア閾値<br>
デフォルト：0.5
* --track_buffer<br>
見失い時に何フレームの間、追跡対象を保持するか<br>
デフォルト：30
* --match_thresh<br>
追跡時のマッチングスコア閾値<br>
デフォルト：0.8
* --min-box-area<br>
最小のバウンディングボックスのサイズ閾値<br>
デフォルト：10
* --mot20<br>
MOT20を使用しているか否か<br>
デフォルト：指定なし
</details>

#### Webカメラ：Webカメラ画像に対しByteTrackで追跡した結果をGUI表示します
```bash
python demo_webcam_onnx.py
```
<details>
<summary>実行時オプション</summary>

* --model<br>
ByteTrackのONNXモデル格納パス<br>
デフォルト：byte_tracker/model/bytetrack_s.onnx
* --device<br>
カメラデバイス番号の指定<br>
デフォルト：0
* --width<br>
カメラキャプチャ時の横幅<br>
デフォルト：960
* --height<br>
カメラキャプチャ時の縦幅<br>
デフォルト：540
* --score_th<br>
人検出のスコア閾値<br>
デフォルト：0.1
* --score_th<br>
人検出のNMS閾値<br>
デフォルト：0.7
* --input_shape<br>
推論時入力サイズ<br>
デフォルト：608,1088
* --with_p6<br>
YOLOXモデルのFPN/PANでp6を含むか否か<br>
デフォルト：指定なし
* --track_thresh<br>
追跡時のスコア閾値<br>
デフォルト：0.5
* --track_buffer<br>
見失い時に何フレームの間、追跡対象を保持するか<br>
デフォルト：30
* --match_thresh<br>
追跡時のマッチングスコア閾値<br>
デフォルト：0.8
* --min-box-area<br>
最小のバウンディングボックスのサイズ閾値<br>
デフォルト：10
* --mot20<br>
MOT20を使用しているか否か<br>
デフォルト：指定なし
</details>

# Reference
* [ifzhang/ByteTrack](https://github.com/ifzhang/ByteTrack)

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
ByteTrack-ONNX-Sample is under [MIT License](LICENSE).

# License(Movie)
サンプル動画は[NHKクリエイティブ・ライブラリー](https://www.nhk.or.jp/archives/creative/)の[イギリス ウースターのエルガー像](https://www2.nhk.or.jp/archives/creative/material/view.cgi?m=D0002011239_00000)を使用しています。
