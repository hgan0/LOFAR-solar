import os
from joblib import Parallel, delayed

SB_Sun = [ 'SB000', 'SB001', 'SB002', 'SB003', 'SB004', 'SB005', 'SB006', 'SB007', 'SB008', 'SB009',]# 'SB010', 'SB011', 'SB012', 'SB013', 'SB014', 'SB015', 'SB016', 'SB017', 'SB018', 'SB019', 'SB020', 'SB021', 'SB022', 'SB023', 'SB024', 'SB025', 'SB026', 'SB027', 'SB028', 'SB029', 'SB030', 'SB031', 'SB032', 'SB033', 'SB034', 'SB035', 'SB036', 'SB037', 'SB038', 'SB039', 'SB040', 'SB041', 'SB042', 'SB043', 'SB044', 'SB045', 'SB046', 'SB047', 'SB048', 'SB049', 'SB050', 'SB051', 'SB052', 'SB053', 'SB054', 'SB055', 'SB056', 'SB057', 'SB058', 'SB059']

SB_Calibrator = [ 'SB060', 'SB061', 'SB062', 'SB063', 'SB064', 'SB065', 'SB066', 'SB067', 'SB068', 'SB069', ]#'SB070', 'SB071', 'SB072', 'SB073', 'SB074', 'SB075', 'SB076', 'SB077', 'SB078', 'SB079', 'SB080', 'SB081', 'SB082', 'SB083', 'SB084', 'SB085', 'SB086', 'SB087', 'SB088', 'SB089', 'SB090', 'SB091', 'SB092', 'SB093', 'SB094', 'SB095', 'SB096', 'SB097', 'SB098', 'SB099', 'SB100', 'SB101', 'SB102', 'SB103', 'SB104', 'SB105', 'SB106', 'SB107', 'SB108', 'SB109', 'SB110', 'SB111', 'SB112', 'SB113', 'SB114', 'SB115', 'SB116', 'SB117', 'SB118', 'SB119']


column_opt = [ "DATA", "CORRECTED_DATA", "MODEL"]

obsvID = "L2025886"
calibrator = "CasA"
pointings = ["SAP000", "SAP001"]

data_dir = "/net/zernike/scratch3/hgan/processed/" + obsvID + "_exp2/case4/"
model_dir = "/net/zernike/scratch3/hgan/data/model/"
save_dir = data_dir

def imaging_FITS(setting, column, FITSname, MSname):
    cmdstr = setting + " -data-column " + column + \
            " -name  " + FITSname + column + \
            " "+ MSname
    os.system(cmdstr)


for i in range(len(SB_Sun)):
    save_dir_SB = save_dir + SB_Sun[i] + "/"
    save_dir_SB_img = save_dir_SB + "images/"

    cmdstr = "mkdir -p "+ save_dir_SB_img
    os.system(cmdstr)

    setting = "wsclean -j 40 -mem 80 -auto-mask 3 -auto-threshold 0.3 -fit-beam -make-psf -reorder " + \
             " -multiscale-scales 1,2,4,8,20,40,80 -mgain 0.05 -weight briggs 0 -size 600 600 " + \
             " -minuvw-m 500 -maxuvw-m 12000 -scale 20asec -pol I -niter 1500 -intervals-out 5 "

    # FITSname = save_dir_SB_img + "Sun_Cycle0_raw_"
    # MSname = save_dir_SB+"/Sun_"+SB_Sun[i]+"_Cycle0_raw.MS"

    FITSname = save_dir_SB_img + "Sun_Cycle0_avg_"
    MSname = save_dir_SB+"/Sun_"+SB_Sun[i]+"_Cycle0_avg.MS"

    FITSname0 = save_dir_SB_img + "Sun_Cycle1_avg_"
    MSname0 = save_dir_SB+"/Sun_"+SB_Sun[i]+"_Cycle1_avg.MS"

    # FITSname1 = save_dir_SB_img + "CasA_Cycle0_raw_"
    # MSname1 = save_dir_SB+"/CasA_"+SB_Calibrator[i]+"_Cycle0_raw.MS"

    FITSname2 = save_dir_SB_img + "CasA_Cycle0_avg_"
    MSname2 = save_dir_SB+"/CasA_"+SB_Calibrator[i]+"_Cycle0_avg.MS"

    FITSname3 = save_dir_SB_img + "Sun_flare_"
    MSname3 = save_dir_SB+"/Sun_flare_"+SB_Sun[i]+"_Cycle0.MS"

    FITSnames = [FITSname, FITSname0, FITSname2, FITSname3, ]
    MSnames = [MSname, MSname0, MSname2, MSname3,  ]
    columns = [column_opt[1], column_opt[1], column_opt[1], column_opt[1],  ]

    for ii in range(0,len(columns)):
        cmdstr = "rm -rf "+ FITSnames[ii] + "*.fits "
        os.system(cmdstr)

    element_run = Parallel(n_jobs=-1)(delayed(imaging_FITS)(setting, columns[k], FITSnames[k], MSnames[k]) for k in range(0,len(columns)))



wsclean -j 40 -mem 80 -auto-mask 3 -auto-threshold 0.3 -fit-beam -make-psf -reorder -multiscale-scales 1,2,4,8,20,40,80 -mgain 0.05 -weight briggs 0 -size 2400 2400 -minuvw-m 500 -maxuvw-m 12000 -scale 10asec -pol I -niter 10000 -join-channels -channels-out 16 -apply-primary-beam -deconvolution-channels 4 -fit-spectral-pol 2 -multiscale-shape gaussian -save-source-list -data-column CORRECTED_DATA -name  quiet_sun_model /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB000/Sun_SB000_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB001/Sun_SB001_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB002/Sun_SB002_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB003/Sun_SB003_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB004/Sun_SB004_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB005/Sun_SB005_Cycle0_avg.MS/  /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB006/Sun_SB006_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB007/Sun_SB007_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB008/Sun_SB008_Cycle0_avg.MS/  /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB009/Sun_SB009_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB010/Sun_SB010_Cycle0_avg.MS/  /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB011/Sun_SB011_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB012/Sun_SB012_Cycle0_avg.MS/  /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB013/Sun_SB013_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB014/Sun_SB014_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB015/Sun_SB015_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB016/Sun_SB016_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB017/Sun_SB017_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB018/Sun_SB018_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB019/Sun_SB019_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB020/Sun_SB020_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB021/Sun_SB021_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB022/Sun_SB022_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB023/Sun_SB023_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB024/Sun_SB024_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB025/Sun_SB025_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB026/Sun_SB026_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB027/Sun_SB027_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB028/Sun_SB028_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB029/Sun_SB029_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB030/Sun_SB030_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB031/Sun_SB031_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB032/Sun_SB032_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB033/Sun_SB033_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB034/Sun_SB034_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB035/Sun_SB035_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB036/Sun_SB036_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB037/Sun_SB037_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB038/Sun_SB038_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB039/Sun_SB039_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB040/Sun_SB040_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB041/Sun_SB041_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB042/Sun_SB042_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB043/Sun_SB043_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB044/Sun_SB044_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB045/Sun_SB045_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB046/Sun_SB046_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB047/Sun_SB047_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB048/Sun_SB048_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB049/Sun_SB049_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB050/Sun_SB050_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB051/Sun_SB051_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB052/Sun_SB052_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB053/Sun_SB053_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB054/Sun_SB054_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB055/Sun_SB055_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB056/Sun_SB056_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB057/Sun_SB057_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB058/Sun_SB058_Cycle0_avg.MS/ /net/zernike/scratch3/hgan/processed/L2025886_exp1/case3/SB059/Sun_SB059_Cycle0_avg.MS/


cluster /net/zernike/scratch3/hgan/processing/LC20_001/exp1_CasA/quiet_sun_model-sources-pb.txt /net/zernike/scratch3/hgan/processing/LC20_001/exp1_CasA/quiet_sun_model.txt 3 > clustering.log


editmodel -skymodel /net/zernike/scratch3/hgan/processing/LC20_001/exp1_CasA/sun_model.txt /net/zernike/scratch3/hgan/processing/LC20_001/exp1_CasA/quiet_sun_model.txt


makesourcedb in='/net/zernike/scratch3/hgan/processing/LC20_001/exp1_CasA/sun_model.txt' out='/net/zernike/scratch3/hgan/processing/LC20_001/exp1_CasA/sun_model.sourcedb'




