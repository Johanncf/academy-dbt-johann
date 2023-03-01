select 
    count(distinct pedido_id) as numero_de_pedidos
from {{ ref('vendas') }}
having not(numero_de_pedidos > 30000)