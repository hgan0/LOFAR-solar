import os

SB_Sun = [ 'SB000', ]#'SB010', 'SB020', 'SB030', 'SB040', ]#'SB001', 'SB002', 'SB003', 'SB004', 'SB005', 'SB006', 'SB007', 'SB008', 'SB009', 'SB010', 'SB011', 'SB012', 'SB013', 'SB014', 'SB015', 'SB016', 'SB017', 'SB018', 'SB019', 'SB020', 'SB021', 'SB022', 'SB023', 'SB024', 'SB025', 'SB026', 'SB027', 'SB028', 'SB029', 'SB030', 'SB031', 'SB032', 'SB033', 'SB034', 'SB035', 'SB036', 'SB037', 'SB038', 'SB039', 'SB040', 'SB041', 'SB042', 'SB043', 'SB044', 'SB045', 'SB046', 'SB047', 'SB048', 'SB049', 'SB050', 'SB051', 'SB052', 'SB053', 'SB054', 'SB055', 'SB056', 'SB057', 'SB058', 'SB059']

SB_Calibrator = [ 'SB060',]# 'SB070', 'SB080', 'SB090', 'SB100',]#'SB061', 'SB062', 'SB063', 'SB064', 'SB065', 'SB066', 'SB067', 'SB068', 'SB069', 'SB070', 'SB071', 'SB072', 'SB073', 'SB074', 'SB075', 'SB076', 'SB077', 'SB078', 'SB079', 'SB080', 'SB081', 'SB082', 'SB083', 'SB084', 'SB085', 'SB086', 'SB087', 'SB088', 'SB089', 'SB090', 'SB091', 'SB092', 'SB093', 'SB094', 'SB095', 'SB096', 'SB097', 'SB098', 'SB099', 'SB100', 'SB101', 'SB102', 'SB103', 'SB104', 'SB105', 'SB106', 'SB107', 'SB108', 'SB109', 'SB110', 'SB111', 'SB112', 'SB113', 'SB114', 'SB115', 'SB116', 'SB117', 'SB118', 'SB119']


columns = [ "CORRECTED_DATA", ] #"DATA", "CORRECTED_DATA", "MODEL"]

obsvID = "L2025886"
calibrator = "CasA"
pointings = ["SAP000", "SAP001"]

save_dir = "/net/zernike/scratch3/hgan/processed/" + obsvID + "_exp1/case1/"
model_dir = "/net/zernike/scratch3/hgan/data/model/"

for i in range(len(SB_Sun)):
    save_dir_SB = save_dir + SB_Sun[i] + "/"
    save_dir_SB_img = save_dir_SB + "images/"
    # cmdstr = "rm -rf "+ save_dir_SB_img
    # os.system(cmdstr)
    cmdstr = "mkdir -p "+ save_dir_SB_img
    os.system(cmdstr)

    FITSname0 = save_dir_SB_img + "Sun_Cycle0_"
    MSname0 = save_dir_SB+"/Sun_"+SB_Sun[i]+"_Cycle0_avg.MS"

    cmdstr = "rm -rf " + FITSname0 + ".*"
    os.system(cmdstr)

    setting = "wsclean -j 40 -mem 80 -auto-mask 3 -auto-threshold 0.3 -fit-beam -make-psf -reorder " + \
             " -multiscale-scales 1,2,4,8,20,40,80 -mgain 0.05 -weight briggs 0 -size 600 600 " + \
             " -minuvw-m 0 -maxuvw-m 12000 -scale 20asec -pol I -niter 1500 "

    cmdstr = setting + " -data-column CORRECTED_DATA" + \
             " -name  "+ FITSname0 + \
             " "+ MSname0
    os.system(cmdstr)

    #
    # clean(vis=MSname0, imagename=FITSname0, niter=150, gain=0.05, imsize=600, cell='20arcsec', weighting='briggs', uvrange='0~12km', multiscale=[1,2,4,8,20,40,80], smallscalebias=0.75)
    #
    # exportfits(imagename=FITSname0+'.image', fitsimage=save_dir_SB_img+'/Sun_cycle0_image.fits', overwrite=True, history=False)
    # exportfits(imagename=FITSname0+'.model', fitsimage=save_dir_SB_img+'/Sun_cycle0_model.fits', overwrite=True, history=False)

