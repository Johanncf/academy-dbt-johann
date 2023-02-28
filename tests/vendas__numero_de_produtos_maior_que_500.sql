select 
    count(distinct produto_id) as numero_de_produtos
from {{ ref('stg_sap__produtos') }}
having not(numero_de_produtos > 500)