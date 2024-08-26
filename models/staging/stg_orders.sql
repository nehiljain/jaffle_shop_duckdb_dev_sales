select
    id as order_id,
    user_id as customer_id,
    order_date,
    status,
    beer_type,
    quantity

from {{ ref('raw_orders') }}
