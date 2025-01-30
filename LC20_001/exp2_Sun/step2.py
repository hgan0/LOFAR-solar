import os
from joblib import Parallel, delayed


SB_Sun = [ 'SB000', 'SB001', 'SB002', 'SB003', 'SB004', 'SB005', 'SB006', 'SB007', 'SB008', 'SB009',]# 'SB010', 'SB011', 'SB012', 'SB013', 'SB014', 'SB015', 'SB016', 'SB017', 'SB018', 'SB019', 'SB020', 'SB021', 'SB022', 'SB023', 'SB024', 'SB025', 'SB026', 'SB027', 'SB028', 'SB029', 'SB030', 'SB031', 'SB032', 'SB033', 'SB034', 'SB035', 'SB036', 'SB037', 'SB038', 'SB039', 'SB040', 'SB041', 'SB042', 'SB043', 'SB044', 'SB045', 'SB046', 'SB047', 'SB048', 'SB049', 'SB050', 'SB051', 'SB052', 'SB053', 'SB054', 'SB055', 'SB056', 'SB057', 'SB058', 'SB059']

SB_Calibrator = [ 'SB060', 'SB061', 'SB062', 'SB063', 'SB064', 'SB065', 'SB066', 'SB067', 'SB068', 'SB069', ]#'SB070', 'SB071', 'SB072', 'SB073', 'SB074', 'SB075', 'SB076', 'SB077', 'SB078', 'SB079', 'SB080', 'SB081', 'SB082', 'SB083', 'SB084', 'SB085', 'SB086', 'SB087', 'SB088', 'SB089', 'SB090', 'SB091', 'SB092', 'SB093', 'SB094', 'SB095', 'SB096', 'SB097', 'SB098', 'SB099', 'SB100', 'SB101', 'SB102', 'SB103', 'SB104', 'SB105', 'SB106', 'SB107', 'SB108', 'SB109', 'SB110', 'SB111', 'SB112', 'SB113', 'SB114', 'SB115', 'SB116', 'SB117', 'SB118', 'SB119']

obsvID = "L2025886"
calibrator = "CasA"
pointings = ["SAP000", "SAP001"]

timewindow1="600" # 600
threshold1="1.0"   # 1.
timewindow2="600" # 600
threshold2="1.0"   # 1.

save_dir = "/net/zernike/scratch3/hgan/processed/" + obsvID + "_exp2/case4/"
model_dir = "/net/zernike/scratch3/hgan/data/model/"

for i in range(len(SB_Sun)):
    save_dir_SB = save_dir + SB_Sun[i] + "/"
    cmdstr = "rm -rf " + save_dir_SB + "Sun_"+SB_Sun[i]+"_Cycle0_avg.MS"
    os.system(cmdstr)

    # Flagging and averaging
    cmdstr = "DPPP" + \
             " msin=" + save_dir_SB + "Sun_"+SB_Sun[i]+"_Cycle0_raw.MS" + \
             " msout=" + save_dir_SB + "Sun_"+SB_Sun[i]+"_Cycle0_avg.MS" + \
             " steps=[flag]" + \
             " flag.type=madflagger" + \
             " flag.threshold=" + threshold1 + \
             " flag.timewindow=" + timewindow1 + \
             " flag.correlations=[0,3,1,2]"
    os.system(cmdstr)

    # Calibration: Apply solution from the calibrator
    cmdstr = "DPPP" + \
             " msin=" + save_dir_SB + "Sun_"+SB_Sun[i]+"_Cycle0_avg.MS" + \
             " msout=" + save_dir_SB + "Sun_"+SB_Sun[i]+"_Cycle0_avg.MS" + \
             " msout.datacolumn=CORRECTED_DATA" + \
             " steps=[applycal]" + \
             " applycal.parmdb=" + save_dir_SB + calibrator + "_"+SB_Calibrator[i]+"_Cycle0_avg.MS/instrument"
    os.system(cmdstr)

    # Flagging of calibrated data
    cmdstr = "DPPP" + \
             " msin=" + save_dir_SB + "Sun_"+SB_Sun[i]+"_Cycle0_avg.MS" + \
             " msin.datacolumn=CORRECTED_DATA" + \
             " msout=" + save_dir_SB + "Sun_"+SB_Sun[i]+"_Cycle0_avg.MS" + \
             " msout.datacolumn=CORRECTED_DATA" + \
             " steps=[flag]" + \
             " flag.type=madflagger" + \
             " flag.threshold=" + threshold2 + \
             " flag.timewindow=" + timewindow2 + \
             " flag.correlations=[0,3,1,2]"
    os.system(cmdstr)
