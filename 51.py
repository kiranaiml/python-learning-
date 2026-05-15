#"The Cloud Server Firewall"
server_data = {
    "region": ("ap-south-1", "Mumbai"), 
    "status": "Online",
    "threat_logs": ["login_fail", "timeout"], 
    "security": {
        "banned_ips": {"192.168.1.1", "10.0.0.5"}, 
        "admin_ips": {"127.0.0.1"} 
    }
}
ip=input("IP Address: ")
if ip in server_data["security"]["banned_ips"]:
    server_data["status"]="Under Attack!"
    server_data["threat_logs"].append("ddos_attempt")
elif ip in server_data["security"]["admin_ips"]:
    server_data["admin_access"]=True
else:
    server_data["active_users"]=[ip]
print("\n"+"="*40)
print("\n___The Cloud Server Firewall___")
print("\n"+"="*40)
print(f"\nThe Server Region: {server_data["region"][1]}")
print(f"The current Server Status: {server_data["status"]}")
print(f"The latest Threat Logs: {server_data["threat_logs"][-1]}")
print(f"The entire raw: {server_data}")
