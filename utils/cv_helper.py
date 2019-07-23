from configuration.config import LoadConfig
from matplotlib import pyplot as plt
import numpy as np
import cv2
import os


class CVHelper:
    # FLANN（Fast_Library_for_Approximate_Nearest_Neighbors)
    # KNN (K-Nearest Neighbor)
    # limit opencv version because of patent https://github.com/skvark/opencv-python/issues/126

    @classmethod
    def sift_show_points_matched(cls, target, source="screenshot.png"):
        base_path = os.path.join(os.getcwd(), "projects", LoadConfig.load_config()["project"], "test_data")
        img_target = cv2.imread(os.path.join(base_path, target), 0)
        img_source = cv2.imread(os.path.join(base_path, source), 0)
        print('target image size: height, width: {}, {}'.format(img_target.shape[0], img_target.shape[1]))
        print('source image size: height, width: {}, {}'.format(img_source.shape[0], img_source.shape[1]))

        sift = cv2.xfeatures2d.SIFT_create()
        kp1, des1 = sift.detectAndCompute(img_target, None)
        kp2, des2 = sift.detectAndCompute(img_source, None)

        bf = cv2.BFMatcher()
        points = []
        matches = bf.knnMatch(des1, des2, k=2)
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                points.append([m])
        img_result = cv2.drawMatchesKnn(img_target, kp1, img_source, kp2, points, None, flags=2)
        plt.imshow(img_result)
        plt.show()

    @classmethod
    def flann_generate_matched_points_center(cls, target, source="screenshot.png"):
        base_path = os.path.join(os.getcwd(), "projects", LoadConfig.load_config()["project"], "test_data")
        img_target = cv2.imread(os.path.join(base_path, target), 0)
        img_source = cv2.imread(os.path.join(base_path, source), 0)
        print('target image size: height, width: {}, {}'.format(img_target.shape[0], img_target.shape[1]))
        print('source image size: height, width: {}, {}'.format(img_source.shape[0], img_source.shape[1]))

        sift = cv2.xfeatures2d.SIFT_create()
        kp1, des1 = sift.detectAndCompute(img_target, None)
        kp2, des2 = sift.detectAndCompute(img_source, None)
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(des1, des2, k=2)

        points = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                points.append(m)
        h1, w1 = img_target.shape[:2]
        h2, w2 = img_source.shape[:2]
        view = np.zeros((max(h1, h2), w1 + w2, 3), np.uint8)
        view[:h1, :w1, 0] = img_target
        view[:h2, w1:, 0] = img_source
        view[:, :, 1] = view[:, :, 0]
        view[:, :, 2] = view[:, :, 0]

        coordinate_x = []
        coordinate_y = []
        for p in points:
            coordinate_x.append(int(kp2[p.trainIdx].pt[0]))
            coordinate_y.append(int(kp2[p.trainIdx].pt[1]))
        scale_x = round(sum(coordinate_x) / len(points) / img_source.shape[1], 2)
        scale_y = round(sum(coordinate_y) / len(points) / img_source.shape[0], 2)
        return scale_x, scale_y
        # temp = []
        # for m, n in matches:
        #     if m.distance < 0.6 * n.distance:
        #         temp.append(m)
        # src_pts = np.float32([kp1[m.queryIdx].pt for m in temp]).reshape(-1, 1, 2)
        # dst_pts = np.float32([kp2[m.trainIdx].pt for m in temp]).reshape(-1, 1, 2)
        # M, mask = cv2.findHomography(src_pts, dst_pts, cv2.LMEDS, 5.0)
        # matches_mask = mask.ravel().tolist()
        #
        # h, w = img_target.shape
        # pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        #
        # dst = cv2.perspectiveTransform(pts, M)
        # img_source_new = cv2.polylines(img_source, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
        #
        # area = [np.int32(dst)]
        #
        # # compute object center coordinate in the search image
        # x = (area[0][2][0][0] - area[0][0][0][0]) / 2 + area[0][0][0][0]
        # y = (area[0][1][0][1] - area[0][0][0][1]) / 2 + area[0][0][0][1]
        # return x, y