branch_name = "test8"
execution_plan = [
# (f"""Create a new branch call it {branch_name}-brewery-shop-example"""),

("""Can you explain to me what the repo is for? `README.md` should have some context for you"""),

("""Let's change the name of the project to craft-beers instead of jaffle shop. Can you help me make sure `profiles.yml`, `dbt_project.yml` and `README.md` are updated to reflect the new name of the project and databases? I dont want to see jaffle_shop in any of the code, docs or data. The name craft-beers is written in code as craft_beers.
Modify the readme/docs/config files to reflect the name 'craft-beers' instead of jaffle shop. The description is Brewery Shop (Craft Beer):  
Business: A small brewery selling various craft beers online and in-store.  
Data: raw_beers, raw_customers, raw_orders, raw_payments, raw_brewery_inventory.  
Focus: Inventory management, sales trends by beer type, customer demographics, and order fulfillment.
"""),

(f"""Modify the db name in `profiles.yml` to {branch_name}_craft_beers.duckdb"""),

("""What does the data files in `seeds` folder represent? Give 1 line description of each file."""),

("""Let's modify the data in the `seeds` folder to represent a brewery shop. Here is the description Brewery Shop (Craft Beer):  
Business: A small brewery selling various craft beers online and in-store.  
Data: raw_beers, raw_customers, raw_orders, raw_payments, raw_brewery_inventory.  
Focus: Inventory management, sales trends by beer type, customer demographics, and order fulfillment.  
Think about all the analytics required to help manager of the brewery shop.
"""),

("""What does the sql files in `models/staging` folder represent? Give 1 line description of each file. Descriptions can be found in schema.yml files if present."""),

("""Modify the staging files to reflect the new data in seed folder to represent brewery shop. For syntax use ref instead of source as its seed models you are relying on in staging models. Pay attention to the columns in the data in `seeds` folder and how you reference them in the staging models. The description is Brewery Shop (Craft Beer):  
Business: A small brewery selling various craft beers online and in-store.  
Data: raw_beers, raw_customers, raw_orders, raw_payments, raw_brewery_inventory.  
Focus: Inventory management, sales trends by beer type, customer demographics, and order fulfillment.
 
Make sure to add all the relevant models to staging with cover the new csv data and correct columns in staging models.
"""),

("""Make sure to add all the relevant files for new `seeds` that are not in `models/staging/schema.yml` and `models`."""),

("""What are the important models other than staging models in `models`? Modify the code in `models` to reflect the new data and usecase of the brewery shop manager.
Pay attention to the column names of the staging models and how you reference them in the models. Joining and aggregations should reference the staging models columns correctly."""),

("""What other models can be created for the manager of the store? It should not require any other additional data than what we have in our staging models `models/staging/schema.yml`. It is possible there are no other changes to me made. If that is the case, dont make any unneeded changes to the models."""),

("""/run dbt build"""),

("""Let's change the name of the project to craft-beers instead of jaffle shop. Can you help me make sure `dbt_project.yml` and `README.md` are updated to reflect the new name of the project? The name craft-beers is written in code as craft_beers.  
Modify the readme/docs/config files to reflect the name 'craft-beers' instead of jaffle shop. The description is Brewery Shop (Craft Beer):  
Business: A small brewery selling various craft beers online and in-store.  
Data: raw_beers, raw_customers, raw_orders, raw_payments, raw_brewery_inventory.  
Focus: Inventory management, sales trends by beer type, customer demographics, and order fulfillment."""),

("""Lets get Data Documentation for Brewery Shop (Craft Beer) complete. Look at all the md and yml files to make sure dbt docs have coverage for all the models and seeds and data. Modify the files in `models/docs.md`"""),
]