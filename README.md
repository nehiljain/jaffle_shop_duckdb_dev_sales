# Testing dbt project: `pharmacy`

`pharmacy` is an online pharmacy providing prescription and over-the-counter medications with home delivery. This dbt project transforms raw data from an app database into a customers and orders model ready for analytics.

<details>
<summary>

## What is this repo?

</summary>

What this repo _is_:

- A self-contained playground dbt project, useful for testing out scripts, and communicating some of the core dbt concepts.

What this repo _is not_:

- A tutorial — check out the [Getting Started Tutorial](https://docs.getdbt.com/tutorial/setting-up) for that. Notably, this repo contains some anti-patterns to make it self-contained, namely the use of seeds instead of sources.
- A demonstration of best practices — check out the [dbt Learn Demo](https://github.com/dbt-labs/dbt-learn-demo) repo instead. We want to keep this project as simple as possible. As such, we chose not to implement:
  - our standard file naming patterns (which make more sense on larger projects, rather than this five-model project)
  - a pull request flow
  - CI/CD integrations
- A demonstration of using dbt for a high-complex project, or a demo of advanced features (e.g. macros, packages, hooks, operations) — we're just trying to keep things simple here!

</details>

<details>
<summary>

## Online Pharmacy Use Case Description

**Business**: An online pharmacy providing prescription and over-the-counter medications with home delivery.

**Data**:

- `raw_customers`: Contains customer information including name, contact details, and address.
- `raw_prescriptions`: Tracks prescriptions, including medication name, dosage, and doctor’s approval.
- `raw_orders`: Logs customer orders, including order date, medication details, and order status.
- `raw_payments`: Records payment details, including payment method, amount, and transaction date.
- `raw_inventory`: Manages medication stock levels, including batch numbers, expiration dates, and quantities.
- `raw_shipments`: Tracks shipments, including courier details, shipment status, and delivery confirmation.

Limit the data to 10 customers, 30 orders, 6 products, 3 stores, 20 deliveries.
**Focus**:

- **Prescription Validation**: Ensure all orders for prescription medications have valid prescriptions linked.
- **Inventory Management**: Track stock levels, flag low inventory, and ensure medications are not expired.
- **Order Fulfillment**: Monitor order status, from placement to delivery, ensuring timely shipment.
- **Customer Segmentation**: Analyze customer purchasing patterns to identify frequent buyers and medication trends.
- **Compliance Monitoring**: Ensure data follows regulatory requirements (e.g., HIPAA) by tracking and validating prescriptions and customer information securely.

**Assumptions**:

- **Simplicity**: Focus on a single country’s regulatory environment to minimize compliance complexity.
- **Order Frequency**: Assumes customers refill prescriptions on a monthly basis, with occasional ad-hoc orders.
- **Medication Variety**: Limited to a basic selection of common prescription and OTC medications for simplicity.
- **Shipping Constraints**: Assumes standard shipping methods with no same-day delivery, to reduce complexity in shipment tracking.
- **Payment Methods**: Limited to credit cards and digital wallets to simplify payment processing.

</summary>

This repo contains [seeds](https://docs.getdbt.com/docs/building-a-dbt-project/seeds) that includes some (fake) raw data from a fictional app along with some basic dbt [models](https://docs.getdbt.com/docs/building-a-dbt-project/building-models), tests, and docs for this data.

The raw data consists of customers, orders, and payments, with the following entity-relationship diagram:

![Jaffle Shop ERD](/etc/jaffle_shop_erd.png)

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
