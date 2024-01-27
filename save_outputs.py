import scipy.io as sio
import os
import cv2

path = "CFL_data"
vessel_folders = [
    "VesselD20H15",
    "VesselD50H5",
    "VesselD50H10",
    "VesselD50H10P",
    "VesselD50H20P",
    "VesselD75H15P",
    "VesselD75H20",
    "VesselD100H5",
    "VesselD100H20P",
    "VesselD150H10P",
]

output = sio.loadmat(
    os.path.join(path, vessel_folders[0], "Output_GRADxyt", "OUTPUT.mat")
)

print(output["MI_core_l"][:, :, 0].shape)

cv2.imshow("f", output["MI_core_l"][:, :, 0] * 255)
cv2.imwrite("example.jpg", output["MI_core_l"][:, :, 0] * 255)
cv2.waitKey()

cv2.destroyAllWindows()
cv2.imwrite("example.jpg", output["MI_core_l"][:, :, 0] * 255)
