import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

smkt_data_winter = pd.read_csv(r"E:\Python_builds\GIPSY_TEST\smkt_winter.csv")
smkt_data_spring = pd.read_csv(r"E:\Python_builds\GIPSY_TEST\smkt_spring.csv")
smkt_data_summer = pd.read_csv(r"E:\Python_builds\GIPSY_TEST\smkt_summer.csv")
smkt_data_autumn = pd.read_csv(r"E:\Python_builds\GIPSY_TEST\smkt_autumn.csv")

bmcl_data_winter = pd.read_csv(r"E:\Python_builds\GIPSY_TEST\bmcl_winter.csv")
bmcl_data_spring = pd.read_csv(r"E:\Python_builds\GIPSY_TEST\bmcl_spring.csv")
bmcl_data_summer = pd.read_csv(r"E:\Python_builds\GIPSY_TEST\bmcl_summer.csv")
bmcl_data_autumn = pd.read_csv(r"E:\Python_builds\GIPSY_TEST\bmcl_autumn.csv")

dngd_data_winter = pd.read_csv(r"E:\Python_builds\GIPSY_TEST\dngd_winter.csv")
dngd_data_spring = pd.read_csv(r"E:\Python_builds\GIPSY_TEST\dngd_spring.csv")
dngd_data_summer = pd.read_csv(r"E:\Python_builds\GIPSY_TEST\dngd_summer.csv")
dngd_data_autumn = pd.read_csv(r"E:\Python_builds\GIPSY_TEST\dngd_autumn.csv")

smkt_zwd_winter = smkt_data_winter.ZWD
bmcl_zwd_winter = bmcl_data_winter.ZWD
dngd_zwd_winter = dngd_data_winter.ZWD

smkt_zwd_spring = smkt_data_spring.ZWD
bmcl_zwd_spring = bmcl_data_spring.ZWD
dngd_zwd_spring = dngd_data_spring.ZWD

smkt_zwd_summer = smkt_data_summer.ZWD
bmcl_zwd_summer = bmcl_data_summer.ZWD
dngd_zwd_summer = dngd_data_summer.ZWD

smkt_zwd_autumn = smkt_data_autumn.ZWD
bmcl_zwd_autumn = bmcl_data_autumn.ZWD
dngd_zwd_autumn = dngd_data_autumn.ZWD


smkt_Error_winter = smkt_data_winter.Error
bmcl_Error_winter = bmcl_data_winter.Error
dngd_Error_winter = dngd_data_winter.Error

smkt_Error_spring = smkt_data_spring.Error
bmcl_Error_spring = bmcl_data_spring.Error
dngd_Error_spring = dngd_data_spring.Error

smkt_Error_summer = smkt_data_summer.Error
bmcl_Error_summer = bmcl_data_summer.Error
dngd_Error_summer = dngd_data_summer.Error

smkt_Error_autumn = smkt_data_autumn.Error
bmcl_Error_autumn = bmcl_data_autumn.Error
dngd_Error_autumn = dngd_data_autumn.Error

#

zsmkt_winter_std = np.mean(smkt_Error_winter)*1000
zsmkt_spring_std = np.mean(smkt_Error_spring)*1000
zsmkt_summer_std = np.mean(smkt_Error_summer)*1000
zsmkt_autumn_std = np.mean(smkt_Error_autumn)*1000

zbmcl_winter_std = np.mean(bmcl_Error_winter)*1000
zbmcl_spring_std = np.mean(bmcl_Error_spring)*1000
zbmcl_summer_std = np.mean(bmcl_Error_summer)*1000
zbmcl_autumn_std = np.mean(bmcl_Error_autumn)*1000

zdngd_winter_std = np.mean(dngd_Error_winter)*1000
zdngd_spring_std = np.mean(dngd_Error_spring)*1000
zdngd_summer_std = np.mean(dngd_Error_summer)*1000
zdngd_autumn_std = np.mean(dngd_Error_autumn)*1000

#

zsmkt_winter_mean = np.mean(smkt_zwd_winter)*1000
zsmkt_spring_mean = np.mean(smkt_zwd_spring)*1000
zsmkt_summer_mean = np.mean(smkt_zwd_summer)*1000
zsmkt_autumn_mean = np.mean(smkt_zwd_autumn)*1000

zbmcl_winter_mean = np.mean(bmcl_zwd_winter)*1000
zbmcl_spring_mean = np.mean(bmcl_zwd_spring)*1000
zbmcl_summer_mean = np.mean(bmcl_zwd_summer)*1000
zbmcl_autumn_mean = np.mean(bmcl_zwd_autumn)*1000

zdngd_winter_mean = np.mean(dngd_zwd_winter)*1000
zdngd_spring_mean = np.mean(dngd_zwd_spring)*1000
zdngd_summer_mean = np.mean(dngd_zwd_summer)*1000
zdngd_autumn_mean = np.mean(dngd_zwd_autumn)*1000

# zsmkt_winter_std = np.std(smkt_zwd_winter)
# zsmkt_spring_std = np.std(smkt_zwd_spring)
# zsmkt_summer_std = np.std(smkt_zwd_summer)
# zsmkt_autumn_std = np.std(smkt_zwd_autumn)

# zbmcl_winter_std = np.std(bmcl_zwd_winter)
# zbmcl_spring_std = np.std(bmcl_zwd_spring)
# zbmcl_summer_std = np.std(bmcl_zwd_summer)
# zbmcl_autumn_std = np.std(bmcl_zwd_autumn)

# zdngd_winter_std = np.std(dngd_zwd_winter)
# zdngd_spring_std = np.std(dngd_zwd_spring)
# zdngd_summer_std = np.std(dngd_zwd_summer)
# zdngd_autumn_std = np.std(dngd_zwd_autumn)


station = ['DNGD', 'BMCL', 'SMKT', 'DNGD', 'BMCL', 'SMKT', 'DNGD', 'BMCL', 'SMKT', 'DNGD', 'BMCL', 'SMKT']
x_pos = [1,2,3,6,7,8,11,12,13,16,17,18]
x_pos_w = [1,2,3]
x_pos_sp = [6,7,8]
x_pos_s = [11,12,13]
x_pos_f = [16,17,18]

CTEz_w =[zdngd_winter_mean, zbmcl_winter_mean, zsmkt_winter_mean]
errorz_w =[zdngd_winter_std, zbmcl_winter_std, zsmkt_winter_std]
CTEz_sp =[zdngd_spring_mean, zbmcl_spring_mean, zsmkt_spring_mean]
errorz_sp =[zdngd_spring_std, zbmcl_spring_std, zsmkt_spring_std]
CTEz_s =[zdngd_summer_mean, zbmcl_summer_mean, zsmkt_summer_mean]
errorz_s =[zdngd_summer_std, zbmcl_summer_std, zsmkt_summer_std]
CTEz_f =[zdngd_autumn_mean, zbmcl_autumn_mean, zsmkt_autumn_mean]
errorz_f =[zdngd_autumn_std, zbmcl_autumn_std, zsmkt_autumn_std]


fig, ax = plt.subplots(1,1,  figsize = (12.5,7.5))
ax.bar(x_pos_w, CTEz_w, yerr=errorz_w, color = "blue", label = "Winter", align='center', alpha=0.5, ecolor='black', capsize=10)
ax.bar(x_pos_sp, CTEz_sp, yerr=errorz_sp, color = "green", label = "Spring", align='center', alpha=0.5, ecolor='black', capsize=10)
ax.bar(x_pos_s, CTEz_s, yerr=errorz_s, color = "orange", label = "Summer", align='center', alpha=0.5, ecolor='black', capsize=10)
ax.bar(x_pos_f, CTEz_f, yerr=errorz_f, color = "brown", label = "Fall", align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel("ZWD (mm)")
ax.set_xticks(x_pos)
ax.set_xticklabels(station)
ax.yaxis.grid(True)
ax.legend(loc = "upper right", prop={'size': 9})
plt.show()