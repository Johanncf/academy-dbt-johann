with 
    codes as (
        select 
            cast(countrylet as string) as nome_pais
            , cast(_2let as string) as sigla_2
            , cast(_3let as string) as sigla_3
        from {{ source('iso', 'countrycode')}}
    )

select * from codes