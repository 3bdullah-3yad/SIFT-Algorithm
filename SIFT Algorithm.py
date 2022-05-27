def imshow(name, img):   
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


import cv2
path = r'D:\Projects\Computer Vision\SIFT Algorithm\egypt-pyramids.jpg'
img = cv2.imread(path, 0)

sift = cv2.SIFT_create()

keypoints = sift.detect(img)

sifted_img = cv2.drawKeypoints(img, keypoints, None)

imshow("img with KPs", sifted_img)
cv2.imwrite(r"D:\Projects\Computer Vision\SIFT Algorithm\sifted_img.jpg", sifted_img)




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
sifted_img2 = cv2.drawKeypoints(img, keypoints, sifted_img, flags=flags)

imshow("img with KPs and flags", sifted_img2)

cv2.imwrite(r"D:\Projects\Computer Vision\SIFT Algorithm\sifted_img2.jpg", sifted_img2)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



keypoints, descriptors = sift.detectAndCompute(img, None)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



path = r"D:\Projects\Computer Vision\SIFT Algorithm\edited-egypt-pyramids.jpg"
img2 = cv2.imread(path, 0)


keypoints2, descriptors2 = sift.detectAndCompute(img2, None)


norm = cv2.NORM_L2
bruteForce = cv2.BFMatcher(norm)
matches = bruteForce.match(descriptors, descriptors2)


matches = sorted(matches, key = lambda match:match.distance)
matched_img = cv2.drawMatches(
                             img, keypoints,
                             img2, keypoints2,
                             matches[:100], img2.copy()
                             )


imshow("matched img", matched_img)


cv2.imwrite(r"D:\Projects\Computer Vision\SIFT Algorithm\matched_img.jpg", matched_img)





