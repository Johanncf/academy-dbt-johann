select 
    count(distinct cliente_id) as numero_de_clientes
from {{ ref('vendas') }}
having not(numero_de_clientes > 19000)