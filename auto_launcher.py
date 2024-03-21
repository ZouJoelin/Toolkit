import subprocess
import time
from datetime import datetime


###########################################
# program to launch #######################
###########################################
def launch_on_GPU(gpu_id=0):
    command = f"python hello_world.py --gpu_id={gpu_id}"
    subprocess.run(command, shell=True)


###########################################
# Monitor Time ############################
###########################################
def monitor_time(start_time = "00:00"):
    while True:
        current_time = datetime.now().strftime("%H:%M")
        print(f"current_time: {current_time}")
        if current_time >= start_time:
            print(f"Time has past {start_time}. Launch program...")
            launch_on_GPU()
            return
        time.sleep(60) 


###########################################
# Monitor GPU memory ######################
###########################################
def get_GPUs_free_memory():
    command = "nvidia-smi --query-gpu=memory.free --format=csv"
    output = subprocess.check_output(command.split()).decode("utf-8").strip().split("\n")[1:]
    gpu_memory = [int(line.split()[0]) for line in output]
    return gpu_memory

def monitor_gpu_memory(threshold=10240):
    while True:
        GPUs_free_memory = get_GPUs_free_memory()
        current_time = datetime.now().strftime("%H:%M")
        print(f"{GPUs_free_memory} @{current_time}")
        for i, free_memory in enumerate(GPUs_free_memory):
            if free_memory >= threshold:
                print(f"GPU {i} has enough free memory ({free_memory} MB). Launch program......")
                launch_on_GPU(i)
                return
        time.sleep(600)  


if __name__ == "__main__":
    # print(get_gpu_memory_usage())
    # monitor_gpu_memory()
    monitor_time("19:55")
