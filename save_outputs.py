import scipy.io as sio
import os
import cv2

path = "CFL_data"
vessel_folders = [
    "VesselD20H15",
    "VesselD50H5",
    "VesselD50H10P",
    "VesselD50H20P",
    "VesselD75H15P",
    "VesselD75H20",
    "VesselD100H5",
    "VesselD100H20P",
    "VesselD150H10P",
]

for folder in vessel_folders:
    print(folder)
    if os.path.exists(os.path.join(path, folder, "Output_GRADxyt", "OUTPUT.mat")):
        output_path = os.path.join(path, folder, "Output_GRADxyt", "OUTPUT.mat")
    else:
        output_path = os.path.join(path, folder, "Output_GRADxy", "OUTPUT.mat")
    print(output_path)
    output = sio.loadmat(output_path)
    try:
        os.mkdir(os.path.join(path, 'input'))
        os.mkdir(os.path.join(path, 'output'))
    except FileExistsError:
        pass
    for i in range(output["MI_core_l"].shape[2]):
        core_img = output["MI_core_l"][:, :, i]
        cv2.imwrite(os.path.join(path, 'output', "{}_{}.jpg".format(folder, i)), core_img * 255)
        RC_img = output["MI_RC_l"][:, :, i]
        cv2.imwrite(os.path.join(path, "input", "{}_{}.jpg".format(folder, i)), RC_img)