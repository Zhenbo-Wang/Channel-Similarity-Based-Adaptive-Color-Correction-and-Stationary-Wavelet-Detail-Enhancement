clear all; close all;

reference_path = 'E:\test\input\'; %  Input files
reference_path2 = 'E:\output\'
image_files = dir(fullfile(reference_path, '*.png')); 
total_images = numel(image_files); 
h = waitbar(0,'Processing Images...');

for i = 1:total_images
    reference_image_name = fullfile(reference_path, image_files(i).name);
    reference_image = imread(reference_image_name);
    

    [ssim_R,ssim_G,ssim_B] = get_ssim(reference_image);
    if ssim_R <= 0.7
        im1 = red_compensate(reference_image,5);
        reference_image = correction_color(im1,ssim_R,ssim_G,ssim_B);
    else
        reference_image = correction_color(reference_image,ssim_R,ssim_G,ssim_B);Run
    end
    reference_image = uint8(Wavelet_enhancement(reference_image));

    reference_image_name2 = fullfile(reference_path2, image_files(i).name);
    imwrite(reference_image, reference_image_name2);

    
    waitbar(i/total_images,h,sprintf('Processing Image %d of %d',i,total_images));
end


