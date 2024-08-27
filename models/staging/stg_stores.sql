with source as (

    select * from {{ ref('raw_stores') }}

),

renamed as (

    select
        id as store_id,
        store_name,
        location

    from source

)

select * from renamed
