import os

SB_Sun = [ 'SB000', ]#'SB001', 'SB002', 'SB003', 'SB004', 'SB005', 'SB006', 'SB007', 'SB008', 'SB009', 'SB010', 'SB011', 'SB012', 'SB013', 'SB014', 'SB015', 'SB016', 'SB017', 'SB018', 'SB019', 'SB020', 'SB021', 'SB022', 'SB023', 'SB024', 'SB025', 'SB026', 'SB027', 'SB028', 'SB029', 'SB030', 'SB031', 'SB032', 'SB033', 'SB034', 'SB035', 'SB036', 'SB037', 'SB038', 'SB039', 'SB040', 'SB041', 'SB042', 'SB043', 'SB044', 'SB045', 'SB046', 'SB047', 'SB048', 'SB049', 'SB050', 'SB051', 'SB052', 'SB053', 'SB054', 'SB055', 'SB056', 'SB057', 'SB058', 'SB059']

SB_Calibrator = [ 'SB060', ]#'SB061', 'SB062', 'SB063', 'SB064', 'SB065', 'SB066', 'SB067', 'SB068', 'SB069', 'SB070', 'SB071', 'SB072', 'SB073', 'SB074', 'SB075', 'SB076', 'SB077', 'SB078', 'SB079', 'SB080', 'SB081', 'SB082', 'SB083', 'SB084', 'SB085', 'SB086', 'SB087', 'SB088', 'SB089', 'SB090', 'SB091', 'SB092', 'SB093', 'SB094', 'SB095', 'SB096', 'SB097', 'SB098', 'SB099', 'SB100', 'SB101', 'SB102', 'SB103', 'SB104', 'SB105', 'SB106', 'SB107', 'SB108', 'SB109', 'SB110', 'SB111', 'SB112', 'SB113', 'SB114', 'SB115', 'SB116', 'SB117', 'SB118', 'SB119']


obsvID = "L2025886" #L2025887
obsvID2 = "L2025887"
calibrator = "CasA"
pointings = ["SAP000", "SAP001"]

# tstart = "07Sep2017/10:10:30" #"07Sep2017/10:10:30"
# tstop  = "07Sep2017/10:11:00" #"07Sep2017/10:11:00"
# tstart1 = "07Sep2017/10:12:29.8" #"07Sep2017/10:10:30"
# tstop1  = "07Sep2017/10:13:30.2" #"07Sep2017/10:11:00"
# tstart2 = "07Sep2017/10:10:00" #"07Sep2017/10:10:30"
# tstop2  = "07Sep2017/10:13:00" #"07Sep2017/10:11:00"
tstart = "21Sep2023/12:48:00" #"21Sep2023/12:56:00" #"21Sep2023/12:48:00" #"21Sep2023/12:34:00"
tstop = "21Sep2023/12:49:00" #"21Sep2023/12:57:00" #"21Sep2023/12:48:00" #"21Sep2023/12:35:00"

data_dir = "/net/zernike/scratch3/hgan/data/raw_data/L2025886/" #"/net/zernike/scratch3/hgan/data/raw_data/"
model_dir = "/net/zernike/scratch3/hgan/data/model/"
save_dir = "/net/zernike/scratch3/hgan/processed/" + obsvID + "_new_cal2/"

for i in range(len(SB_Calibrator)):
    save_dir_SB = save_dir + SB_Sun[i] + "/"
    cmdstr = "rm -rf " + save_dir_SB
    os.system(cmdstr)
    cmdstr = "mkdir -p " + save_dir_SB
    os.system(cmdstr)
    # cmdstr = "rm -rf " + save_dir + calibrator + "_"+SB_Calibrator[i]+"_raw.MS"
    # os.system(cmdstr)
    # cmdstr = "rm -rf " + save_dir + "Sun_"+SB_Sun[i]+"_Cycle0_raw.MS"
    # os.system(cmdstr)

    cmdstr = "DPPP" + \
             " msin=" + data_dir + obsvID2 + "_" + pointings[1] +"_"+SB_Calibrator[i]+"_uv.MS" + \
             " msin.starttime="+tstart + \
             " msin.endtime="+tstop + \
             " msout=" + save_dir_SB + calibrator + "_"+SB_Calibrator[i]+"_Cycle0_raw.MS" + \
             " steps=[]"
    os.system(cmdstr)

    cmdstr = "DPPP" + \
             " msin=" + data_dir + obsvID + "_" + pointings[0] +"_"+SB_Sun[i]+"_uv.MS" + \
             " msin.starttime="+tstart + \
             " msin.endtime="+tstop + \
             " msout=" + save_dir_SB + "Sun_"+SB_Sun[i]+"_Cycle0_raw.MS" + \
             " steps=[]"
    os.system(cmdstr)

    #
    # cmdstr = "cp -a " + save_dir_SB + "Sun_"+SB_Sun[i]+"_Cycle0_raw.MS " + save_dir_SB + "Sun_"+SB_Sun[i]+"_Cycle1_raw.MS"
    # os.system(cmdstr)
    # cmdstr = "cp -a " + save_dir_SB + "Sun_"+SB_Sun[i]+"_Cycle0_raw.MS " + save_dir_SB + "Sun_"+SB_Sun[i]+"_Cycle2_raw.MS"
    # os.system(cmdstr)
    # cmdstr = "cp -a " + save_dir_SB + calibrator + "_"+SB_Calibrator[i]+"_Cycle0_raw.MS " + save_dir_SB + calibrator + "_"+SB_Calibrator[i]+"_Cycle1_raw.MS"
    # os.system(cmdstr)
