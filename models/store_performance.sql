with deliveries as (

    select * from {{ ref('stg_deliveries') }}

),

orders as (

    select * from {{ ref('stg_orders') }}

),

payments as (

    select * from {{ ref('stg_payments') }}

),

store_sales as (

    select
        deliveries.store_id,
        sum(payments.amount) as total_sales,
        count(distinct orders.order_id) as number_of_orders
    from deliveries
    left join orders on deliveries.order_id = orders.order_id
    left join payments on orders.order_id = payments.order_id
    group by deliveries.store_id

),

final as (

    select
        stores.store_id,
        stores.store_name,
        stores.location,
        store_sales.total_sales,
        store_sales.number_of_orders
    from {{ ref('stg_stores') }} as stores
    left join store_sales on stores.store_id = store_sales.store_id

)

select * from final
