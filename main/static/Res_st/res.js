var mymodal = document.getElementById('mymodal')
mymodal.addEventListener('show.bs.modal', function (event) {
    var button = event.relatedTarget

    var cliente = button.getAttribute('data-bs-cli')
    var tel = button.getAttribute("data-bs-num")
    var stat = button.getAttribute('data-bs-st')
    var room = button.getAttribute("data-bs-quarto")
    var ide = button.getAttribute("data-bs-id")

    var modalTitle = mymodal.querySelector(".modal-title")
    var modalTel = mymodal.querySelector('.tele')
    var modalStatus = mymodal.querySelector('.status')
    var modalQuarto = mymodal.querySelector(".quarto")
    var modalDelete = mymodal.querySelector("#del")

    modalTitle.textContent = 'Nome do cliente: ' + cliente
    modalTel.textContent = 'Telefone: ' + tel
    modalStatus.textContent = 'Status: ' + stat
    modalQuarto.textContent = 'Tipo do Quarto: ' + room 
    modalDelete.href = `/murderer/${ide}/`

})