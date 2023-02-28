with 
    pedidos as (
        select *
        from {{ ref('int_vendas__detalhe_pedidos') }}
    ),

    motivo_venda as (
        select *
        from {{ ref('int_vendas__motivo_vendas') }}
    ),

    produtos as (
        select *
        from {{ ref('stg_sap__produtos') }}
    ),

    cartao as (
        select *
        from {{ ref('stg_sap__cartao') }}
    ),

    clientes as (
        select *
        from {{ ref('int_vendas__clientes') }}
    ),

    endereco as (
        select *
        from {{ ref('int_vendas__endereco_completo') }}
    ),

    joined as (
        select 
            pedidos.pedido_id
            , pedidos.total_pedido
            , pedidos.status_pedido
            , pedidos.data_pedido
            , pedidos.ano_pedido
            , pedidos.mes_pedido
            , pedidos.dia_pedido
            , clientes.cliente_id
            , clientes.nome_cliente
            , clientes.nome_loja
            , pedidos.detalhe_pedido_id
            , pedidos.preco_unitario
            , pedidos.desconto_unitario
            , produtos.produto_id
            , produtos.nome_produto
            , pedidos.quantidade
            , CASE
                WHEN cartao.tipo_cartao is null THEN 'indefinido'
                ELSE cartao.tipo_cartao
              END as tipo_cartao
            , endereco.cidade
            , endereco.nome_estado
            , endereco.sigla_estado
            , endereco.nome_regiao
            , endereco.sigla_3
            , CASE
                WHEN motivo_venda.motivador is null THEN 'indefinido'
                ELSE motivo_venda.motivador
              END as motivo_venda
              
        from pedidos
        left join motivo_venda on
            pedidos.pedido_id = motivo_venda.pedido_id
        left join cartao on
            pedidos.cartao_id = cartao.cartao_id
        left join produtos on 
            pedidos.produto_id = produtos.produto_id
        left join clientes on
            pedidos.cliente_id = clientes.cliente_id
        left join endereco on
            pedidos.endereco_entrega_id = endereco.endereco_id
    )

select * from joined