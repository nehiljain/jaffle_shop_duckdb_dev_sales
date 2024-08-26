# Testing dbt project: `craft_beers`

`craft_beers` is a fictional brewery shop. This dbt project transforms raw data from an app database into a customers and orders model ready for analytics.

<details>
<summary>

## What is this repo?

</summary>

Business: A small brewery selling various craft beers online and in-store.

Data: raw_beers, raw_customers, raw_orders, raw_payments, raw_brewery_inventory.

Focus: Inventory management, sales trends by beer type, customer demographics, and order fulfillment.

</details>

<details>
<summary>

## What's in this repo?

</summary>

This repo contains [seeds](https://docs.getdbt.com/docs/building-a-dbt-project/seeds) that includes some (fake) raw data from a fictional brewery app along with some basic dbt [models](https://docs.getdbt.com/docs/building-a-dbt-project/building-models), tests, and docs for this data.

The raw data consists of beers, customers, orders, and payments, with the following entity-relationship diagram:

![Brewery Shop ERD](/etc/jaffle_shop_erd.png)

</details>

## Why should I care about this repo?

If you're just starting your cloud data warehouse journey and are hungry to get started with dbt before your organization officially gets a data warehouse, you should check out this repo.

If you want to run 28 SQL operations with dbt in less than `1 second`, for free, and all on your local machine, you should check out this repo.
![dbt_performance](images/dbt_performance.png)

If you want an adrenaline rush from a process that used to take dbt newcomers `1 hour` and is now less than `1 minute`, you should check out this repo.

![dbt_full_deploy_commands](images/dbt_full_deploy_commands.png)

[Verified GitHub Action on dbt Performance](https://github.com/dbt-labs/jaffle_shop_duckdb/runs/7141529753?check_suite_focus=true#step:4:306)

## Running this project

Prerequisities: Python >= 3.5

### Mach Speed: No explanation needed
