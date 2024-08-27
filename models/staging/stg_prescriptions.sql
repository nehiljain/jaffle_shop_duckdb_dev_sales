with source as (

    select * from {{ ref('raw_prescriptions') }}

),

renamed as (

    select
        id as prescription_id,
        customer_id,
        medication_name,
        dosage,
        doctor_approval

    from source

)

select * from renamed
