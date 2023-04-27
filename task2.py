import subprocess
import distro
system_info = subprocess.check_output("lscpu").decode("utf-8").splitlines()


for line in system_info:
    if "Core(s) per socket" in line:
        core=[line.split(":")[1].strip()][0]
    if "Byte Order" in line:
        byte_order=[line.split(":")[1].strip()][0]
    if "Model name"  in line:
        model_name=[line.split(":")[1].strip()][0]
    if "CPU max MHz" in line:
        CPU_max_MHz=[line.split(":")[1].strip()][0]
    if "CPU min MHz" in line:
        CPU_min_MHz=[line.split(":")[1].strip()][0]
    if "L1i cache" in line:
        L1i_cache=[line.split(":")[1].strip()][0]
    if "L1d cache" in line:
        L1d_cache=[line.split(":")[1].strip()][0]
    if "L2 cache" in line:
        L2_cache=[line.split(":")[1].strip()][0]
    if "L3 cache" in line:
        L3_cache=[line.split(":")[1].strip()][0]
    if "Thread(s) per core" in line:
        thread_per_core=[line.split(":")[1].strip()][0]
    if "Virtualization:" in line:
        V1=[line.split(":")[1].strip()][0]

#     # Get distributor information
distributor_id = distro.id()
# distributor_codename = distro.codename()
distribution = distro.linux_distribution()
print("----------------SYSTEM INFORMATION--------------")
print("BYTE ORDER",byte_order)
print("CORE: ",core)
print("model_name  ",model_name)
print("cpu_max_freq(MHz)  ",CPU_max_MHz)
print("cpu_min_freq(MHz) ",CPU_min_MHz)
print("virtualization  ",V1)
print("l1i_cache_size(KiB) ",L1i_cache )
print("l1d_cache_size(KiB) ",L1d_cache )
print("l2_cache_size(MiB)  ",L2_cache)
print("l3_cache_size(MiB)  ",L3_cache)
print("thread_per_core  ",thread_per_core)
print("----------------DISTRIBUTOR INFORMATION--------------")
print("distributor_id         ",distribution[0])
print("distributor_description ",distribution[1])
print("distributor_codename   ",distribution[2])