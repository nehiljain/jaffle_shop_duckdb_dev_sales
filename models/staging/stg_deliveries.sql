with source as (

    select * from {{ ref('raw_deliveries') }}

),

renamed as (

    select
        id as delivery_id,
        order_id,
        store_id,
        delivery_date,
        delivery_time

    from source

)

select * from renamed
