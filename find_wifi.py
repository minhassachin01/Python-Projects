import subprocess

collect_data = (
    subprocess.check_output(["netsh", "wlan", "show", "profiles"])
    .decode("utf-8")
    .split("\n")
)
wifi = [i.split(":")[1][1:-1] for i in collect_data if "All User Profile" in i]

for i in wifi:
    results = (
        subprocess
        .check_output(["netsh", "wlan", "show", "profile", i, "key=clear"])
        .decode("utf-8")
        .split("\n")
    )
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    
    try:
        
        print("{:<20}|  {:<}".format(i, results[0]))
    except IndexError:
        print("{:<20}|  {:<}".format(i, ""))
