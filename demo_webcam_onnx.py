import os
import copy
import time
import argparse

import cv2

from byte_tracker.byte_tracker_onnx import ByteTrackerONNX


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--model',
        type=str,
        default='byte_tracker/model/bytetrack_s.onnx',
    )
    parser.add_argument('--device', type=int, default=0)
    parser.add_argument("--width", help='cap width', type=int, default=960)
    parser.add_argument("--height", help='cap height', type=int, default=540)
    parser.add_argument(
        '--score_th',
        type=float,
        default=0.1,
    )
    parser.add_argument(
        '--nms_th',
        type=float,
        default=0.7,
    )
    parser.add_argument(
        '--input_shape',
        type=str,
        default='608,1088',
    )
    parser.add_argument(
        '--with_p6',
        action='store_true',
        help='Whether your model uses p6 in FPN/PAN.',
    )

    # tracking args
    parser.add_argument(
        '--track_thresh',
        type=float,
        default=0.5,
        help='tracking confidence threshold',
    )
    parser.add_argument(
        '--track_buffer',
        type=int,
        default=30,
        help='the frames for keep lost tracks',
    )
    parser.add_argument(
        '--match_thresh',
        type=float,
        default=0.8,
        help='matching threshold for tracking',
    )
    parser.add_argument(
        '--min-box-area',
        type=float,
        default=10,
        help='filter out tiny boxes',
    )
    parser.add_argument(
        '--mot20',
        dest='mot20',
        default=False,
        action='store_true',
        help='test mot20.',
    )

    args = parser.parse_args()

    return args


def main():
    # 引数取得
    args = get_args()

    cap_device = args.device
    cap_width = args.width
    cap_height = args.height

    # ByteTrackerインスタンス生成
    byte_tracker = ByteTrackerONNX(args)

    # カメラ準備
    cap = cv2.VideoCapture(cap_device)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, cap_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cap_height)

    frame_id = 1

    while True:
        start_time = time.time()

        # フレーム読み出し
        ret, frame = cap.read()
        if not ret:
            break
        debug_image = copy.deepcopy(frame)

        # Byte Tracker推論
        _, bboxes, ids, scores = byte_tracker.inference(frame)

        elapsed_time = time.time() - start_time

        # 検出情報描画
        debug_image = draw_tracking_info(
            debug_image,
            bboxes,
            ids,
            scores,
            frame_id,
            elapsed_time,
        )

        # キー処理(ESC：終了)
        key = cv2.waitKey(1)
        if key == 27:  # ESC
            break

        # 画面反映
        cv2.imshow('ByteTrack ONNX Sample', debug_image)

        frame_id += 1

    cap.release()
    cv2.destroyAllWindows()


def get_id_color(index):
    temp_index = abs(int(index)) * 3
    color = ((37 * temp_index) % 255, (17 * temp_index) % 255,
             (29 * temp_index) % 255)
    return color


def draw_tracking_info(
    image,
    tlwhs,
    ids,
    scores,
    frame_id=0,
    elapsed_time=0.,
):
    text_scale = 1.5
    text_thickness = 2
    line_thickness = 2

    # フレーム数、処理時間、推論時間
    text = 'frame: %d ' % (frame_id)
    text += 'elapsed time: %.0fms ' % (elapsed_time * 1000)
    text += 'num: %d' % (len(tlwhs))
    cv2.putText(
        image,
        text,
        (0, int(15 * text_scale)),
        cv2.FONT_HERSHEY_PLAIN,
        2,
        (0, 0, 255),
        thickness=text_thickness,
    )

    for index, tlwh in enumerate(tlwhs):
        x1, y1 = int(tlwh[0]), int(tlwh[1])
        x2, y2 = x1 + int(tlwh[2]), y1 + int(tlwh[3])

        # バウンディングボックス
        color = get_id_color(ids[index])
        cv2.rectangle(image, (x1, y1), (x2, y2), color, line_thickness)

        # ID、スコア
        # text = str(ids[index]) + ':%.2f' % (scores[index])
        text = str(ids[index])
        cv2.putText(image, text, (x1, y1 - 5), cv2.FONT_HERSHEY_PLAIN,
                    text_scale, (0, 0, 0), text_thickness + 3)
        cv2.putText(image, text, (x1, y1 - 5), cv2.FONT_HERSHEY_PLAIN,
                    text_scale, (255, 255, 255), text_thickness)
    return image


if __name__ == '__main__':
    main()
