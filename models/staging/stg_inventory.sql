with source as (

    select * from {{ ref('raw_inventory') }}

),

renamed as (

    select
        id as inventory_id,
        medication,
        batch_number,
        expiration_date,
        quantity

    from source

)

select * from renamed
