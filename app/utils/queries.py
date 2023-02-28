from services import DatavisService

def numero_pedidos_por_dimensao(dimension: str):
    return f'''
    SELECT COUNT(DISTINCT pedido_id) total, {dimension} 
    FROM `dbt_adventure_works.vendas` 
    GROUP BY `{dimension}`
    ORDER BY total DESC
    '''

def quantidade_comprada_por_dimensao(dimension: str):
    return f'''
    SELECT SUM(quantidade) total, {dimension} 
    FROM `dbt_adventure_works.vendas`
    GROUP BY {dimension}
    ORDER BY total DESC
    '''

def quantidade_comprada_serie_temporal():
    return f'''
        SELECT SUM(quantidade) total, (mes_pedido || '/' || ano_pedido) as data
        FROM `dbt_adventure_works.vendas`
        GROUP BY ano_pedido, mes_pedido
        ORDER BY ano_pedido, mes_pedido
    '''

def total_negociado_por_dimensao(dimension: str):
    return f'''
    SELECT CAST(ROUND(SUM(quantidade * preco_unitario)) as int) total, {dimension} 
    FROM `dbt_adventure_works.vendas`
    GROUP BY {dimension}
    ORDER BY total DESC
    '''

def filtros_metricas_totais(produto, tipo_cartao, data, cliente, status, cidade, estado, pais):
    WHERE_CLAUSE = ''

    PRODUTO = ''
    TIPO_CARTAO = ''
    DATA = ''
    CLIENTE = ''
    STATUS = ''
    CIDADE = ''
    ESTADO = ''
    PAIS = ''

    if produto:
        PRODUTO = f'nome_produto = "{produto}"'
    if tipo_cartao:
        TIPO_CARTAO = f'tipo_cartao = "{tipo_cartao}"'
    if data:
        DATA = f'data_pedido = "{data}"'
    if cliente:
        CLIENTE = f'nome_cliente = "{cliente}"'
    if status:
        STATUS = f'status_pedido = "{status}"'
    if cidade:
        CIDADE = f'cidade = "{cidade}"'
    if estado:
        ESTADO = f'nome_estado = "{estado}"'
    if pais:
        PAIS = f'sigla_3 = "{pais}"'
    
    CLAUSE = ' AND '.join([item for item in [PRODUTO, TIPO_CARTAO, DATA, CLIENTE, STATUS, CIDADE, ESTADO, PAIS] if item])

    if CLAUSE:
        WHERE_CLAUSE = f'WHERE {CLAUSE}'

    return WHERE_CLAUSE    

def pedidos_totais_filtrados(produto, tipo_cartao, data, cliente, status, cidade, estado, pais):
    WHERE_CLAUSE = filtros_metricas_totais(produto, tipo_cartao, data, cliente, status, cidade, estado, pais)

    return f'''
        SELECT COUNT(DISTINCT pedido_id) total
        FROM `dbt_adventure_works.vendas`
        {WHERE_CLAUSE}
    '''

def quantidade_total_filtrado(produto, tipo_cartao, data, cliente, status, cidade, estado, pais):
    WHERE_CLAUSE = filtros_metricas_totais(produto, tipo_cartao, data, cliente, status, cidade, estado, pais)

    return f'''
        WITH transformado as (
            SELECT DISTINCT detalhe_pedido_id, quantidade
            FROM `cea-adw-johann.dbt_adventure_works.vendas`
        )

        SELECT SUM(quantidade) total
        FROM transformado
        {WHERE_CLAUSE}
    '''

def total_negociado_filtrado(produto, tipo_cartao, data, cliente, status, cidade, estado, pais):
    WHERE_CLAUSE = filtros_metricas_totais(produto, tipo_cartao, data, cliente, status, cidade, estado, pais)

    return f'''
    WITH pedidos_unicos as (
        SELECT DISTINCT pedido_id, total_pedido, nome_cliente
        FROM `cea-adw-johann.dbt_adventure_works.vendas`
        {WHERE_CLAUSE}
    )

    SELECT ROUND(SUM(total_pedido), 2) total
    FROM pedidos_unicos
    '''

def ticket_medio_por_dimensao(ano_pedido, mes_pedido, cidade, nome_estado, sigla_3):
    
    WHERE_CLAUSE = ''

    ANO = ''
    MES = ''
    CIDADE = ''
    ESTADO = ''
    PAIS = ''

    if ano_pedido:
        ANO = f'ano_pedido = {ano_pedido}'
    if mes_pedido:
        MES = f'mes_pedido = {mes_pedido}'
    if cidade:
        CIDADE = f'cidade = "{cidade}"'
    if nome_estado:
        ESTADO = f'nome_estado = "{nome_estado}"'
    if sigla_3:
        PAIS = f'sigla_3 = "{sigla_3}"'
    
    CLAUSE = ' AND '.join([item for item in [ANO, MES, CIDADE, ESTADO, PAIS] if item])

    if CLAUSE:
        WHERE_CLAUSE = f'WHERE {CLAUSE}'

    return f'''
        SELECT 
            ROUND(AVG(preco_unitario), 2) total, 
            nome_produto
        FROM `dbt_adventure_works.vendas`

        {WHERE_CLAUSE}

        GROUP BY 
            nome_produto

        ORDER BY total DESC
    '''

def filtros_melhores_clientes(produto, tipo_cartao, motivo_venda, data, cidade, nome_estado, pais):
    WHERE_CLAUSE = ''

    PRODUTO = ''
    TIPO_CARTAO = ''
    DATA = ''
    CLIENTE = ''
    STATUS = ''
    CIDADE = ''
    ESTADO = ''
    PAIS = ''

    if produto:
        PRODUTO = f'nome_produto = "{produto}"'
    if tipo_cartao:
        TIPO_CARTAO = f'tipo_cartao = "{tipo_cartao}"'
    if data:
        DATA = f'data_pedido = "{data}"'
    if motivo_venda:
        CLIENTE = f'motivo_venda = "{motivo_venda}"'
    if cidade:
        CIDADE = f'cidade = "{cidade}"'
    if nome_estado:
        ESTADO = f'nome_estado = "{nome_estado}"'
    if pais:
        PAIS = f'sigla_3 = "{pais}"'
    
    CLAUSE = ' AND '.join([item for item in [PRODUTO, TIPO_CARTAO, DATA, CLIENTE, STATUS, CIDADE, ESTADO, PAIS] if item])

    if CLAUSE:
        WHERE_CLAUSE = f'WHERE {CLAUSE}'
    
    return WHERE_CLAUSE

def clientes_vs_lojas_total_negociado_por_dimensao(produto, tipo_cartao, motivo_venda, data, cidade, nome_estado, pais):
    WHERE_CLAUSE = filtros_melhores_clientes(produto, tipo_cartao, motivo_venda, data, cidade, nome_estado, pais)
    
    return f'''
    WITH transformado as (
        SELECT 
            DISTINCT pedido_id
            , CASE 
                WHEN nome_loja != 'pessoa_fisica' THEN 'loja'
                ELSE nome_loja
            END as cliente
            , total_pedido
        FROM `cea-adw-johann.dbt_adventure_works.vendas`
        {WHERE_CLAUSE}
    )

    SELECT SUM(total_pedido) total, cliente
    FROM transformado
    GROUP BY cliente
    '''

def melhores_clientes_total_negociado_por_dimensao(produto, tipo_cartao, motivo_venda, data, cidade, nome_estado, pais):
    WHERE_CLAUSE = filtros_melhores_clientes(produto, tipo_cartao, motivo_venda, data, cidade, nome_estado, pais)
    
    return f'''
    WITH pedidos_unicos as (
        SELECT DISTINCT pedido_id, total_pedido, nome_cliente, nome_loja
        FROM `cea-adw-johann.dbt_adventure_works.vendas`
        {WHERE_CLAUSE}
    )

    SELECT ROUND(SUM(total_pedido)) total, nome_cliente
    FROM pedidos_unicos
    WHERE nome_loja = 'pessoa_fisica'
    GROUP BY nome_cliente
    '''

def melhores_lojas_total_negociado_por_dimensao(produto, tipo_cartao, motivo_venda, data, cidade, nome_estado, pais):
    WHERE_CLAUSE = filtros_melhores_clientes(produto, tipo_cartao, motivo_venda, data, cidade, nome_estado, pais)
    
    return f'''
    WITH pedidos_unicos as (
        SELECT DISTINCT pedido_id, total_pedido, nome_loja, data_pedido
        FROM `cea-adw-johann.dbt_adventure_works.vendas`
        {WHERE_CLAUSE}
    )

    SELECT ROUND(SUM(total_pedido)) total, nome_loja
    FROM pedidos_unicos
    WHERE nome_loja != 'pessoa_fisica'
    GROUP BY nome_loja
    '''

def count_query_pais():
    return f'''
    SELECT COUNT(DISTINCT pedido_id) total, sigla_3 pais
    FROM `dbt_adventure_works.vendas` 
    GROUP BY sigla_3
    ORDER BY total DESC
    '''

def quantidade_comprada_por_pais():
    return f'''
    SELECT SUM(quantidade) total, sigla_3 pais
    FROM `dbt_adventure_works.vendas` 
    GROUP BY pais
    ORDER BY total DESC
    '''

def total_pedido_por_pais():
    return f'''
    WITH pedidos_unicos as (
        SELECT DISTINCT pedido_id, total_pedido, sigla_3 as pais
        FROM `dbt_adventure_works.vendas` 
    )

    SELECT CAST(ROUND(SUM(total_pedido)) as int) total, pais
    FROM pedidos_unicos 
    GROUP BY pais
    ORDER BY total DESC
    ''' 


def dimensoes_categorias():
    optionsDataService = DatavisService()

    nome_produto = optionsDataService.get_data(
        'SELECT DISTINCT nome_produto FROM `dbt_adventure_works.vendas`'
    )['nome_produto'].to_list()

    tipo_cartao = optionsDataService.get_data(
        'SELECT DISTINCT tipo_cartao FROM `dbt_adventure_works.vendas`'
    )['tipo_cartao'].to_list()

    data_pedido = optionsDataService.get_data(
        'SELECT DISTINCT data_pedido FROM `dbt_adventure_works.vendas` ORDER BY data_pedido DESC'
    )['data_pedido'].to_list()

    nome_cliente = optionsDataService.get_data(
        'SELECT DISTINCT nome_cliente FROM `dbt_adventure_works.vendas`'
    )['nome_cliente'].to_list()

    status_pedido = optionsDataService.get_data(
        'SELECT DISTINCT status_pedido FROM `dbt_adventure_works.vendas`'
    )['status_pedido'].to_list()
    
    cidade = optionsDataService.get_data(
        'SELECT DISTINCT cidade FROM `dbt_adventure_works.vendas`'
    )['cidade'].to_list()
    
    nome_estado = optionsDataService.get_data(
        'SELECT DISTINCT nome_estado FROM `dbt_adventure_works.vendas`'
    )['nome_estado'].to_list()

    sigla_3 = optionsDataService.get_data(
        'SELECT DISTINCT sigla_3 FROM `dbt_adventure_works.vendas`'
    )['sigla_3'].to_list()

    motivo_venda = optionsDataService.get_data(
    'SELECT DISTINCT motivo_venda FROM `dbt_adventure_works.vendas`'
    )['motivo_venda'].to_list()

    return [nome_produto, tipo_cartao, data_pedido, nome_cliente, status_pedido, cidade, nome_estado, sigla_3, motivo_venda]

def write_title(value: str, options: list):
    if value is None:
        return 'produto'

    for option in options:
        if option['value'] == value:
            label = option['label']['props']['children'][0]
            return f'{label}'