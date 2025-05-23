membros = {
    "Alice": {"cargo": "Moderador", "pontos": 50},
    "Bob": {"cargo": "Membro", "pontos": 30},
    "Carlos": {"cargo": "Moderador","pontos": 20}
}


totalpontos = 0
totalmoderador = 0
for nome, inf in membros.items():
    totalpontos += inf['pontos']
    if inf['cargo'] == 'Moderador':
        totalmoderador += 1

print(f'p:{totalpontos}, Moderador:{totalmoderador}')