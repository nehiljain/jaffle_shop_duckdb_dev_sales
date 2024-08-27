with source as (

    select * from {{ ref('raw_products') }}

),

renamed as (

    select
        id as product_id,
        product_name,
        category,
        price

    from source

)

select * from renamed
