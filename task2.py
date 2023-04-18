# import sys
# import cpuinfo
# print(sys.byteorder)

# print(cpuinfo.get_cpu_info()['brand'])

# import subprocess
# import platform
# #system_info=subprocess.check_output("lscpu", shell=True).strip().decode()

# system_info= platform.uname()
# print("BYTE ORDER",system_info.byteorder)

#import platform
import subprocess
import distro
system_info = subprocess.check_output("lscpu").decode("utf-8").splitlines()
#print(system_info)
core = [line.split(":")[1].strip() for line in system_info if "Core(s) per socket" in line][0]
byte_order=[line.split(":")[1].strip() for line in system_info if "Byte Order" in line][0]
model_name = [line.split(":")[1].strip() for line in system_info if "Model name" in line][0]
cpu_max_freq = [line.split(":")[1].strip().split()[0] for line in system_info if "CPU max MHz" in line][0]
cpu_min_freq = [line.split(":")[1].strip().split()[0] for line in system_info if "CPU min MHz" in line][0]
#virtualization = True if "vmx" in system_info else False
V1=[line.split(":")[1].strip().split()[0] for line in system_info if "Virtualization:" in line][0]
l1i_cache_size = [line.split(":")[1].strip().split()[0] for line in system_info if "L1i cache" in line][0]
l1d_cache_size = [line.split(":")[1].strip().split()[0] for line in system_info if "L1d cache" in line][0]
l2_cache_size = [line.split(":")[1].strip().split()[0] for line in system_info if "L2 cache" in line][0]
l3_cache_size = [line.split(":")[1].strip().split()[0] for line in system_info if "L3 cache" in line][0]
thread_per_core = [line.split(":")[1].strip() for line in system_info if "Thread(s) per core" in line][0]

#     # Get distributor information
distributor_id = distro.id()
#distributor_description = distro.LinuxDistribution()
distributor_codename = distro.codename()
distribution = distro.linux_distribution()
print("----------------SYSTEM INFORMATION--------------")
print("BYTE ORDER",byte_order)
print("CORE: ",core)
print("model_name  ",model_name)
print("cpu_max_freq(MHz)  ",cpu_max_freq)
print("cpu_min_freq(MHz) ",cpu_min_freq)
print("virtualization  ",V1)
print("l1i_cache_size(KiB) ",l1i_cache_size )
print("l1d_cache_size(KiB) ",l1d_cache_size )
print("l2_cache_size(MiB)  ",l2_cache_size)
print("l3_cache_size(MiB)  ",l3_cache_size)
print("thread_per_core  ",thread_per_core)
print("----------------DISTRIBUTOR INFORMATION--------------")
print("distributor_id         ",distribution[0])
print("distributor_description ",distribution[1])
print("distributor_codename   ",distribution[2])