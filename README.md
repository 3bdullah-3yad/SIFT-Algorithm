# SIFT-Algorithm

Suppose we have two images. One image is of a bench in a park. The
second image is of the entire park, which also includes the bench. Now
suppose we want to write code that helps us find the bench inside the
park image. You might think this is an easy task, but let me add some
complexity. What if the image of the bench is a zoomed image? Or what if
it is rotated? Or both? How are you going to deal with it now?
<br><br>The answer lies in the scale-invariant feature transform, or SIFT
algorithm. As the name suggest, it is scale invariant, which means that no
matter how much we zoom in on (or out of) the image, we can still find
similarities. Another feature of this algorithm is that it is rotation invariant.
Regardless of degree of rotation, it still performs well. The only issue
with this algorithm is that it’s patented, which means that for academic
purposes it’s good, but for commercial purpose there may be lot of legal
issues involved with using it. However, this won’t stop us from learning
and applying this algorithm for now.
<br><br>We first must understand the basics of the algorithm. Then we can
apply it to finding similarities between two images using Python and then
we’ll look at the code line by line.

<br><br>**Let’s look at the features of the image that the SIFT algorithm tries to
factor out during processing:**

- Scale (zoomed-in or zoomed-out image)
- Rotation
- Illumination
- Perspective

<br><br>As you can see, not only are scale and rotation accommodated, the
SIFT algorithm also takes care of the illumination present in the image and
the perspective from which we are looking. But how does it do all of this?
Let’s take a look at the step-by-step process of using the SIFT algorithm:
1. Find and constructing a space to ensure scale
invariance
2. Find the difference between the gaussians
3. Find the important points present inside the image
4. Remove the unimportant points to make efficient
comparisons
5. Provide orientation to the important points found in
step 3
6. Identifying the key features uniquely.
