import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_autumn_smkt = pd.read_csv("E:\Python_builds\GIPSY_TEST\daily_combined_smkt_autumn.csv")
data_spring_smkt = pd.read_csv("E:\Python_builds\GIPSY_TEST\daily_combined_smkt_spring.csv")
data_summer_smkt = pd.read_csv("E:\Python_builds\GIPSY_TEST\daily_combined_smkt_summer.csv")
data_winter_smkt = pd.read_csv("E:\Python_builds\GIPSY_TEST\daily_combined_smkt_winter.csv")

data_autumn_bmcl = pd.read_csv("E:\Python_builds\GIPSY_TEST\daily_combined_bmcl_autumn.csv")
data_spring_bmcl = pd.read_csv("E:\Python_builds\GIPSY_TEST\daily_combined_bmcl_spring.csv")
data_summer_bmcl = pd.read_csv("E:\Python_builds\GIPSY_TEST\daily_combined_bmcl_summer.csv")
data_winter_bmcl = pd.read_csv("E:\Python_builds\GIPSY_TEST\daily_combined_bmcl_winter.csv")

data_autumn_dngd = pd.read_csv("E:\Python_builds\GIPSY_TEST\daily_combined_dngd_autumn.csv")
data_spring_dngd = pd.read_csv("E:\Python_builds\GIPSY_TEST\daily_combined_dngd_spring.csv")
data_summer_dngd = pd.read_csv("E:\Python_builds\GIPSY_TEST\daily_combined_dngd_summer.csv")
data_winter_dngd = pd.read_csv("E:\Python_builds\GIPSY_TEST\daily_combined_dngd_winter.csv")



data_autumn_smkt_ = pd.DataFrame(data_autumn_smkt)
data_autumn_smkt_['Mean'] = data_autumn_smkt_.mean(axis=1)
mean_autumn_smkt = data_autumn_smkt_.Mean

data_spring_smkt_ = pd.DataFrame(data_spring_smkt)
data_spring_smkt_['Mean'] = data_spring_smkt_.mean(axis=1)
mean_spring_smkt = data_spring_smkt_.Mean

data_summer_smkt_ = pd.DataFrame(data_summer_smkt)
data_summer_smkt_['Mean'] = data_summer_smkt_.mean(axis=1)
mean_summer_smkt = data_summer_smkt_.Mean

data_winter_smkt_ = pd.DataFrame(data_winter_smkt)
data_winter_smkt_['Mean'] = data_winter_smkt_.mean(axis=1)
mean_winter_smkt = data_winter_smkt_.Mean



data_autumn_bmcl_ = pd.DataFrame(data_autumn_bmcl)
data_autumn_bmcl_['Mean'] = data_autumn_bmcl_.mean(axis=1)
mean_autumn_bmcl = data_autumn_bmcl_.Mean

data_spring_bmcl_ = pd.DataFrame(data_spring_bmcl)
data_spring_bmcl_['Mean'] = data_spring_bmcl_.mean(axis=1)
mean_spring_bmcl = data_spring_bmcl_.Mean

data_summer_bmcl_ = pd.DataFrame(data_summer_bmcl)
data_summer_bmcl_['Mean'] = data_summer_bmcl_.mean(axis=1)
mean_summer_bmcl = data_summer_bmcl_.Mean

data_winter_bmcl_ = pd.DataFrame(data_winter_bmcl)
data_winter_bmcl_['Mean'] = data_winter_bmcl_.mean(axis=1)
mean_winter_bmcl = data_winter_bmcl_.Mean



data_autumn_dngd_ = pd.DataFrame(data_autumn_dngd)
data_autumn_dngd_['Mean'] = data_autumn_dngd_.mean(axis=1)
mean_autumn_dngd = data_autumn_dngd_.Mean

data_spring_dngd_ = pd.DataFrame(data_spring_dngd)
data_spring_dngd_['Mean'] = data_spring_dngd_.mean(axis=1)
mean_spring_dngd = data_spring_dngd_.Mean

data_summer_dngd_ = pd.DataFrame(data_summer_dngd)
data_summer_dngd_['Mean'] = data_summer_dngd_.mean(axis=1)
mean_summer_dngd = data_summer_dngd_.Mean

data_winter_dngd_ = pd.DataFrame(data_winter_dngd)
data_winter_dngd_['Mean'] = data_winter_dngd_.mean(axis=1)
mean_winter_dngd = data_winter_dngd_.Mean



fig, axs = plt.subplots(2,2)

axs[0][0].plot(list(range(len(data_winter_smkt_))), 1000*mean_winter_smkt, color = "black", label = "smkt")
axs[0][0].plot(list(range(len(data_winter_bmcl_))), 1000*mean_winter_bmcl, color = "blue", label = "bmcl")
axs[0][0].plot(list(range(len(data_winter_dngd_))), 1000*mean_winter_dngd, color = "red", label = "dngd")
axs[0][0].set_title("Winter")
axs[0][0].set_xlabel("Time (Hrs)")
axs[0][0].set_ylabel("ZWD(m)")
axs[0][0].legend()
axs[0][0].grid()

axs[0][1].plot(list(range(len(data_summer_smkt_))), 1000*mean_summer_smkt, color = "black", label = "smkt")
axs[0][1].plot(list(range(len(data_summer_bmcl_))), 1000*mean_summer_bmcl, color = "blue", label = "bmcl")
axs[0][1].plot(list(range(len(data_summer_dngd_))), 1000*mean_summer_dngd, color = "red", label = "dngd")
axs[0][1].set_title("summer")
axs[0][1].set_xlabel("Time (Hrs)")
axs[0][1].set_ylabel("ZWD(m)")
axs[0][1].legend()
axs[0][1].grid()

axs[1][0].plot(list(range(len(data_spring_smkt_))), 1000*mean_spring_smkt, color = "black", label = "smkt")
axs[1][0].plot(list(range(len(data_spring_bmcl_))), 1000*mean_spring_bmcl, color = "blue", label = "bmcl")
axs[1][0].plot(list(range(len(data_spring_dngd_))), 1000*mean_spring_dngd, color = "red", label = "dngd")
axs[1][0].set_title("spring")
axs[1][0].set_xlabel("Time (Hrs)")
axs[1][0].set_ylabel("ZWD(m)")
axs[1][0].legend()
axs[1][0].grid()

axs[1][1].plot(list(range(len(data_autumn_smkt_))), 1000*mean_autumn_smkt, color = "black", label = "smkt")
axs[1][1].plot(list(range(len(data_autumn_bmcl_))), 1000*mean_autumn_bmcl, color = "blue", label = "bmcl")
axs[1][1].plot(list(range(len(data_autumn_dngd_))), 1000*mean_autumn_dngd, color = "red", label = "dngd")
axs[1][1].set_title("autumn")
axs[1][1].set_xlabel("Time (Hrs)")
axs[1][1].set_ylabel("ZWD(m)")
axs[1][1].legend()
axs[1][1].grid()

plt.tight_layout()
plt.show()