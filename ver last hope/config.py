image_scale = 1000
round_pose = 1 #----> less than number of image
scale = 1 #default is 1 ---->round 2:4k | 4/3:2k | 1:FHD
cam_type = "Ver" #"Hor = Horizontal cam, Ver = Vertical cam"
crop_Hor = 0
crop_Ver = 0
window_name = "Game pose"
Parent_folder = "A:\\mediapipe\\ver last hope\\" #changeable
#                ^^^^^^^^^^^^^^^^^^^  --->example (place *folder* that you installed) always follow by "\\"

























image_folder_name = "raw ref img\\put image here"#don't change
image_folder = Parent_folder+image_folder_name
output_folder_name = "reference image deletable"#don't change
ouput_all_image = Parent_folder+output_folder_name
reference_file_name = "all_reference_poses_point_deletable.py" #don't change
ouput_all_point = Parent_folder+reference_file_name
