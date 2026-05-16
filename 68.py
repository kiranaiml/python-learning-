#The Cyber Security Log Filter
failed_attempts=[12,3,45,8,15,2]
threat_score=[attempts*100 for attempts in failed_attempts if attempts>10 ]
print(threat_score)
