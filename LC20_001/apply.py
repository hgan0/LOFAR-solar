import os

SB_Sun = [ 'SB000', ] #[ 'SB000', 'SB001', 'SB002', 'SB003', 'SB004', 'SB005', 'SB006', 'SB007', 'SB008', 'SB009', 'SB010', 'SB011', 'SB012', 'SB013', 'SB014', 'SB015', 'SB016', 'SB017', 'SB018', 'SB019', 'SB020', 'SB021', 'SB022', 'SB023', 'SB024', 'SB025', 'SB026', 'SB027', 'SB028', 'SB029', 'SB030', 'SB031', 'SB032', 'SB033', 'SB034', 'SB035', 'SB036', 'SB037', 'SB038', 'SB039', 'SB040', 'SB041', 'SB042', 'SB043', 'SB044', 'SB045', 'SB046', 'SB047', 'SB048', 'SB049', 'SB050', 'SB051', 'SB052', 'SB053', 'SB054', 'SB055', 'SB056', 'SB057', 'SB058', 'SB059']

SB_Calibrator = [ 'SB060',] #[ 'SB060', 'SB061', 'SB062', 'SB063', 'SB064', 'SB065', 'SB066', 'SB067', 'SB068', 'SB069', 'SB070', 'SB071', 'SB072', 'SB073', 'SB074', 'SB075', 'SB076', 'SB077', 'SB078', 'SB079', 'SB080', 'SB081', 'SB082', 'SB083', 'SB084', 'SB085', 'SB086', 'SB087', 'SB088', 'SB089', 'SB090', 'SB091', 'SB092', 'SB093', 'SB094', 'SB095', 'SB096', 'SB097', 'SB098', 'SB099', 'SB100', 'SB101', 'SB102', 'SB103', 'SB104', 'SB105', 'SB106', 'SB107', 'SB108', 'SB109', 'SB110', 'SB111', 'SB112', 'SB113', 'SB114', 'SB115', 'SB116', 'SB117', 'SB118', 'SB119']


obsvID = "L2025886"
calibrator = "CasA"
pointings = ["SAP000", "SAP001"]


data_dir = "/net/zernike/scratch3/hgan/data/raw_data/L2025886/" #"/net/zernike/scratch3/hgan/data/raw_data/"
model_dir = "/net/zernike/scratch3/hgan/data/model/"
save_dir = "/net/zernike/scratch3/hgan/processed/" + obsvID + "/" #"_cal2/"

timewindow1="600" # 600
threshold1="1.0"   # 1.

for i in range(len(SB_Sun)): #[6, ]: #range(len(SB_Sun)):
    save_dir_SB = save_dir + SB_Sun[i] + "/"
    save_dir_SB_img = save_dir_SB + "images/"

    # Location of quiet Sun calibration solution
    calib = save_dir_SB + calibrator + "_cycle0.table" #"/Sun_cycle1.table"

    # Create MS for flare time interval
    MSname = save_dir_SB+"/Sun_flare_"+SB_Sun[i]+"_Cycle0.MS"
#    MSname = save_dir_SB+"/CasA_"+SB_Calibrator[i]+"_Cycle0_avg.MS"

    cmdstr = "rm -r "+MSname
    os.system(cmdstr)
#
    # Copy data for flare time interval
    cmdstr = "DPPP" + \
             " msin=" + data_dir + obsvID + "_" + pointings[0] +"_"+SB_Sun[i]+"_uv.MS" + \
             " msin.starttime=21Sep2023/12:48:00" + \
             " msin.endtime=21Sep2023/12:52:00"  + \
             " msout="+MSname + \
             " steps=[]"
    os.system(cmdstr)

    # Calibration with quiet-Sun solution
    cmdstr = "DPPP" + \
             " msin="+MSname + \
             " msout="+MSname + \
             " msout.datacolumn=CORRECTED_DATA" + \
             " steps=[applycal,applybeam]" + \
             " applycal.parmdb="+calib
#             " steps=[applycal,applybeam]" + \ #Only if no self-cal cycle 1
    os.system(cmdstr)

    #
    # cmdstr = "rm -f "+ save_dir_SB_img + "Sun_flare_Cycle0_*.fits"
    # os.system(cmdstr)

    setting = "wsclean -j 40 -mem 80 -auto-mask 3 -auto-threshold 0.3 -fit-beam -make-psf -reorder " + \
             " -multiscale-scales 1,2,4,8,20,40,80 -mgain 0.05 -weight briggs 0 -size 600 600 " + \
             " -minuvw-m 500 -maxuvw-m 12000 -scale 20asec -pol I -niter 1500 -intervals-out 12 -interval 0 1200"

    cmdstr = setting + " -data-column CORRECTED_DATA" + \
             " -name  "+ save_dir_SB_img + "Sun_flare_Cycle0_t1200_CORRECTED" + \
             " "+ MSname
    os.system(cmdstr)
