with
    estado as (
        select 
            cast(stateprovinceid as int) as estado_id
            , cast(stateprovincecode as string) as sigla_estado
            , cast(name as string) as nome_estado
            , cast(territoryid as int) as regiao_id
        from
            {{ source('sap_adw', 'stateprovince') }}
    )

select * from estado