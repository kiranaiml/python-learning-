#"The Deep Learning Architect"
neural_network = {
    "model_name": "BrainNet-1",
    "layers": ["input", "hidden_1", "output"],
    "hyperparameters": {
        "learning_rate": 0.01,
        "batch_size": 32
    }
}
user_input=input("new layer to add:")
neural_network['layers'].append(user_input)
new_input=int(input("new batch size:"))
neural_network["hyperparameters"]["batch_size"]=new_input
if new_input>64:
    neural_network["Memory_warning"]="High RAM Usage!"
else:
    neural_network["Memory_warning"]="stable"
print("\n"+"="*40)
print("\n___The Deep Learning Architect___")
print("\n"+"="*40)
print(f"\nThe Model Name: {neural_network["model_name"]}")
print(f"The current Learning Rate:{neural_network["hyperparameters"]["learning_rate"]}")
print(f"The Memory Warning status:{neural_network["Memory_warning"]}")
print(f"The entire updated:{neural_network}")
print("\n"+"="*40)
print("\n       THANK YOU      ")
print("\n"+"="*40)