with 
    clientes as (
        select
            *
        from
            {{ ref('stg_sap__clientes') }}
    ),

    lojas as (
        select
            *
        from
            {{ ref('stg_sap__lojas') }}
    ),

    pessoas as (
        select
            *
        from
            {{ ref('stg_sap__pessoas') }}
    ),

    joined as (
        select
            clientes.cliente_id
            , CASE WHEN 
                pessoas.nome is null
                THEN lojas.nome_loja
                ELSE pessoas.nome
              END as nome_cliente
            , CASE WHEN 
                lojas.nome_loja is null
                THEN 'pessoa_fisica'
                ELSE lojas.nome_loja
              END as nome_loja
        from
            clientes
            left join lojas on
                clientes.loja_id = lojas.loja_id
            left join pessoas on
                clientes.pessoa_id = pessoas.pessoa_id

    )

select * from joined