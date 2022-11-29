import numpy as np
import pdb
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
import csv
import pdb

from unitree_legged_sdk_python_tools.utils.data_parsing import read_cvs_file

def main():

	# folder_name = "2022_11_22_16_43_76"; # from laptop
	# folder_name = "2022_11_22_16_46_34"; # inside the robot


	# folder_name = "2022_01_13_18_30_55"

	path2data = "./"

	data, file_names, joints_names = read_cvs_file(path2data,folder_name)

	# pdb.set_trace()

	data = data[:,10::,:]

	Njoints = 3
	k_cut = 0 # Cut the first time steps
	hdl_fig, hdl_splots = plt.subplots(Njoints,1,figsize=(13,9),sharex=True)
	hdl_fig.suptitle("Position - Right Leg")
	for jj in range(Njoints):
		time_stamp = data[0,k_cut::,0] # It's the same for all, q_des, q_curr, etc.
		hdl_splots[jj].plot(time_stamp,data[1,k_cut::,jj+1],label=file_names[1]) # desired
		# hdl_splots[jj].plot(time_stamp[5::],data[0,5::,jj+1],label=file_names[0]) # current (delay compensated)
		hdl_splots[jj].plot(time_stamp,data[0,:,jj+1],label=file_names[0]) # current
		hdl_splots[jj].set_title(joints_names[jj])
		hdl_splots[jj].set_ylabel("angle [rad]")
		hdl_splots[jj].legend()
	hdl_splots[Njoints-1].set_xlabel("time [sec]")


	hdl_fig, hdl_splots = plt.subplots(Njoints,1,figsize=(13,9),sharex=True)
	hdl_fig.suptitle("Velocity - Right Leg")
	k_cut = 10
	for jj in range(Njoints):
		time_stamp = data[0,k_cut::,0] # It's the same for all, q_des, q_curr, etc.

		joint_vel_vec = data[2,:,jj+1]

		joint_pos_vec = data[0,:,jj+1]
		joint_vel_vec_num_diff = np.diff(joint_pos_vec,prepend=0.0) / 0.002

		hdl_splots[jj].plot(time_stamp,joint_vel_vec[k_cut::],label=file_names[2])
		hdl_splots[jj].plot(time_stamp,joint_vel_vec_num_diff[k_cut::],label="dq_curr (num diff)")
		hdl_splots[jj].set_title(joints_names[jj])
		hdl_splots[jj].set_ylabel("angular velocity [rad/s]")
		hdl_splots[jj].legend()
	hdl_splots[Njoints-1].set_xlabel("time [sec]")


	hdl_fig, hdl_splots = plt.subplots(Njoints,1,figsize=(13,9),sharex=True)
	hdl_fig.suptitle("Torque - Right Leg")
	for jj in range(Njoints):
		time_stamp = data[0,k_cut::,0] # It's the same for all, q_des, q_curr, etc.
		hdl_splots[jj].plot(time_stamp,data[3,k_cut::,jj+1],label=file_names[3]) # u des
		hdl_splots[jj].plot(time_stamp,data[4,k_cut::,jj+1],label=file_names[4]) # u est
		hdl_splots[jj].set_title(joints_names[jj])
		hdl_splots[jj].set_ylabel("torque [Nm]")
		hdl_splots[jj].legend()
	hdl_splots[Njoints-1].set_xlabel("time [sec]")


	plt.show(block=True)




if __name__ == "__main__":

	main()