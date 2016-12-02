orig = imread('mandril.tif');
orig = orig(:,:,1);

im1 = imnoise(orig,'speckle', 0.0071);
im2 = imnoise(orig, 'salt & pepper', 0.0071);
im3 = imnoise(orig, 'gaussian', 0, 0.00197);
im4 = imnoise(orig, 'poisson');
im5 = imgaussfilt(orig, 1.17);

% mse1 = immse(orig, im1);
% mse2 = immse(orig, im2);
% mse3 = immse(orig, im3);
% mse4 = immse(orig, im4);
% mse5 = immse(orig, im5);
% 
% disp(mse1)
% disp(mse2)
% disp(mse3)
% disp(mse4)
% disp(mse5)

mse1 = psnr(orig, im1);
mse2 = psnr(orig, im2);
mse3 = psnr(orig, im3);
mse4 = psnr(orig, im4);
mse5 = psnr(orig, im5);

disp(mse1)
disp(mse2)
disp(mse3)
disp(mse4)
disp(mse5)

mse1 = ssim(orig, im1);
mse2 = ssim(orig, im2);
mse3 = ssim(orig, im3);
mse4 = ssim(orig, im4);
mse5 = ssim(orig, im5);

disp(mse1)
disp(mse2)
disp(mse3)
disp(mse4)
disp(mse5)

% name = 'mandril';
% imwrite(im1, [name '-speckle.png']);
% imwrite(im2, [name '-salt.png']);
% imwrite(im3, [name '-gauss.png']);
% imwrite(im4, [name '-poiss.png']);
% imwrite(im5, [name '-blur.png']);