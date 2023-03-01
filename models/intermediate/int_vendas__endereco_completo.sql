with
    endereco as (
        select *
        from {{ ref('stg_sap__endereco') }}
    ),
    
    estado as (
        select *
        from {{ ref('stg_sap__estado') }}
    ),

    regiao as (
        select *
        from {{ ref('stg_sap__regiao') }}
    ),

    iso as (
        select *
        from {{ ref('stg_iso__codigo_paises') }}
    ),

    joined as (
        select
            endereco.endereco_id
            , endereco.cidade
            , estado.sigla_estado
            , estado.nome_estado
            , regiao.nome_regiao
            , iso.sigla_3
            , regiao.grupo
        
        from endereco
        left join estado on
            endereco.estado_id = estado.estado_id
        left join regiao on
            estado.regiao_id = regiao.regiao_id
        left join iso on
            regiao.sigla_pais = iso.sigla_2
    ) 

select * from joined
