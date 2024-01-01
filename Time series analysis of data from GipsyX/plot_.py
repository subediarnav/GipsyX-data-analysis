import pandas as pd
import matplotlib.pyplot as plt

stations = ["bmcl", "dngd", "smkt"]

data_dngd = pd.read_csv("E:\Python_builds\GIPSY_TEST\combined_dngd_wet.csv")
data_dngd.sort_values(["Time"],axis=0, ascending=True,inplace=True,na_position='first',ignore_index=True)
data = pd.DataFrame(data_dngd)
time_dngd = data_dngd.Time
ZWD_dngd = data_dngd.ZWD*10**3


data_bmcl = pd.read_csv("E:\Python_builds\GIPSY_TEST\combined_bmcl_wet.csv")
data_bmcl.sort_values(["Time"],axis=0, ascending=True,inplace=True,na_position='first',ignore_index=True)
data = pd.DataFrame(data_bmcl)
time_bmcl = data_bmcl.Time
ZWD_bmcl = data_bmcl.ZWD*10**3



data_smkt = pd.read_csv("E:\Python_builds\GIPSY_TEST\combined_smkt_wet.csv")
data_smkt.sort_values(["Time"],axis=0, ascending=True,inplace=True,na_position='first',ignore_index=True)
data = pd.DataFrame(data_bmcl)
time_smkt = data_smkt.Time
ZWD_smkt = data_smkt.ZWD*10**3


# DNGD

start_dngd = min(time_dngd)
newt_dngd = []
for i in range(len(data_dngd)):
    t = (time_dngd[i]-start_dngd)/(3600*24)
    newt_dngd.append(t)
data_dngd["new_time"] = newt_dngd

new_time_dngd = data_dngd.new_time

# BMCL
start_bmcl = min(time_bmcl)
newt_bmcl = []
for i in range(len(data_bmcl)):
    t = (time_bmcl[i]-start_bmcl)/(3600*24)
    newt_bmcl.append(t)
data_bmcl["new_time"] = newt_bmcl

new_time_bmcl = data_bmcl.new_time

# SMKT
start_smkt = min(time_smkt)
newt_smkt = []
for i in range(len(data_smkt)):
    t = (time_smkt[i]-start_smkt)/(3600*24)
    newt_smkt.append(t)
data_smkt["new_time"] = newt_smkt

new_time_smkt = data_smkt.new_time



# fig, (ax1,ax2,ax3) = plt.subplots(3,1)
# ax1.plot(time_dngd, ZWD_dngd)
# ax1.grid()
# ax1.set_xlabel("time")
# ax1.set_ylabel("ZWD_dngd")

# ax2.plot(time_bmcl, ZWD_bmcl)
# ax2.grid()
# ax2.set_xlabel("time")
# ax2.set_ylabel("ZWD_bmcl")

# ax3.plot(time_smkt, ZWD_smkt)
# ax3.grid()
# ax3.set_xlabel("time")
# ax3.set_ylabel("ZWD_smkt")

plt.figure(figsize = (15,4))
plt.plot(new_time_dngd, ZWD_dngd, label = "DNGD", linewidth = 1, color = "orange")
plt.plot(new_time_bmcl, ZWD_bmcl, label = "BMCL", linewidth = 1, color = "blue")
plt.plot(new_time_smkt, ZWD_smkt, label = "SMKT", linewidth = 1, color = "black")
plt.grid()
plt.legend()
plt.xlabel("DOY")
plt.ylabel("ZWD (mm)")
plt.tight_layout()
plt.show()


