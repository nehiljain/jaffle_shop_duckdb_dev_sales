with source as (

    select * from {{ ref('cleaned_raw_shipments') }}

),

renamed as (

    select
        id as shipment_id,
        order_id,
        courier,
        shipment_status,
        delivery_confirmation

    from source

)

select * from renamed
