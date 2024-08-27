def load_requirements(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def create_execution_plan(branch_name, project_name, requirements):

    execution_plan = [

("""Can you explain to me what the repo is for? `README.md` should have some context for you"""),

(f"""Let's change the name of the project to {project_name} instead of jaffle shop. Can you help me make sure `profiles.yml`, `dbt_project.yml` and `README.md` are updated to reflect the new name of the project and databases? I dont want to see jaffle_shop in any of the code, docs or data. The name {project_name} is written in code as {project_name}.
Modify the readme/docs/config files to reflect the name '{project_name}' instead of jaffle shop. The description is \n {requirements}
"""),

(f"""Modify the db name in `profiles.yml` to {branch_name}_{project_name}.duckdb"""),

("""What does the data files in `seeds` folder represent? Give 1 line description of each file."""),

(f"""Let's modify the data in the `seeds` folder to represent the use case at hand. Here is the description \n {requirements}  

Think about all the analytics required to help manager of the {project_name}.
"""),

("""What does the sql files in `models/staging` folder represent? Give 1 line description of each file. Descriptions can be found in schema.yml files if present."""),

(f"""Modify the staging files to reflect the new data in seed folder to represent the use case at hand. For syntax use ref instead of source as its seed models you are relying on in staging models. Pay attention to the columns in the data in `seeds` folder and how you reference them in the staging models. The description is \n {requirements}


 
Make sure to add all the relevant models to staging with cover the new csv data and correct columns in staging models.
"""),

("""Make sure to add all the relevant files for new `seeds` that are not in `models/staging/schema.yml` and `models`."""),

(f"""What are the important models other than staging models in `models`? Modify the code in `models` to reflect the new data and usecase of the {project_name} manager.
Pay attention to the column names of the staging models and how you reference them in the models. Joining and aggregations should reference the staging models columns correctly."""),

(f"""What other models can be created for the manager of the store? It should not require any other additional data than what we have in our staging models `models/staging/schema.yml`. It is possible there are no other changes to me made. If that is the case, dont make any unneeded changes to the models."""),


(f"""Let's change the name of the project to {project_name} instead of jaffle shop. Can you help me make sure `dbt_project.yml` and `README.md` are updated to reflect the new name of the project? The name {project_name} is written in code as {project_name}.  
Modify the readme/docs/config files to reflect the name '{project_name}' instead of jaffle shop. The description is \n {requirements}
"""),

    ]

    return execution_plan