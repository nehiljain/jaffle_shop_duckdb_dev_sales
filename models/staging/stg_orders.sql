select
    id as order_id,
    customer_id,
    order_date,
    status,
    beer_id,
    quantity

from {{ ref('raw_orders') }}
