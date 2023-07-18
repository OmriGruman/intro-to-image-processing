# %% [markdown]
# Let's identify coins!
# in the image given below we want to detect each coin currency,
# and we'll do it with cv2.HoughCircles!

# %%
# to run in google colab
import sys
if 'google.colab' in sys.modules:
    import subprocess 
    subprocess.call('apt-get install subversion'.split())
    subprocess.call('svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_04b_hough_transform/ex4b/coins.png'.split())

# %%
from matplotlib import pyplot as plt
import cv2

figsize = (10, 10)

# %%
im3 = cv2.imread("coins.png")
im3 = cv2.cvtColor(im3, cv2.COLOR_BGR2RGB)
im = cv2.cvtColor(im3, cv2.COLOR_RGB2GRAY)
res = im3.copy()

# TODO: fill in the best values possible 
# to detect the right circle dimeter and place
acc_ratio = 1
min_dist = 70
canny_upper_th = 450
acc_th = 50
circles = cv2.HoughCircles(im, cv2.HOUGH_GRADIENT, acc_ratio,
                           min_dist, param1=canny_upper_th,
                           param2=acc_th, minRadius=None, maxRadius=None)

#=== font vars
font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (-40, 10)
fontScale = 0.8
fontColor = (0,0,0)
lineType = 2

# ==== for each detected circle
for x, y, r in circles[0, :].astype(int):
    # draw the outer circle
    res = cv2.circle(res, (x, y), r, (0, 255, 0), 3)
    
    # TODO: write currency type on each coin.
    # use cv2.putText() and the font vars above.
    # If you need, different coin sizes can be found here:
    # https://avocadoughtoast.com/weights-sizes-us-coins/
    if r < 53:
        currency = "0.10$"
    elif r < 62:
        currency = "0.05$"
    else:
        currency = "0.25$"

    org = (x + bottomLeftCornerOfText[0], y + bottomLeftCornerOfText[1])
    res = cv2.putText(res, currency, org, font, fontScale, fontColor, 2, lineType)


plt.figure(figsize=figsize)
plt.imshow(res)
plt.title("final result- coins detection")
plt.show()

# %%