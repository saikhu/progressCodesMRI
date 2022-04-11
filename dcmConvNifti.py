'''
import dicom2nifti
import os


rootDir = "/raid/users/usman/unomic_data/00_origData/01_N"
dicom_directory = os.path.join(rootDir, '01_N_DCM')
# print(dicom_directory)
# print(os.path.isdir(dicom_directory))

if os.path.isdir(dicom_directory):
    print('Source dir is True: ', dicom_directory)

output_folder = os.path.join(rootDir, '01_N_Nifti')

if os.path.isdir(output_folder):
    print('Destination dir is True: ', output_folder)


dicom2nifti.convert_directory(
    dicom_directory, output_folder, compression=False, reorient=True)
'''


dcm2niix -z n -v y -s n -o /raid/users/usman/unomic_data/00_origData/01_N/01_N_Nifti/ -i /raid/users/usman/unomic_data/00_origData/01_N/01_N_DCM/