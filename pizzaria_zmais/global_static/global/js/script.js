function RemoverItem (url) {
    const confirmar = confirm("Tem certeza que deseja remover esse Item?")
    if (confirmar) {
        window.location.href = url
    }
    else {
        alert("Operação cancelada")
    }
}