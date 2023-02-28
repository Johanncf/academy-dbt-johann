with 
    regiao as (
        select 
            cast(territoryid as int) as regiao_id
            , cast(name as string) as nome_regiao
            , cast(countryregioncode as string) as sigla_pais
            , cast(`group` as string) as grupo
        from
            {{ source('sap_adw', 'salesterritory') }}
    )

select * from regiao