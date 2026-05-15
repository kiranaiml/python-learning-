#"The AI Model Configurator"
model_config={
    "model_name":"vision-alpha",
    "accuracy_score":82.5,
    "datasets_used":["image","text,"]
}  
name=input("name of a new dataset(audio/video): ")
model_config["datasets_used"].append(name)
score=float(input("new accuracy score from the latest test:"))
model_config["accuracy_score"]=score
if score>90.0:
   model_config["status"] = "Ready for Deployment"
else:
    model_config["status"] = "Needs more training"
print("\n"+"="*40)
print("\n___ The AI Model Configurator___")
print("\n"+"="*40)
print(f"\nThe Model Name: {model_config["model_name"]}")
print(f"The Total Number of Datasets used: {len(model_config['datasets_used'])}")
print(f"\nThe Final Deployment Status: {model_config["status"]}")
print(f"\nThe data structure update.: {model_config["datasets_used"]}")
print("\n"+"="*40)
print("\n        THANK YOU FOR VISITING     ")
print("\n"+"="*40)
