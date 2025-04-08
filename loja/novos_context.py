from .models import Pedido, ItensPedido, Cliente, Categoria, Tipo

# def carrinho(request):
#     quantidade_produtos_carrinho = 0
#     cliente = None  # Definimos o cliente como None inicialmente

#     if request.user.is_authenticated:
#         cliente = getattr(request.user, "cliente", None)  # Evita erro se cliente não existir

#         # Se o usuário está logado mas não tem um cliente, cria um automaticamente
#         if cliente is None:
#             cliente = Cliente.objects.create(cliente=request.user)

#     else:
#         if request.COOKIES.get("id_sessao"):
#             id_sessao = request.COOKIES.get("id_sessao")
#             cliente, _ = Cliente.objects.get_or_create(id_sessao=id_sessao)
#         else:
#             return {"quantidade_produtos_carrinho": quantidade_produtos_carrinho}

#     pedidos = Pedido.objects.filter(cliente=cliente, finalizado=False)

#     if pedidos.exists():
#         pedido = pedidos.first()  # Usa o primeiro encontrado
#     else:
#         pedido = Pedido.objects.create(cliente=cliente, finalizado=False)

#     # Agora `pedido` sempre existirá antes de ser usado
#     itens_pedido = ItensPedido.objects.filter(pedido=pedido)

#     for item in itens_pedido:
#         quantidade_produtos_carrinho += item.quantidade

#     return {"quantidade_produtos_carrinho": quantidade_produtos_carrinho}


def carrinho(request):
    quantidade_produtos_carrinho = 0
    if request.user.is_authenticated:
        cliente = request.user.cliente
    else:
        if request.COOKIES.get("id_sessao"):
            id_sessao = request.COOKIES.get("id_sessao")
            cliente, criado = Cliente.objects.get_or_create(id_sessao=id_sessao)
        else:
            return {"quantidade_produtos_carrinho": quantidade_produtos_carrinho}
    pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)
    itens_pedido = ItensPedido.objects.filter(pedido=pedido)
    for item in itens_pedido:
        quantidade_produtos_carrinho += item.quantidade
    return {"quantidade_produtos_carrinho": quantidade_produtos_carrinho}


def categorias_tipos(request):
    categorias_navegacao = Categoria.objects.all()
    tipos_navegacao = Tipo.objects.all()
    return {"categorias_navegacao": categorias_navegacao, "tipos_navegacao": tipos_navegacao}

def faz_parte_equipe(request):
    equipe = False
    if request.user.is_authenticated:
        if request.user.groups.filter(name="equipe").exists():
            equipe = True
    return {"equipe": equipe}
        