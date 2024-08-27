with inventory as (

    select
        inventory_id,
        medication_name as medication,
        batch_number,
        expiration_date,
        quantity
    from {{ ref('stg_inventory') }}

),

alerts as (

    select
        inventory_id,
        medication,
        batch_number,
        expiration_date,
        quantity,
        case
            when quantity < 50 then 'Low Stock'
            when expiration_date < current_date + interval '30 days' then 'Expiring Soon'
            else 'Sufficient Stock'
        end as stock_status

    from inventory

)

select * from alerts
