with source as (

    select * from {{ ref('cleaned_raw_prescriptions') }}

),

renamed as (

    select
        id as prescription_id,
        customer_id,
        medication,
        dosage,
        doctor_approval

    from source

)

select * from renamed
