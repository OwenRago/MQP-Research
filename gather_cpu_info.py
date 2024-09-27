# gather_cpu_info.py
import os

output_file = "/output/cpu_info.txt"

# Function to gather CPU information
def gather_cpu_info():
    with open(output_file, "w") as f:
        f.write("Gathering CPU information...\n\n")

        # Get online CPUs
        with open("/sys/devices/system/cpu/online", "r") as online_file:
            online_cpus = online_file.read().strip()
            f.write(f"Online CPUs: {online_cpus}\n")
            

        # Iterate through each CPU directory and gather information
        cpu_dir = "/sys/devices/system/cpu"
        for cpu in sorted(os.listdir(cpu_dir)):
            if cpu.startswith("cpu") and cpu[3:].isdigit():
                
                f.write(f"\nInformation for {cpu}:\n")
                cpu_path = os.path.join(cpu_dir, cpu)

                # CPU Topology
                try:
                    with open(os.path.join(cpu_path, "topology/core_id"), "r") as core_id_file:
                        core_id = core_id_file.read().strip()
                        f.write(f"Core ID: {core_id}\n")

                    with open(os.path.join(cpu_path, "topology/physical_package_id"), "r") as package_id_file:
                        package_id = package_id_file.read().strip()
                        f.write(f"Package ID: {package_id}\n")

                    with open(os.path.join(cpu_path, "topology/core_siblings"), "r") as core_siblings_file:
                        core_siblings = core_siblings_file.read().strip()
                        f.write(f"Core siblings: {core_siblings}\n")

                except FileNotFoundError:
                    printThis = cpu_dir + "  " + cpu
                    f.write(printThis)
                    f.write("CPU topology information not available\n")

        f.write("-----------------------------------\n")
        f.write("CPU information gathering complete.\n")

if __name__ == "__main__":
    gather_cpu_info()
    print(f"CPU information saved to {output_file}")
