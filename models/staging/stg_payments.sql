select
    id as payment_id,
    order_id,
    payment_method,
    amount / 100 as amount  -- `amount` is currently stored in cents, so we convert it to dollars

from {{ ref('raw_payments') }}
